import json, requests
from flask import request

userID = 0


def signUp():
    #data1 = {'firstName':'Priyanka', 'lastName':'Deo', 'emailId':'deo.priyanka02@gmail.com', 'password':'dfer'}
    firstName = raw_input('Firstname ')
    lastName = raw_input('Lastname ')
    emailId = raw_input('email ')
    password = raw_input('password ')
    data1 = {'firstName':firstName, 'lastName':lastName, 'emailId':emailId, 'password':password}
    url = "http://127.0.0.1:5000/user/signUp"
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
    global userID
    email = raw_input('email ')
    password = raw_input('password ')
    data1 = {'emailId':email, 'password':password}
    url = "http://127.0.0.1:5000/user/login"
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.post(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text
    resp =  json.loads(r.text)
    print resp["UserID"]
    userID = resp["UserID"]

def createBoard():
    global userID
    boardName = raw_input('boardName ')
    boardDesc = raw_input('boardDesc ')
    category = raw_input('email ')
    isPrivate = raw_input('isPrivate ')
    data1 = {"boardName":boardName,"boardDesc":boardDesc,"category": category,"isPrivate": isPrivate}
    url = "http://127.0.0.1:5000/user/%s/boards/" % userID
    print "Create Board ::",url
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.post(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text

def getBoards():
    url = "http://127.0.0.1:5000/user/%s/boards/" % userID
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.get(url, headers = headers)
    print r.status_code
    print r.text

def getSingleBoard():
    print "Enter Board Name to be returned"
    boardName = raw_input('boardName ')
    url = "http://127.0.0.1:5000/user/%s/boards/%s" % (userID,boardName)
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.get(url, headers = headers)
    print r.status_code
    print r.text

def deleteBoard():
    global userID
    print "Enter Board Name to be deleted ::"
    boardName = raw_input('boardName ')
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    url = "http://127.0.0.1:5000/user/%s/boards/%s/" % (userID,boardName)
    r = requests.delete(url, headers = headers)
    print r.status_code
    print r.text

def updateBoard():
    global userID
    print "Enter Board Name to be updated ::"
    boardName = raw_input('boardName ')
    boardName1 = None
    boardDesc = None
    category = None
    isPrivate = None
    while True:
        var = raw_input("Enter fields to be updated :: 1.boardName 2.boardDesc 3.category 4.isPrivate 5.DoneEditing")
        if var == "1":
            boardName1 = raw_input('boardName ')
        if var == "2":
            boardDesc = raw_input('boardDesc ')
        if var == "3":
            category = raw_input('category ')
        if var == "4":
            isPrivate = raw_input('isPrivate ')
        if var == "5":
            break
    data1 = {"boardName":boardName1,"boardDesc":boardDesc,"category": category,"isPrivate": isPrivate}
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    url = "http://127.0.0.1:5000/user/%s/boards/%s/" % (userID,boardName)
    r = requests.put(url, data=json.dumps(data1) ,headers = headers)
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

    while True:
        var = raw_input("Enter an option 1. SignUp 2.SignIn 3.boards 4.getBoards 5.getSingleBoard 6.DeleteBoards")
        if var == '1':
            print "signUp"
            signUp()
        if var == '2':
            print "signIn"
            signIn()
        if var == '3':
            print "createBoard"
            createBoard()
        if var == '4':
            print "getBoards"
            getBoards()
        if var == '5':
            getSingleBoard()
        if var == '6':
            deleteBoard()
        if var == '7':
            updateBoard()

