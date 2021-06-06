import json
import requests
from requests.api import request

url = "https://petstore.swagger.io/v2/user/"

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}
# With json.dumps works good
def post_req(user_name):
    data1 = json.dumps({
    "id": 255,
    "username": "TestingUser1",
    "firstName": "Test_user1",
    "lastName": "Test_userone",
    "email": "test_userone@gmail.com",
    "password": "Qwerty123",
    "phone": "380551233211",
    "userStatus": 99})
    r = requests.post (url,headers=headers,data = data1)
    return (r)

response = post_req("testuser1")
print (response.json())
print (response.json()['code'])
print (response.json()['type'] == 'unknown')
print (response.status_code == 200)

#Why this is not working?
#def post_req1(user_name):
    #data_payload = dict (id = 255,
    #username = 'testuser',
    #firstname = 'testuser1',
    #lastname = 'testuser11',
    #email = 'test@gmail.com',
    #password = 'Qwerty123',
    #phone = '380551233211',
    #userstatus = 99)
    #r1 = requests.post (url,headers=headers,data = data_payload)
    #return (print (r1.text))

#check = post_req1("testuser2")
#print (check)

def get_request (name):
    return requests.get (url + f"{name}",headers=headers)

get_r = get_request("TestingUser1")
print (get_r)
print (get_r.json()['username'])
print (get_r.json()['username'] == 'TestingUser1')