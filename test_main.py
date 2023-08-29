from fastapi.testclient import TestClient
import unittest
from main import app

client = TestClient(app)

class TestFibonacciEndpoint(unittest.TestCase):

    def test_negative_input(self):
        response = client.get("/fib?n=-5")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"status":400,"message":"Bad request."})
        
    def test_zero_input(self):
        response = client.get("/fib?n=0")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"status":400,"message":"Bad request."})

    def test_one_input(self):
        response = client.get("/fib?n=1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 1})

    def test_two_input(self):
        response = client.get("/fib?n=2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 1})
        
    def test_five_input(self):
        response = client.get("/fib?n=5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 5})
        
    def test_large_input(self):
        response = client.get("/fib?n=10")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 55})

if __name__ == '__main__':
    unittest.main()