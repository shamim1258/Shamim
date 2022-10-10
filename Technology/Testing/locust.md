# Locust

-  Library for load or performance testing.
-  It provides terminal plus web interface for monitoring testing output.
-  **Setup :**
   -  `pip install locust`
   -  Create `locustfile.py` under project directory where manage.py file exists.
^
    from locust import HttpLocust, TaskSet, task, HttpUser
    class UserBehavior(TaskSet):
    
    @task
    def put_tests(self):
        self.client.put("http://127.0.0.1:8000/apix/orderudpate/", {
                "OrderNumber": "2-13272967743",
                "OrderType": "Termination",
                "OrderStatus": "Cancelled"
        },
        headers = {"authorization": "Basic a2hhbjUzMDpzaGFtaW1AZGV2"}
        )

    class WebsiteUser(HttpUser):
        tasks = [UserBehavior]
^
   -  To run locust server `locust --host=http://127.0.0.1:8089`
   -  To access web interface `http://localhost:8089/`
