import json
from database.models import Users
from .basecase import BaseCase

class TestUserPermisions(BaseCase):
    def test_admin_permission(self):
        #Given 
        new_admin = json.dumps({
            "email":"admin@gmail.com",
            "password":"jhsfsfgsf",
            "role": "admin"
        })
        new_admin2 = json.dumps({
            "email":"admin@gmail.com",
            "password":"jhsfsfgsf",
            "role": "admin"
        })
        admin_payload = json.dumps({
            "email":"admin2@gmail.com",
            "password":"jhsfsfgsf",
            "role": "admin"
        })

        user_payload = json.dumps({
            "email":"user@gmail.com",
            "password":"jhsfsfgsf",
        })

        new_user = json.dumps({
            "email":"newuser@gmail.com",
            "password":"jhsfsfgsf"
        })





        #When
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=admin_payload)
        
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=new_admin)
        admin_id = response.json['id']
        
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        user_id = response.json['id']
        #login admin
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data = admin_payload)

        token = response.json['token']
        print(token)
        #create_user
        response = self.app.post('/api/users', headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}, data=new_user)
        self.assertEqual(200, response.status_code)

        #create admin
        response = self.app.post('/api/users', headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}, data=new_admin2)
        self.assertNotEqual(200, response.status_code)

        #remove user
        response = self.app.delete('/api/user/'+user_id, headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}, data=new_user)
        self.assertEqual(200, response.status_code)

        #remove admin
        response = self.app.delete('/api/users/'+admin_id, headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}, data=new_admin)
        self.assertNotEqual(200, response.status_code)
        print(response.json)
        #update role
        response = self.app.put('/api/users/'+admin_id, headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}, data={'role':""})
        self.assertNotEqual(200, response.status_code)
        print(response.json)
        response = self.app.put('/api/users/'+user_id, headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}, data={'role':"admin"})
        print(response.json)
        self.assertNotEqual(200, response.status_code)
        # #update disco
        response = self.app.put('/api/users/'+user_id,headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}, data={'disco':"abuja"})
        print(response.json)
        self.assertEqual(200, response.status_code)

        # #

    def test_user_permission(self):
         #Given 
        new_admin = json.dumps({
            "email":"admin@gmail.com",
            "password":"jhsfsfgsf",
            "role": "admin"
        })
        new_admin2 = json.dumps({
            "email":"admin@gmail.com",
            "password":"jhsfsfgsf",
            "role": "admin"
        })
        admin_payload = json.dumps({
            "email":"admin2@gmail.com",
            "password":"jhsfsfgsf",
            "role": "admin"
        })

        user_payload = json.dumps({
            "email":"user@gmail.com",
            "password":"jhsfsfgsf",
        })

        new_user = json.dumps({
            "email":"newuser@gmail.com",
            "password":"jhsfsfgsf"
        })





        #When
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=admin_payload)
        
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=new_admin)
        admin_id = response.json['id']
        
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        user_id = response.json['id']
        #login admin
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data = user_payload)

        token = response.json['token']
        
        #create_user
        response = self.app.post('/api/users', headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}, data=new_user)
        self.assertNotEqual(200, response.status_code)

        #create admin
        response = self.app.post('/api/users', headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}, data=new_admin2)
        self.assertNotEqual(200, response.status_code)

        #remove user
        response = self.app.delete('/api/user/'+user_id, headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}, data=new_user)
        self.assertNotEqual(200, response.status_code)

        #remove admin
        response = self.app.delete('/api/users/'+admin_id, headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}, data=new_admin)
        self.assertNotEqual(200, response.status_code)

        #update role
        response = self.app.put('/api/users/'+admin_id, headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}, data={'role':""})
        self.assertNotEqual(200, response.status_code)

        response = self.app.put('/api/users/'+user_id, headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}, data={'role':"admin"})
        self.assertNotEqual(200, response.status_code)
       
        
        