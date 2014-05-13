import json, requests
from flask import request

userID = 0
global host

def signUp():
    #data1 = {'firstName':'Priyanka', 'lastName':'Deo', 'emailId':'deo.priyanka02@gmail.com', 'password':'dfer'}
    firstName = raw_input('Firstname ')
    lastName = raw_input('Lastname ')
    emailId = raw_input('email ')
    password = raw_input('password ')
    data1 = {'firstName':firstName, 'lastName':lastName, 'emailId':emailId, 'password':password}
    url = "http://127.0.0.1:5000/users/signUp/"
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.post(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text    
    resp = json.loads(r.text)
    #print r.text.Links
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
    url = "http://127.0.0.1:5000/users/login/"
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.post(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text
    if (r.status_code == 201):
        resp =  json.loads(r.text)
        print resp["UserID"]
        userID = resp["UserID"]
        return userID
    else:
        print "Invalid email and password"
        return None

def createBoard():
    global userID
    boardName = raw_input('boardName ')
    boardDesc = raw_input('boardDesc ')
    category = raw_input('category ')
    isPrivate = raw_input('isPrivate ')
    data1 = {"boardName":boardName,"boardDesc":boardDesc,"category": category,"isPrivate": isPrivate}
    url = "http://192.168.0.100:5000/users/%s/boards/" % userID
    print "Create Board ::",url
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.post(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text

def getBoards():
    url = "http://127.0.0.1:5000/users/%s/boards/" % userID
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.get(url, headers = headers)
    print r.status_code
    print r.text

def getSingleBoard():
    print "Enter Board Name to be returned"
    boardName = raw_input('boardName ')
    url = "http://" + host + "users/%s/boards/%s" % (userID,boardName)
    print "#######", url
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.get(url, headers = headers)
    print r.status_code
    print r.text

def deleteBoard():
    global userID
    print "Enter Board Name to be deleted ::"
    boardName = raw_input('boardName ')
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    url = "http://127.0.0.1:5000/users/%s/boards/%s/" % (userID,boardName)
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
    url = "http://127.0.0.1:5000/users/%s/boards/%s/" % (userID,boardName)
    r = requests.put(url, data=json.dumps(data1) ,headers = headers)
    print r.status_code
    print r.text
		    

def createPins():
    global userID
    print "Enter Board Name to be updated ::"
    #boardName = raw_input('boardName ')
    #pinName = raw_input('pinName ')
    #boardDesc = raw_input('boardDesc ')
    #category = raw_input('category ')
    #isPrivate = raw_input('isPrivate ')
    #'/users/<int:user_id>/boards/<string:boardName>/pins/
    data1 = {"pinName" : "Bucketlist - Summer clothes shopping - check :)" ,"pinImage" : "wardrobe.jpg","pinDesc" : "Awesome Summer discounts at Paragon Mall!!Check it out"}
    url = "http://"+ host + "/users/%s/boards/%s/pins/" % (userID,boardName)
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.post(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text

def getSinglePin():
    global userID
    print "Enter Board Name to be returned"
    boardName = raw_input('boardName ')
    pinId = raw_input('pinNum ')
    url = "http://"+host+"/users/%s/boards/%s/pins/%s/" % (userID,boardName, pinId)
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.get(url, headers = headers)
    print r.status_code
    print r.text

def getPins():
    global userID
    print "Enter Board Name to be returned"
    boardName = raw_input('boardName ')
    url = "http://127.0.0.1:5000/users/%s/boards/%s/pins/" % (userID,boardName)
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.get(url, headers = headers)
    print r.status_code
    print r.text

def deletePins():
    global userID
    print "Enter Board Name to be returned"
    boardName = raw_input('boardName ')
    pinId = raw_input('pinNum ')
    url = "http://127.0.0.1:5000/users/%s/boards/%s/pins/%s/" % (userID,boardName,pinId)
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.delete(url, headers = headers)
    print r.status_code
    print r.text


def updatePins():
    #data1 = {"pinName" : "Bucketlist - Summer clothes shopping - check :)" ,"pinImage" : "wardrobe.jpg","pinDesc" : "Awesome Summer discounts at Paragon Mall!!Check it out"}
    data1 = {
    "pinName" : "Bring out the bikinis!!!!" ,
    "pinImage" : "bikinibabe.jpg",
    "pinDesc" : "Have been waiting all year to show dese off!! :P"
    }
    url = "http://127.0.0.1:5000/users/boards"
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


def updateComment():
    global userID
    print "Enter Comment Id to be updated ::"
    boardName = raw_input('boardName')
    pin_Id = raw_input('pin_Id')
    comment_Id1 = None
    pinComment = None
    while True:
        varc = raw_input("Enter fields to be updated :: 1.comment_Id 2.pinComment 3.Done Editing")
        if varc == "1":
            comment_Id1 = raw_input('comment_Id')
        if varc == "2":
            pinComment = raw_input('pinComment')
        if varc == "3":
            break
    data1 = {"comment_Id": comment_Id1, "pinComment": pinComment}
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    url = "http://127.0.0.1:5000/users/%s/boards/%s/pins/%s/comments/" % (userID, boardName, pin_Id)
    r = requests.put(url, data=json.dumps(data1),  headers=headers)
    print r.status_code
    print r.text
		    
def deleteComment():
    boardname = raw_input("Enter board name")
    pinId = raw_input("Enter pin id")
    commentId = raw_input("Enter comment id")
    #data1 = {"Comment":"this my comment"}
    url = "http://127.0.0.1:5000/users/%s/boards/%s/pins/%s/comments/%s" %(userID, boardname, pinId, commentId)
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.delete(url, data=json.dumps(data1),  headers = headers)
    print r.status_code
    print r.text

def getComment():
    boardname = raw_input("Enter board name")
    pinId = raw_input("Enter pin id")
    url = "http://127.0.0.1:5000/users/%s/boards/%s/pins/%s/comments" % (userID, boardname, pinId)
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.get(url, headers = headers)
    print r.status_code
    print r.text

def createComment():
    #data1 = {"Comment":"this my comment"}
    boardname = raw_input("Enter board name")
    pinId = raw_input("Enter pin id")
    url = "http://127.0.0.1:5000/users/%s/boards/%s/pins/%s/comments" % (userID, boardname, pinId)
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.post(url, data=json.dumps(data1),  headers = headers)
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
def start_boards():
    while True:
        option = raw_input("Enter an option 1.boards 2.getBoards 3.getSingleBoard 4.DeleteBoards 5.UpdateBoards 6.Exit")
        if option == '1':
            print "createBoard"
            createBoard()
        if option == '2':
            print "getBoards"
            getBoards()
        if option == '3':
            getSingleBoard()
        if option == '4':
            deleteBoard()
        if option == '5':
            updateBoard()
        if option == '6':
            main_options()

def start_pins():
    while True:
        option = raw_input("Enter an option 1.pins 2.getPins 3.getSinglePin 4.DeletePin 5.UpdatePin 6.Exit")
        if option == '1':
            print "createPin"
            createPins()
        if option == '2':
            print "getpins"
            getPins()
        if option == '3':
            getSinglePin()
        if option == '4':
            deletePins()
        if option == '5':
            updatePins()
        if option == '6':
            main_options()
     
def start_comments():
    while True:
        option = raw_input("Enter an option 1.comments 2.getcomments 3.DeleteComment 4.UpdateComment 5.Exit")
        if option == '1':
            print "createBoard"
            createComment()
        if option == '2':
            print "getBoards"
            getComment()
        if option == '3':
            deleteComment()
        if option == '4':
            updateComment()
        if option == '5':
            main_options()

def main_options():
    opt = raw_input("Enter an option 1. Boards 2.Pins 3. Comments 4.Exit")
    if opt == '1':
        start_boards()
    if opt == '2':
        start_pins()        
    if opt == '3':
        start_comments()
    else:
        exit()

if __name__ == '__main__':
    host = raw_input("The host id: ")
    while True:
        var = raw_input("Enter an option 1. SignUp 2.SignIn")
        if var == '1':
            print "signUp"
            signUp()
            var = '2'
        if var == '2':
            print "signIn"
            code = signIn()
        if code:
            main_options()


