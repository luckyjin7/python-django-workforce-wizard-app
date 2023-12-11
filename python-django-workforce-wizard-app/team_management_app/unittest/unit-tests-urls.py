import unittest
from django.test import Client

class TestUrls(unittest.TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_add(self):
        response = self.client.get("/add")
        self.assertEqual(response.status_code, 200)
        
    def test_edit(self):
        response = self.client.get("/edit/1")
        self.assertEqual(response.status_code, 200)
        
    def test_update(self):
        response = self.client.get("/update/1")
        self.assertEqual(response.status_code, 200)
        
    def test_delete(self):
        response = self.client.get("/delete/1")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()