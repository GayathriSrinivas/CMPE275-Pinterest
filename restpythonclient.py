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
    #print resp['hello']
    url_data = []
    meth_data = []
    get_items(resp, "url", url_data)
    get_items(resp, "method", meth_data)
    print url_data
    print meth_data
    #print url_fil, url_meth
    #print meth_fil, meth_meth


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

def updateBoard():
    data1 = {"boardName":"Summer Wear","boardDesc":"Cool clothes for summer","category": "Clothes","isPrivate": "False"}
    url = "http://127.0.0.1:5000/user/boards"
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.put(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text
		    
def deleteBoard():
    data1 = {"boardName":"Summer Wear","boardDesc":"Cool clothes for summer","category": "Clothes","isPrivate": "False"}
    url = "http://127.0.0.1:5000/user/boards"
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.delete(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text

def createPins():
    data1 = {"pinName" : "Bucketlist - Summer clothes shopping - check :)" ,"pinImage" : "wardrobe.jpg","pinDesc" : "Awesome Summer discounts at Paragon Mall!!Check it out"}
    url = "http://127.0.0.1:5000/user/boards"
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.post(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text

def updatePins():
    data1 = {"pinName" : "Bucketlist - Summer clothes shopping - check :)" ,"pinImage" : "wardrobe.jpg","pinDesc" : "Awesome Summer discounts at Paragon Mall!!Check it out"}
    url = "http://127.0.0.1:5000/user/boards"
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.put(url, data=json.dumps(data1),  headers = headers)
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

def deletePins():
    data1 = {"pinName" : "Bucketlist - Summer clothes shopping - check :)" ,"pinImage" : "wardrobe.jpg","pinDesc" : "Awesome Summer discounts at Paragon Mall!!Check it out"}
    url = "http://127.0.0.1:5000/user/boards"
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.delete(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text


def createComment():
    data1 = {"Comment":"this my comment"}
    url = "http://127.0.0.1:5000/user/"
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.post(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text

def updateComment():
    data1 = {"Comment":"this my comment"}
    url = "http://127.0.0.1:5000/user/boards"
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.put(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text
		    
def deleteComment():
    data1 = {"Comment":"this my comment"}
    url = "http://127.0.0.1:5000/user/boards"
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.delete(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text

def get_items(json_data, key, data_list):				#Function to parse json 
    if type(json_data) is dict:
        for item_key in json_data:
            if type(json_data[item_key]) in (list, dict):
                get_items(json_data[item_key], key, data_list)
            elif item_key == key:
                print "********", json_data[item_key]
		data_list.append(json_data[item_key])
		#perform_operation(json_data[item_key], json_data['url'], json_data['method'])
    if type(json_data) == str:
        json_data = json.loads(json_data)
    elif type(json_data) is list:
        for item in json_data:
            if type(item) in (list, dict):
                get_items(item, key, data_list)
"""
def perform_operation(pdId, url, meth):		#Function to store required items info
    filtered_data[pdId] = url.replace("\\", "")	#Price of required items
    meth_data[pdId] = meth.replace("\\", "")	#Urls of the required items
"""
if __name__ == '__main__':
    var = raw_input("Enter an option 1. SignUp 2.SignIn")
    if var == '1':
        signUp()
    if var == '2':
        signIn()
