import json
import requests
import os

global host
global userID

def signUp():
    firstName = raw_input('Firstname')
    lastName = raw_input('Lastname')
    emailId = raw_input('email')
    password = raw_input('password')
    data1 = {'firstName': firstName, 'lastName': lastName, 'emailId': emailId, 'password': password}
    url = "http://" + host + "/users/signUp/"
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    r = requests.post(url, data=json.dumps(data1), headers=headers)
    print r.status_code
    print r.text
    resp = json.loads(r.text)
    url_data = []
    meth_data = []
    get_items(resp, "url", url_data)
    get_items(resp, "method", meth_data)
    print url_data
    print meth_data


def signIn():
    global userID
    email = raw_input('email')
    password = raw_input('password')
    data1 = {'emailId': email, 'password': password}
    url = "http://" + host + "/users/login/"
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    r = requests.post(url, data=json.dumps(data1), headers=headers)
    print r.status_code
    print r.text
    if r.status_code == 201:
        resp = json.loads(r.text)
        print resp["UserID"]
        userID = resp["UserID"]
        return userID
    else:
        print "Invalid email and password"
        return None


def createBoard():
    global userID
    boardName = raw_input('boardName')
    boardDesc = raw_input('boardDesc')
    category = raw_input('category')
    isPrivate = raw_input('isPrivate')
    data1 = {"boardName": boardName, "boardDesc": boardDesc, "category": category, "isPrivate": isPrivate}
    url = "http://" + host + "/users/%d/boards/" % userID
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    r = requests.post(url, data=json.dumps(data1), headers=headers)
    print r.status_code
    print r.text


def getBoards():
    global userID
    url = "http://" + host + "/users/%d/boards/" % userID
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    r = requests.get(url, headers=headers)
    print r.status_code
    print r.text


def getSingleBoard():
    global userID
    print "Enter Board Name to be returned"
    boardName = raw_input('boardName')
    url = "http://" + host + "/users/%d/boards/%s/" % (userID, boardName)
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    r = requests.get(url, headers=headers)
    print r.status_code
    print r.text


def deleteBoard():
    global userID
    print "Enter Board Name to be deleted ::"
    boardName = raw_input('boardName')
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    url = "http://" + host + "/users/%d/boards/%s/" % (userID, boardName)
    r = requests.delete(url, headers=headers)
    print r.status_code
    print r.text


def updateBoard():
    global userID
    print "Enter Board Name to be updated ::"
    boardName = raw_input('boardName')
    boardName1 = None
    boardDesc = None
    category = None
    isPrivate = None
    while True:
        var = raw_input("Enter fields to be updated :: 1.boardName 2.boardDesc 3.category 4.isPrivate 5.DoneEditing")
        if var == "1":
            boardName1 = raw_input('boardName')
        if var == "2":
            boardDesc = raw_input('boardDesc')
        if var == "3":
            category = raw_input('category')
        if var == "4":
            isPrivate = raw_input('isPrivate')
        if var == "5":
            break
    data1 = {"boardName": boardName1, "boardDesc": boardDesc, "category": category, "isPrivate": isPrivate}
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    url = "http://" + host + "/users/%d/boards/%s/" % (userID, boardName)
    r = requests.put(url, data=json.dumps(data1), headers=headers)
    print r.status_code
    print r.text


def createPins():
    global userID
    #Choose Image from this List of Images
    images = { '1' :'clothes1.jpg','2' :'clothes2.jpg','3' :'clothes3.jpg','4' :'clothes4.jpg',
               '5': 'decor1.jpg','6': 'decor1.jpg','7': 'decor1.jpg','8': 'decor1.jpg',
               '9': 'food1.jpg','10': 'food1.jpg','11': 'food1.jpg','12': 'food1.jpg'
              }
    print json.dumps(images,indent=1)
    pinImage = raw_input ("choose Which image to upload") 
    pinName = raw_input('pinName')
    boardName = raw_input('boardName')
    pinDesc = raw_input('pinDesc')

    #Storing the Image on the Server
    url = "http://" + host + "/image/"  
    current_dir = os.path.dirname(os.path.realpath(__file__)) + '/client-images/'
    files = { 'file': open(current_dir+images[pinImage], 'rb') }
    r = requests.post(url, files=files) 
    r = json.loads(r.text)

    #Storing Image Info on the Server
    data1 = {"pinName": pinName, "pinImage": r["fileName"], "pinDesc": pinDesc}
    url = "http://" + host + "/users/%d/boards/%s/pins/" % (userID, boardName)
    print url
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}

    r = requests.post(url, data=json.dumps(data1), headers=headers)
    print r.status_code
    print r.text

def getPins():
    global userID
    boardName = raw_input('boardName')
    url = "http://" + host + "/users/%d/boards/%s/pins/" % (userID, boardName)
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    r = requests.get(url, headers=headers)
    print r.status_code
    print r.text

def getSinglePin():
    global userID
    print "Enter Pin to be returned ::"
    boardName = raw_input('boardName')
    pin_Id = int(raw_input('pin_Id'))
    url = "http://" + host + "/users/%d/boards/%s/pins/%d/" % (userID, boardName, pin_Id)
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    r = requests.get(url, headers=headers)
    print r.status_code
    print r.text


def deletePins():
    global userID
    print "Enter Pin to be deleted ::"
    boardName = raw_input('boardName')
    pin_Id = int(raw_input('pin_Id'))
    url = "http://" + host + "/users/%d/boards/%s/pins/%d/" % (userID, boardName, pin_Id)
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    r = requests.delete(url, headers=headers)
    print r.status_code
    print r.text


def updatePins():
    global userID
    print "Enter Pin to be updated ::"
    boardName = raw_input('boardName')
    pin_Id = int(raw_input('pin_Id'))
    pin_Id1 = None
    pinName = None
    pinImage = None
    pinDesc = None
    while True:
        varp = raw_input("Enter fields to be updated :: 1.pin_Id 2.pinName 3.pinImage 4.pinDesc 5.Done Editing")
        if varp == "1":
            pin_Id1 = int(raw_input('pin_Id'))
        if varp == "2":
            pinName = raw_input('pinName')
        if varp == "3":
            pinImage = int(raw_input('pinImage'))
        if varp == "4":
            pinDesc = raw_input('pinDesc')
        if varp == "5":
            break
    data1 = {"pin_Id": pin_Id1, "pinName": pinName, "pinImage": pinImage, "pinDesc": pinDesc}
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    url = "http://" + host + "/users/%d/boards/%s/pins/%d/" % (userID, boardName, pin_Id)
    r = requests.put(url, data=json.dumps(data1), headers=headers)
    print r.status_code
    print r.text


def updateComment():
    global userID
    print "Enter Comment to be updated ::"
    boardName = raw_input('boardName')
    pin_Id = int(raw_input('pin_Id'))
    comment_Id1 = None
    pinComment = None
    while True:
        varc = raw_input("Update fields:: 1.comment_Id 2.pinComment 3.Done Editing")
        if varc == "1":
            comment_Id1 = int(raw_input('comment_Id'))
        if varc == "2":
            pinComment = raw_input('pinComment')
        if varc == "3":
            break
    data1 = {"comment_Id": comment_Id1, "pinComment": pinComment}
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    url = "http://" + host + "/users/%d/boards/%s/pins/%d/comments/%d/" % (userID, boardName, pin_Id, comment_Id1)
    r = requests.put(url, data=json.dumps(data1), headers=headers)
    print r.status_code
    print r.text


def getSingleComment():
    global userID
    print "Enter Comment to be returned ::"
    boardName = raw_input('boardName')
    pin_Id = int(raw_input('pin_Id'))
    comment_Id = raw_input('comment_Id')
    url = "http://" + host + "/users/%d/boards/%s/pins/%d/comments/%d/" % (userID, boardName, pin_Id, comment_Id)
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    r = requests.get(url, headers=headers)
    print r.status_code
    print r.text


def deleteComment():
    global userID
    print "Enter Comment to be deleted ::"
    boardName = raw_input('boardName')
    pin_Id = int(raw_input('pin_Id'))
    comment_Id = int(raw_input('comment_Id'))
    url = "http://" + host + "/users/%d/boards/%s/pins/%d/comments/%d/" % (userID, boardName, pin_Id, comment_Id)
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    r = requests.delete(url, headers=headers)
    print r.status_code
    print r.text


def getComment():
    global userID
    boardName = raw_input('boardName')
    pin_Id = int(raw_input('pin_Id'))
    url = "http://" + host + "/users/%d/boards/%s/pins/%d/comments/" % (userID, boardName, pin_Id)
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    r = requests.get(url, headers=headers)
    print r.status_code
    print r.text


def createComment():
    global userID
    boardName = raw_input('boardName')
    pin_Id = int(raw_input('pin_Id'))
    pinComment = raw_input("pinComment")
    data1 = {"pinComment": pinComment}
    url = "http://" + host + "/users/%d/boards/%s/pins/%d/comments/" % (userID, boardName, pin_Id)
    headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
    r = requests.post(url, data=json.dumps(data1), headers=headers)
    print r.status_code
    print r.text


def get_items(json_data, key, data_list):  #Function to parse json
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

def viewAllPublicBoards():
    url = "http://127.0.0.1:5000/users/%s/public" %userID
    headers = {'Content-type':'application/json', 'Accept':'text/json'}
    r = requests.get(url, headers = headers)
    print r.status_code
    print r.text

def start_boards():
    while True:
        option = raw_input("Enter an option 1.CreateBoards 2.getBoards 3.getSingleBoard 4.DeleteBoards 5.UpdateBoards  6.View All Public Boards by other Users 7.Exit")
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
            viewAllPublicBoards()
        if option == '7':
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
    host = "127.0.0.1:5000"
    #host = raw_input("The host id: ")
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
