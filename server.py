from flask import Flask
from flask import request
from flask import Response
from flask import abort
import json
import db_util

app = Flask(__name__)

#Main Page
@app.route('/')
def welcome_page():
    return "Welcome to Pinterest !!!"


#Database to Enter Detais
@app.route("/user/signUp", methods=['POST'])
def user_signup():
    user_details = request.get_json()
    firstName = user_details.get('firstName')
    lastName = user_details.get('lastName')
    emailId = user_details.get('emailId')
    password = user_details.get('password')
    print "User Signup"
    user_id = db_util.user_signup(firstName, lastName, emailId, password)
    print user_id

    #return user_id
    if (user_id != "0"):
        links = [
            {'url': '/user/login', 'method': 'POST'}
        ]
        js = {'Links': links, 'UserID': user_id}
        resp = Response(json.dumps(js, indent=2), status=201, mimetype='application/json')
        resp.headers['Link'] = 'http://127.0.0.1:5000'
        return resp


@app.route('/user/login', methods=['POST'])
def login():
    user_logdetails = request.get_json()
    emailId = user_logdetails.get('emailId')
    password = user_logdetails.get('password')
    mess = db_util.user_signin(emailId, password)
    if mess != "Email & Password don't match":
        links = [
            {'url': '/user/{user_id}/boards', 'method': 'GET'},
            {'url': '/user/{user_id}/boards', 'method': 'POST'},
        ]
        js = {'Links': links, 'UserID': mess}
        resp = Response(json.dumps(js, indent=2), status=201, mimetype='application/json')
        resp.headers['Link'] = 'http://127.0.0.1:5000'
        return resp
    else:
        js = {'error message': "Email & Password don't match"}
        resp = Response(json.dumps(js, indent=2), status=400, mimetype='application/json')
        resp.headers['Link'] = 'http://127.0.0.1:5000'
        return resp


#Create Boards(POST) or List all Boards(GET)
@app.route('/user/<int:user_id>/boards/', methods=['POST', 'GET'])
def boards(user_id):
    print
    'User Id %d' % user_id
    if request.method == "GET":
        print
        "GET Request"
        data = {'User': user_id, 'Boards': db_util.get_boards(user_id)}
        resp = Response(json.dumps(data, indent=2), status=200, mimetype='application/json')
        return resp
    else:
        board_details = request.get_json()
        boardName = board_details.get('boardName')
        boardDesc = board_details.get('boardDesc')
        category = board_details.get('category')
        isPrivate = board_details.get('isPrivate', 'False')
        sboards = db_util.create_board(user_id, boardName, boardDesc, category, isPrivate)

        # Return List of Allowed Operations
        links = [
            {'url': '/users/{UserId}/boards/{boardName}', 'method': 'GET'},
            {'url': '/users/{UserId}/boards/{boardName}', 'method': 'PUT'},
            {'url': '/users/{UserId}/boards/{boardName}', 'method': 'DELETE'},
            {'url': '/users/{UserId}/boards/{boardName}/pins/', 'method': 'POST'}
        ]

        js = {'Links': links}
        resp = Response(json.dumps(js, indent = 2), status=201, mimetype='application/json')
        resp.headers['Link'] = 'http://127.0.0.1:5000'
        #return "201 User Login Successful !! "
        return resp


#GET a single Board
@app.route('/user/<int:user_id>/boards/<string:boardName>/', methods=['GET'])
def asboard(user_id, boardName):
    print
    'Board Name %s' % boardName
    asboard = db_util.get_aboard(user_id, boardName)

    if asboard == 0:
        abort(404)

    # Return List of Allowed Operations
    links = [
        {'url': '/users/{UserId}/boards/{boardName}', 'method': 'PUT'},
        {'url': '/users/{UserId}/boards/{boardName}', 'method': 'DELETE'},
        {'url': '/users/{UserId}/boards/{boardName}/pins/', 'method': 'POST'}
    ]
    js = {'Board': asboard, 'Links': links}
    resp = Response(json.dumps(js, indent=2), status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://127.0.0.1:5000'
    #print 'done'
    return resp


#Update or Delete Board
@app.route('/user/<int:user_id>/boards/<string:boardName>/', methods=['PUT', 'DELETE'])
def updateBoard(user_id, boardName):
    if request.method == "PUT":
        print "PUT Request"
        board_details = request.get_json()
        boardName1 = board_details.get('boardName',None)
        boardDesc = board_details.get('boardDesc',None)
        category = board_details.get('category',None)
        isPrivate = board_details.get('isPrivate', None)
        sboards = db_util.update_board(user_id, boardName,boardName1, boardDesc, category, isPrivate)
        # Return List of Allowed Operations
        links = [
            {'url': '/users/{UserId}/boards/{boardName}', 'method': 'GET'},
            {'url': '/users/{UserId}/boards/{boardName}', 'method': 'DELETE'},
            {'url': '/users/{UserId}/boards/{boardName}/pins/', 'method': 'POST'}
        ]
        js = {'Board': sboards, 'Links': links}
        resp = Response(json.dumps(js, indent=2), status=200, mimetype='application/json')
        resp.headers['Link'] = 'http://127.0.0.1:5000'
        return resp
    else:
        print
        "DELETE Request"
        db_util.delete_board(user_id, boardName)
        # Return List of Allowed Operations
        links = {'Links': [
            {'url': '/users/{UserId}/boards/', 'method': 'POST'}
        ]}
        resp = Response(json.dumps(links), status=200, mimetype='application/json')
        resp.headers['Link'] = 'http://127.0.0.1:5000'
        return resp


#Create Pins (POST) or List all Pins(GET)
@app.route('/user/<int:user_id>/boards/<string:boardName>/pins/', methods=['GET', 'POST'])
def pins(user_id, boardName):
    print
    'Board name is: %s' % boardName
    if request.method == "GET":
        print
        "GET Request"
        data = {'User': user_id, 'Board': boardName, 'Pins': db_util.get_pins(user_id, boardName)}
        resp = Response(json.dumps(data, indent=3), status=200, mimetype='application/json')
        return resp
    else:
        pint_details = request.get_json()
        pinName = pint_details.get('pinName')
        pinImage = pint_details.get('pinImage')
        pinDesc = pint_details.get('pinDesc')
        spins = db_util.create_pin(user_id, boardName, pinName, pinImage, pinDesc)
        # Return List of Allowed Operations
        links = [
            {'url': '/users/{UserId}/boards/{boardName}/pins/{pin_Id}', 'method': 'GET'},
            {'url': '/users/{UserId}/boards/{boardName}/pins/{pin_Id}', 'method': 'PUT'},
            {'url': '/users/{UserId}/boards/{boardName}/pins/{pin_Id}', 'method': 'DELETE'}
        ]

        js = {'Created Pin': spins, 'Links': links}
        resp = Response(json.dumps(js, indent=2), status=201, mimetype='application/json')
        resp.headers['Link'] = 'http://127.0.0.1:5000'
        return resp


#GET a single Pin
@app.route('/user/<int:user_id>/boards/<string:boardName>/pins/<int:pin_Id>/', methods=['GET'])
def apin(user_id, boardName, pin_Id):
    print "Pin id is: %d" % pin_Id
    aspin = db_util.get_apin(user_id, boardName, pin_Id)

    if aspin == 0:
        abort(404)

    # Return List of Allowed Operations
    links = [
        {'url': '/users/{UserId}/boards/{boardName}/pins/{pin_Id}', 'method': 'PUT'},
        {'url': '/users/{UserId}/boards/{boardName}/pins/{pin_Id}', 'method': 'DELETE'},
        {'url': '/users/{UserId}/boards/{boardName}/pins/{pin_Id}/comments/', 'method': 'POST'}
    ]

    js = {'Links': links, 'Pin': aspin}
    resp = Response(json.dumps(js, indent=2), status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://127.0.0.1:5000'
    #print 'done'
    return resp


#Update or Delete Pins
@app.route('/user/<int:user_id>/boards/<string:boardName>/pins/<int:pin_Id>/', methods=['PUT', 'DELETE'])
def updatePin(user_id, boardName, pin_Id):
    if request.method == "PUT":
        print
        "PUT Request"
        pint_details = request.get_json()
        pinName = pint_details.get('pinName')
        pinImage = pint_details.get('pinImage')
        pinDesc = pint_details.get('pinDesc')
        upins = db_util.update_pin(user_id, boardName, pin_Id, pinName, pinImage, pinDesc)
        # Return List of Allowed Operations
        links = [
            {'url': '/users/{UserId}/boards/{boardName}/pins/{pin_Id}', 'method': 'GET'},
            {'url': '/users/{UserId}/boards/{boardName}/pins/{pin_Id}', 'method': 'DELETE'},
            {'url': '/users/{UserId}/boards/{boardName}/pins/{pin_Id}/comments/', 'method': 'POST'}
        ]
        js = {'Pins': upins, 'Links': links}
        resp = Response(json.dumps(js, indent=2), status=200, mimetype='application/json')
        resp.headers['Link'] = 'http://127.0.0.1:5000'
        return resp
    else:
        print
        'DELETE Request'
        db_util.delete_pin(user_id, boardName, pin_Id)
        #Return List of Allowed Operations
        links = {'Links': [
            {'url': '/users/{UserId}/boards/{boardName}/pins/', 'method': 'POST'}
        ]}
        resp = Response(json.dumps(links), status=200, mimetype='application/json')
        resp.headers['Link'] = 'http://127.0.0.1:5000'
        return resp


#Create Comments (POST) or List all Comments(GET)
@app.route('/user/<int:user_id>/boards/<string:boardName>/pins/<string:pinName>/comments/', methods=['GET', 'POST'])
def comments(user_id, boardName, pinName):
    print
    'Pin Name is: %s' % pinName
    if request.method == "GET":
        print
        "GET Request"
        data = {'User': user_id, 'Board': boardName, 'Pins': pinName,
                'Comments': db_util.get_comments(user_id, boardName, pinName)}
        resp = Response(json.dumps(data, indent=4), status=200, mimetype='application/json')
        return resp
    else:
        comment_details = request.get_json()
        pinComment = comment_details.get('pinComment')
        comm = db_util.create_comment(user_id, boardName, pinName, pinComment)
        # Return List of Allowed Operations
        links = {'Links': [
            {'url': '/users/{UserId}/boards/{boardName}/pins/{pinName}/comments/{comment_id}', 'method': 'GET'},
            {'url': '/users/{UserId}/boards/{boardName}/pins/{pinName}/comments/{comment_id}', 'method': 'PUT'},
            {'url': '/users/{UserId}/boards/{boardName}/pins/{pinName}/comments/{comment_id}', 'method': 'DELETE'}
        ]}

        js = {'Created Comment': comm, 'Links': links}
        resp = Response(json.dumps(js, indent=2), status=201, mimetype='application/json')
        resp.headers['Link'] = 'http://127.0.0.1:5000'
        return resp


#GET a single Comment
@app.route('/user/<int:user_id>/boards/<string:boardName>/pins/<string:pinName>/comments/<int:comment_Id>/',
           methods=['GET'])
def acomment(user_id, boardName, pinName, comment_Id):
    print "Comment id is: %d" % comment_Id
    ascomm = db_util.get_acomment(user_id, boardName, pinName, comment_Id)

    if ascomm == 0:
        abort(404)

    # Return List of Allowed Operations
    links = [
        {'url': '/users/{UserId}/boards/{boardName}/pins/{pinName}/comments/{comment_id}', 'method': 'PUT'},
        {'url': '/users/{UserId}/boards/{boardName}/pins/{pinName}/comments/{comment_id}', 'method': 'DELETE'},
        {'url': '/users/{UserId}/boards/{boardName}/pins/{pinName}/comments/', 'method': 'POST'}
    ]

    js = {'User': user_id, 'Pin': pinName, 'Comment': ascomm, 'Links': links}
    resp = Response(json.dumps(js, indent=4), status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://127.0.0.1:5000'
    #print 'done'
    return resp


#Update or Delete Comments
@app.route('/user/<int:user_id>/boards/<string:boardName>/pins/<string:pinName>/comments/<int:comment_Id>/',
           methods=['PUT', 'DELETE'])
def updateComment(user_id, boardName, pinName, comment_Id):
    if request.method == "PUT":
        print
        "PUT Request"
        comment_details = request.get_json()
        pinComment = comment_details.get('pinComment')
        cpins = db_util.update_comment(user_id, boardName, pinName, comment_Id, pinComment)
        # Return List of Allowed Operations
        links = [
            {'url': '/users/{UserId}/boards/{boardName}/pins/{pinName}/comments/{comment_id}', 'method': 'GET'},
            {'url': '/users/{UserId}/boards/{boardName}/pins/{pinName}/comments/{comment_id}', 'method': 'DELETE'},
            {'url': '/users/{UserId}/boards/{boardName}/pins/{pinName}/comments/', 'method': 'POST'}
        ]
        js = {'User': user_id, 'Pin': pinName, 'Comments': cpins, 'Links': links}
        resp = Response(json.dumps(js, indent=4), status=200, mimetype='application/json')
        resp.headers['Link'] = 'http://127.0.0.1:5000'
        return resp
    else:
        print
        'DELETE Request'
        db_util.delete_comment(user_id, boardName, pinName, comment_Id)
        #Return List of Allowed Operations
        links = {'Links': [
            {'url': '/users/{UserId}/boards/{boardName}/pins/{pinName}/comments/', 'method': 'POST'}
        ]}
        resp = Response(json.dumps(links), status=200, mimetype='application/json')
        resp.headers['Link'] = 'http://127.0.0.1:5000'
        return resp


if __name__ == '__main__':
    app.run(debug=True)