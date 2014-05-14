from flask import Flask

from couchdb.client import Server
from couchdb.mapping import Document, IntegerField, TextField

#from flask import couchdb


app = Flask(__name__)
flag = True
image_path = "http://localhost:5000/static/images"


def init_boards():
    """

    :rtype : object
    """
    server = Server()
    try:
        db = server.create('boards')
    except Exception:
        db = server['boards']
    return db


rec = 0


class UserIdCount(Document):
    doc_type = TextField()
    count = IntegerField()


def autoIncrementUserId():
    db = init_boards()
    view_find_doc = '''
      function(doc) {
          if (doc.doc_type == "UserIdCount") {
            emit(doc.count, null);
          }
        }
    '''
    doc_id = db.query(view_find_doc).rows[0].id
    doc = db.get(doc_id)
    count = doc['count']
    doc['count'] = count + 1
    db.update([doc])
    return doc['count']


def autoIncrement():
    global rec
    pstrt = 1
    pint = 1
    if (rec == 0):
        rec = pstrt
    else:
        rec += pint
    return rec


def checkForFirstDoc():
    db = init_boards()
    view_find_doc = '''
      function(doc) {
          if (doc.doc_type == "UserIdCount") {
            emit(doc.count, null);
          }
        }
    '''
    print "before view is None"
    count_of_users = '''
        function (keys, values, rereduce) {
            return sum(values);
        }
        '''
    for row in db.query(view_find_doc, count_of_users):
        return row.value


#User Sign up
def user_signup(firstName, lastName, emailId, password):
    global flag
    print "User Signup"
    db = init_boards()
    doc_count = checkForFirstDoc()
    if (doc_count is None):
        if (flag == True):
            print "inside flag == true"
            id_count = UserIdCount(doc_type="UserIdCount", count=0)
            id_count.store(db)
            flag = False
    for docid in db:
        user = db.get(docid)
        if user.get('emailId', None) == emailId:
            print "User already Registered. Please proceed to SignIn"
            return user['user_id']
    print "New User"
    doc = {'firstName': firstName, 'lastName': lastName, 'emailId': emailId, 'password': password,
           'user_id': autoIncrementUserId(), 'boards': []}
    db.save(doc)
    return doc['user_id']


#User Sign in
def user_signin(emailId, password):
    print "User_Sign_in"
    db = init_boards()
    for docid in db:
        user = db.get(docid)
        if user.get('emailId', None) == emailId and user.get('password', None) == password:
            return user['user_id']
    return "Email & Password don't match"


def get_doc_for_user_id(user_id):
    db = init_boards()
    viewMapFunction = '''
        function(doc) {
          if (doc.user_id == ''' + str(user_id) + ''') {
            emit(doc.user_id, null);
          }
        }
    '''
    doc_id = db.query(viewMapFunction).rows[0].id
    doc = db.get(doc_id)
    return doc


def get_all_boards(user_id):
    db = init_boards()
    list_doc = []
    viewMapFunction = '''
        function(doc) {
            if (doc.user_id != ''' + str(user_id) + ''' && doc.boards.length != 0) {
                for( var i=0, l=doc.boards.length; i<l; i++) {
                    if(doc.boards[i].isPrivate != "True" && doc.boards[i].isPrivate != "true") {
                        emit(doc.emailId,doc.boards[i]);
                    }
                }
            }
        }
    '''
    for row in db.query(viewMapFunction):
        list_doc.append(row.value)
        list_doc[-1]['emailId'] = row.key
        for pin in list_doc[-1].get('pins', []):
            pin['pinImage'] = '%s/%s' % (image_path, pin['pinImage'])
    return list_doc


def create_board(user_id, boardName, boardDesc, category, isPrivate):
    print "Create Board"
    db = init_boards()
    # Need to find document of given user - use View to find document ID for corresponding user
    doc = get_doc_for_user_id(user_id)
    board = {'boardName': boardName, 'boardDesc': boardDesc, 'category': category, 'isPrivate': isPrivate, 'pins': []}
    doc['boards'].append(board)
    db.update([doc])
    return board


def get_boards(user_id):
    print "Get List of all boards"
    list_boards = get_doc_for_user_id(user_id)['boards']
    for board in list_boards:
        for pin in board.get('pins', []):
            pin['pinImage'] = '%s/%s' % (image_path, pin['pinImage'])
    return list_boards


def get_aboard(user_id, boardName):
    print "Get a board"
    list_b = get_boards(user_id)
    for x in list_b:
        if x['boardName'] == boardName:
            return x
    return 0


def update_board(user_id, boardName, boardName1, boardDesc, category, isPrivate):
    print "Update a Board"
    temp = []
    db = init_boards()
    doc = get_doc_for_user_id(user_id)
    list_ub = doc['boards']
    print "list_ub", list_ub,
    for ind, x in enumerate(list_ub):
        if x['boardName'] == boardName:
            temp = x
            if boardName1 is not None:
                temp['boardName'] = boardName1
            if boardDesc is not None:
                temp['boardDesc'] = boardDesc
            if category is not None:
                temp['category'] = category
            if isPrivate is not None:
                temp['isPrivate'] = isPrivate
            list_ub[ind] = temp
    db.update([doc])
    return temp


def delete_board(user_id, boardName):
    print "Delete a Board"
    db = init_boards()
    # Need to find document of given user - use View to find document ID for corresponding user
    doc = get_doc_for_user_id(user_id)
    list_up = doc['boards']
    new_list = [x for x in list_up if not x['boardName'] == boardName]
    doc['boards'] = new_list
    db.update([doc])
    return


def create_pin(user_id, boardName, pinName, pinImage, pinDesc):
    print "Create Pin"
    db = init_boards()
    # Need to find document of given user - use View to find document ID for corresponding user
    doc = get_doc_for_user_id(user_id)
    pin = {'pin_Id': autoIncrement(), 'pinName': pinName, 'pinImage': pinImage, 'pinDesc': pinDesc, 'comments': []}
    list_up = doc['boards']
    for x in list_up:
        if x['boardName'] == boardName:
            x['pins'].append(pin)
    db.update([doc])
    pin['pinImage'] = '%s/%s' % (image_path, pin['pinImage'])
    return pin


def get_pins(user_id, boardName):
    list_pins = []
    print "Get List of all pins"
    list_boards = get_doc_for_user_id(user_id)['boards']
    for x in list_boards:
        if x['boardName'] == boardName:
            list_pins = x['pins']
    for pin in list_pins:
        pin['pinImage'] = "%s/%s" % (image_path, pin['pinImage'])
    return list_pins


def get_apin(user_id, boardName, pin_Id):
    print "Get a pin"
    list_p = get_pins(user_id, boardName)
    for x in list_p:
        if x['pin_Id'] == pin_Id:
            x['pinImage'] = '%s/%s' % (image_path, x['pinImage'])
            return x
    return 0


def update_pin(user_id, boardName, pin_Id, pinName, pinImage, pinDesc):
    print "Update a pin"
    temp = []
    db = init_boards()
    doc = get_doc_for_user_id(user_id)
    list_b = doc['boards']
    for x in list_b:
        if x['boardName'] == boardName:
            list_up = x['pins']
            for ind, y in enumerate(list_up):
                if y['pin_Id'] == pin_Id:
                    temp = y
                    if pinName is not None:
                        temp['pinName'] = pinName
                    if pinImage is not None:
                        temp['pinImage'] = pinImage
                    if pinDesc is not None:
                        temp['pinDesc'] = pinDesc
                    list_up[ind] = temp
    db.update([doc])
    temp['pinImage'] = '%s/%s' % (image_path, temp['pinImage'])
    return temp


def delete_pin(user_id, boardName, pin_Id):
    print "Delete a Pin"
    db = init_boards()
    doc = get_doc_for_user_id(user_id)
    list_b = doc['boards']
    for x in list_b:
        if x['boardName'] == boardName:
            # print "$$$$$$$$$$$$$$$$$$$$$$"
            # print x
            # print "$$$$$$$$$$$$$$$$$$$$$$"
            list_upd = x['pins']
        new_list = [y for y in list_upd if not y['pin_Id'] == pin_Id]
        x['pins'] = new_list
    db.update([doc])
    return


def create_comment(user_id, boardName, pin_Id, pinComment):
    print "Create Comment"
    db = init_boards()
    # Need to find document of given user - use View to find document ID for corresponding user
    doc = get_doc_for_user_id(user_id)
    comment = {'comment_Id': autoIncrement(), 'pinComment': pinComment}
    list_boards = doc['boards']
    for x in list_boards:
        if x['boardName'] == boardName:
            list_upd = x['pins']
            for y in list_upd:
                if y['pin_Id'] == pin_Id:
                    y['comments'].append(comment)
    db.update([doc])
    return comment


def get_comments(user_id, boardName, pin_Id):
    list_comments = []
    print "Get List of all comments for a Pin"
    list_boards = get_doc_for_user_id(user_id)['boards']
    for x in list_boards:
        if x['boardName'] == boardName:
            list_pins = x['pins']
            for y in list_pins:
                if y['pin_Id'] == pin_Id:
                    list_comments = y['comments']
    return list_comments


def get_acomment(user_id, boardName, pin_Id, comment_Id):
    print "Get a comment by id %d" % comment_Id
    list_c = get_comments(user_id, boardName, pin_Id)
    for x in list_c:
        if x['comment_Id'] == comment_Id:
            return x
    return 0


def update_comment(user_id, boardName, pin_Id, comment_Id, pinComment):
    print "Update a comment"
    temp = []
    db = init_boards()
    doc = get_doc_for_user_id(user_id)
    list_b = doc['boards']
    for x in list_b:
        if x['boardName'] == boardName:
            list_p = x['pins']
            for y in list_p:
                if y['pin_Id'] == pin_Id:
                    list_com = y['comments']
                    for ind, z in enumerate(list_com):
                        if z['comment_Id'] == comment_Id:
                            temp = z
                            if pinComment is not None:
                                temp['pinComment'] = pinComment
                            list_com[ind] = temp
    db.update([doc])
    # print "----------------------"
    # print temp
    # print "----------------------"
    return temp


def delete_comment(user_id, boardName, pin_Id, comment_Id):
    print "Delete a Comment"
    db = init_boards()
    doc = get_doc_for_user_id(user_id)
    list_b = doc['boards']
    for x in list_b:
        if x['boardName'] == boardName:
            list_p = x['pins']
            for y in list_p:
                if y['pin_Id'] == pin_Id:
                    list_comm = y['comments']
                new_list = [z for z in list_comm if not z['comment_Id'] == comment_Id]
                y['comments'] = new_list
    db.update([doc])
    return


