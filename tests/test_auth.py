
import json
from database.models import Users
from .basecase import BaseCase

class SignupTest(BaseCase):
    def test_successful_signup(self):
        # Given
        payload = json.dumps({
            "email": "sa.ayinda@gmail.com",
            "password": "deaddsdjs",
            "disco":"abuja",
            "role":"admin"
        })
        # When
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)
        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
    def test_unsuccesful_signup(self):
        
        #Given
        payload = json.dumps({
            "email": "sa.ayinda@gmail.com",
            "password": "deaddsdjs",
            "disco":"abuja",
            "role":"admin"
        })

        #when
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        #Then

        self.assertNotEqual(200, response.status_code)

class TestUserLogin(BaseCase):
    def test_successful_login(self):

        # Given
        payload = json.dumps({
            "email": "sa.ayinda@gmail.com",
            "password": "deaddsdjs",
            "disco":"abuja",
            "role":"admin"
        })
        
        # When
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)
        
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=payload)
        # Then
        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)
    def test_unsuccesful_login(self):
        payload = json.dumps({
            "email":"sjdnsd@gmail.com",
            "password":"skdnsnsfn"
        })
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=payload)
        
        self.assertNotEqual(200, response.status_code)

