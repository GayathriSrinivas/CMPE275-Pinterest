import json, requests
from flask import request

def signUp():
    #data1 = {'firstName':'Priyanka', 'lastName':'Deo', 'emailId':'deo.priyanka02@gmail.com', 'password':'dfer'}
    firstName = raw_input('Firstname ')
    lastName = raw_input('Lastname ')
    email = raw_input('email ')
    password = raw_input('password ')
    data1 = {'firstName':firstName, 'lastName':lastName, 'email':email, 'password':password}
    url = "http://127.0.0.1:5000/user/login"
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.post(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text    
    resp = json.loads(r.text)
    print resp['hello']

def signIn():
    #data1 = {'email':'deo.priyanka02@gmail.com', 'password':'dfer'}
    email = raw_input('email ')
    password = raw_input('password ')
    data1 = {'emailId':email, 'password':password}
    url = "http://127.0.0.1:5000/user/add"
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.post(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text

def createBoard():
    data1 = {"boardName":"Summer Wear","boardDesc":"Cool clothes for summer","category": "Clothes","isPrivate": "False"}
    url = "http://127.0.0.1:5000/user/add"
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.post(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text

def createPins():
    data1 = {"pinName" : "Bucketlist - Summer clothes shopping - check :)" ,"pinImage" : "wardrobe.jpg","pinDesc" : "Awesome Summer discounts at Paragon Mall!!Check it out"}
    url = "http://127.0.0.1:5000/user/boards"
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.post(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text
    ######PUT############
    #payload = {'username':'bob', 'email':'fedgr'}
    #r=requests.put("rghj.com/endpt", data = payload)
    ######DELETE############
    #payload = {'some':'data'}
    #headers = {'content-type': 'application/json'}
    #url = "https://www.toggl.com/api/v6/" + data_description + ".json"
    #response = requests.delete(url, data=json.dumps(payload), headers=headers,auth=HTTPBasicAuth(toggl_token, 'api_token'))

if __name__ == '__main__':
    var = raw_input("Enter an option 1. SignUp 2.SignIn")
    if var == '1':
        signUp()
    if var == '2':
        signIn()
