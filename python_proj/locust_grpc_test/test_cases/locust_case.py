from locust import HttpLocust, TaskSet, task, between


class UserBehaviour(TaskSet):

    @task(1)
    def test_say_hello(self):
        self.client.get('/')


class WebsiteUser(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(1, 2)
