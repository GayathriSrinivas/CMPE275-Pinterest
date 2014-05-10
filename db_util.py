from flask import Flask
from couchdb.client import Server
import couchdb 
import json


app = Flask(__name__)

def init_couchdb():
	server = Server()
	try:
	    db = server.create('pinterest')
	except Exception:
	    db = server['pinterest']
	return db

def init_boards():
	server = Server()
	try:
	    db = server.create('boards')
	except Exception:
	    db = server['boards']
	return db


def user_signup(User):
    print "User Signup"
    emailId = User['email']
    db = init_couchdb()
    for docid in  db :
        user = db.get(docid)
        if(user['email'] == emailId):
            print "User already Registered. Please proceed to SignIn"
            return user['user_id']

    print "New User"
    User.store(db)
    return User['user_id']

def user_signin(email,pwd):
    print "User_Sign_in"
    db = init_couchdb()
    for docid in db:
        user = db.get(docid)
        if ( user['email'] == email and user['password'] == pwd ):
            return user['user_id']
    return "Email & Password don't match"


def create_board(user_id,boardName,boardDesc,category,isPrivate):
	print "Create Board"
	db = init_boards()
	doc = {'boardName':boardName , 'boardDesc':boardDesc, 'category':category , 'isPrivate':isPrivate , 'user_id':user_id}
	db.save(doc)
	for docid in  db :
		boards = db.get(docid)
		print boards;

def get_boards(user_id):
	print "Get List of all boards"
	list_boards = []
	db = init_boards()
	for docid in db:
		boards = db.get(docid)
		if(boards['user_id'] == user_id):
			list_boards.append(boards)
	return json.dumps(list_boards)
