#!/usr/bin/python3

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.user = User()
    
    def test_email_initial_value(self):
        self.assertEqual(self.user.email, "")
    
    def test_password_initial_value(self):
        self.assertEqual(self.user.password, "")
    
    def test_first_name_initial_value(self):
        self.assertEqual(self.user.first_name, "")
    
    def test_last_name_initial_value(self):
        self.assertEqual(self.user.last_name, "")
    
    def test_email_assignment(self):
        self.user.email = "test@example.com"
        self.assertEqual(self.user.email, "test@example.com")
    
    def test_password_assignment(self):
        self.user.password = "password123"
        self.assertEqual(self.user.password, "password123")
    
    def test_first_name_assignment(self):
        self.user.first_name = "John"
        self.assertEqual(self.user.first_name, "John")
    
    def test_last_name_assignment(self):
        self.user.last_name = "Doe"
        self.assertEqual(self.user.last_name, "Doe")

if __name__ == '__main__':
    unittest.main()

