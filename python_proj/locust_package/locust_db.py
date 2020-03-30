import six
import requests
import threading
from itertools import chain
from influxdb import InfluxDBClient
from locust import runners
from locust.stats import sort_stats
from locust.runners import SlaveLocustRunner, MasterLocustRunner

__all__ = ['start']
interval = 5        # interval time for save data
client = InfluxDBClient('localhost', 8086, database='locust_test')


def get_locust_stats_by_web_api():
    print("get_locust_stats")
    try:
        start_url = f'http://localhost:8089/stats/requests'
        print(start_url)
        return requests.get(start_url).json()
    except Exception as e:
        print(e)


def get_locust_stats():
    stats = []

    for s in chain(sort_stats(runners.locust_runner.request_stats), [runners.locust_runner.stats.total]):
        stats.append({
            "method": s.method,
            "name": s.name,
            "num_requests": s.num_requests,
            "num_failures": s.num_failures,
            "avg_response_time": s.avg_response_time,
            "min_response_time": s.min_response_time or 0,
            "max_response_time": s.max_response_time,
            "current_rps": s.current_rps,
            "median_response_time": s.median_response_time,
            "avg_content_length": s.avg_content_length,
        })

    errors = [e.to_dict() for e in six.itervalues(runners.locust_runner.errors)]

    # Truncate the total number of stats and errors displayed since a large number of rows will cause the app
    # to render extremely slowly. Aggregate stats should be preserved.
    report = {"stats": stats[:500], "errors": errors[:500]}

    if stats:
        report["total_rps"] = stats[len(stats) - 1]["current_rps"]
        report["fail_ratio"] = runners.locust_runner.stats.total.fail_ratio
        report[
            "current_response_time_percentile_95"] = runners.locust_runner.stats.total.get_current_response_time_percentile(
            0.95)
        report[
            "current_response_time_percentile_50"] = runners.locust_runner.stats.total.get_current_response_time_percentile(
            0.5)

    is_distributed = isinstance(runners.locust_runner, MasterLocustRunner)
    if is_distributed:
        slaves = []
        for slave in runners.locust_runner.clients.values():
            slaves.append({"id": slave.id, "state": slave.state, "user_count": slave.user_count})

        report["slaves"] = slaves

    report["state"] = runners.locust_runner.state
    report["user_count"] = runners.locust_runner.user_count

    return report


def save_to_db(project_name, host, rep):
    print('save_to_db')
    save_summary(project_name, host, rep)
    save_data(project_name, host, rep, 'errors')
    save_data(project_name, host, rep, 'stats')


def save_summary(project_name, host, rep):
    summary = [
        {
            "measurement": "summary",
            "tags": {
                "host": host,
                "project_name": project_name
            },
            "fields": {
                "current_response_time_percentile_50": rep['current_response_time_percentile_50'],
                "current_response_time_percentile_95": rep['current_response_time_percentile_95'],
                "fail_ratio": rep['fail_ratio'],
                "total_rps": rep['total_rps'],
                "user_count": rep['user_count']
            }
        }
    ]
    client.write_points(summary)


def save_data(project_name, host, rep, data_name):
    data_list = rep[data_name]
    summary = [
        {
            "measurement": data_name,
            "tags": {
                "host": host,
                "project_name": project_name,
                "path": data['name']
            },
            "fields": data
        } for data in data_list
    ]
    client.write_points(summary)


def get_locust_host():
    if runners.locust_runner.host:
        host = runners.locust_runner.host
    elif len(runners.locust_runner.locust_classes) > 0:
        host = runners.locust_runner.locust_classes[0].host
    else:
        host = None

    return host


def monitor(project_name):
    print("start monitoring")
    slave = isinstance(runners.locust_runner, SlaveLocustRunner)
    if slave:
        print('is slave, will not rerun')
        return

    try:
        rep = get_locust_stats()
        if rep['state'] == 'running':
            host = get_locust_host()
            save_to_db(project_name, host, rep)
            print(f'is_slave: {slave}, host: {host}, project_name: {project_name}')
        else:
            print('it is not running now')
    except Exception as e:
        print(e)

    timer = threading.Timer(interval, monitor, args=[project_name])
    timer.start()


def start(*args, **kwargs):
    timer = threading.Timer(5, monitor, args=args, kwargs=kwargs)
    timer.start()
    # monitor('locust_monitoring')