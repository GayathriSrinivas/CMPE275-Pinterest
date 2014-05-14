from flask import Flask
from flask import request
from flask import Response
from flask import abort
import json
from werkzeug import secure_filename

import db_util


app = Flask(__name__)

#Main Page
@app.route('/')
def welcome_page():
    return "Welcome to Pinterest !!!"


@app.route('/image/', methods=['POST'])
def image():
    f = request.files['file']
    #Save on Disk
    f.save('static/images/' + secure_filename(f.filename))
    return Response(json.dumps({"fileName": f.filename}), status=201, mimetype='application/json')


#Database to Enter Details
@app.route("/users/signUp/", methods=['POST'])
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
    if user_id != "0":
        links = [
            {'url': '/users/login/', 'method': 'POST'}
        ]
        js = {'Links': links, 'UserID': user_id}
        resp = Response(json.dumps(js, indent=2), status=201, mimetype='application/json')
        return resp


@app.route('/users/login/', methods=['POST'])
def login():
    user_logdetails = request.get_json()
    emailId = user_logdetails.get('emailId')
    password = user_logdetails.get('password')
    mess = db_util.user_signin(emailId, password)
    if mess != "Email & Password don't match":
        links = [
            {'url': '/users/%s/boards/' % mess, 'method': 'GET'},
            {'url': '/users/%s/boards/' % mess, 'method': 'POST'},
        ]
        js = {'Links': links, 'UserID': mess}
        resp = Response(json.dumps(js, indent=2), status=201, mimetype='application/json')
        return resp
    else:
        js = {'error message': "Email & Password don't match"}
        resp = Response(json.dumps(js, indent=2), status=400, mimetype='application/json')
        return resp


#Create Boards(POST) or List all Boards(GET)
@app.route('/users/<int:user_id>/boards/', methods=['POST', 'GET'])
def boards(user_id):
    print 'User Id %d' % user_id
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
            {'url': '/users/%d/boards/%s/' % (user_id, boardName), 'method': 'GET'},
            {'url': '/users/%d/boards/%s/' % (user_id, boardName), 'method': 'PUT'},
            {'url': '/users/%d/boards/%s/' % (user_id, boardName), 'method': 'DELETE'},
            {'url': '/users/%d/boards/%s/pins/' % (user_id, boardName), 'method': 'POST'}
        ]
        js = {'Boards': sboards, 'Links': links}
        resp = Response(json.dumps(js, indent=2), status=201, mimetype='application/json')
        return resp


#GET a single Board
@app.route('/users/<int:user_id>/boards/<string:boardName>/', methods=['GET'])
def asboard(user_id, boardName):
    print 'Board Name %s' % boardName
    asboard = db_util.get_aboard(user_id, boardName)

    if asboard == 0:
        abort(404)

    # Return List of Allowed Operations
    links = [
        {'url': '/users/%d/boards/%s/' % (user_id, boardName), 'method': 'PUT'},
        {'url': '/users/%d/boards/%s/' % (user_id, boardName), 'method': 'DELETE'},
        {'url': '/users/%d/boards/%s/pins/' % (user_id, boardName), 'method': 'POST'}
    ]
    js = {'Board': asboard, 'Links': links}
    resp = Response(json.dumps(js, indent=2), status=200, mimetype='application/json')
    return resp


#Update or Delete Board
@app.route('/users/<int:user_id>/boards/<string:boardName>/', methods=['PUT', 'DELETE'])
def updateBoard(user_id, boardName):
    if request.method == "PUT":
        print "PUT Request"
        board_details = request.get_json()
        boardName1 = board_details.get('boardName', None)
        boardDesc = board_details.get('boardDesc', None)
        category = board_details.get('category', None)
        isPrivate = board_details.get('isPrivate', None)
        sboards = db_util.update_board(user_id, boardName, boardName1, boardDesc, category, isPrivate)
        # Return List of Allowed Operations
        links = [
            {'url': '/users/%d/boards/%s/' % (user_id, sboards['boardName']), 'method': 'GET'},
            {'url': '/users/%d/boards/%s/' % (user_id, sboards['boardName']), 'method': 'DELETE'},
            {'url': '/users/%d/boards/%s/pins/' % (user_id, sboards['boardName']), 'method': 'POST'}
        ]
        js = {'User': user_id, 'Board': sboards, 'Links': links}
        resp = Response(json.dumps(js, indent=3), status=200, mimetype='application/json')
        return resp
    else:
        print "DELETE Request"
        db_util.delete_board(user_id, boardName)
        # Return List of Allowed Operations
        links = {'Links': [
            {'url': '/users/%d/boards/' % user_id, 'method': 'POST'}
        ]}
        resp = Response(json.dumps(links), status=200, mimetype='application/json')
        return resp


#Create Pins (POST) or List all Pins(GET)
@app.route('/users/<int:user_id>/boards/<string:boardName>/pins/', methods=['GET', 'POST'])
def pins(user_id, boardName):
    print 'Board name is: %s' % boardName
    if request.method == "GET":
        print "GET Request"
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
            {'url': '/users/%d/boards/%s/pins/%d/' % (user_id, boardName, int(spins['pin_Id'])), 'method': 'GET'},
            {'url': '/users/%d/boards/%s/pins/%d/' % (user_id, boardName, int(spins['pin_Id'])), 'method': 'PUT'},
            {'url': '/users/%d/boards/%s/pins/%d/' % (user_id, boardName, int(spins['pin_Id'])), 'method': 'DELETE'}
        ]
        js = {'User': user_id, 'Board': boardName, 'Created Pin': spins, 'Links': links}
        resp = Response(json.dumps(js, indent=4), status=201, mimetype='application/json')
        return resp


#GET a single Pin
@app.route('/users/<int:user_id>/boards/<string:boardName>/pins/<int:pin_Id>/', methods=['GET'])
def apin(user_id, boardName, pin_Id):
    print "Pin id is: %d" % pin_Id
    aspin = db_util.get_apin(user_id, boardName, pin_Id)

    if aspin == 0:
        abort(404)

    # Return List of Allowed Operations
    links = [
        {'url': '/users/%d/boards/%s/pins/%d/' % (user_id, boardName, pin_Id), 'method': 'PUT'},
        {'url': '/users/%d/boards/%s/pins/%d/' % (user_id, boardName, pin_Id), 'method': 'DELETE'},
        {'url': '/users/%d/boards/%s/pins/%d/comments/' % (user_id, boardName, pin_Id), 'method': 'POST'}
    ]
    js = {'User': user_id, 'Board': boardName, 'Links': links, 'Pin': aspin}
    resp = Response(json.dumps(js, indent=4), status=200, mimetype='application/json')
    return resp


#Update or Delete Pins
@app.route('/users/<int:user_id>/boards/<string:boardName>/pins/<int:pin_Id>/', methods=['PUT', 'DELETE'])
def updatePin(user_id, boardName, pin_Id):
    if request.method == "PUT":
        print "PUT Request"
        pint_details = request.get_json()
        pinName = pint_details.get('pinName', None)
        pinImage = pint_details.get('pinImage', None)
        pinDesc = pint_details.get('pinDesc', None)
        upins = db_util.update_pin(user_id, boardName, pin_Id, pinName, pinImage, pinDesc)
        # Return List of Allowed Operations
        links = [
            {'url': '/users/%d/boards/%s/pins/%d/' % (user_id, boardName, pin_Id), 'method': 'GET'},
            {'url': '/users/%d/boards/%s/pins/%d/' % (user_id, boardName, pin_Id), 'method': 'DELETE'},
            {'url': '/users/%d/boards/%s/pins/%d/comments/' % (user_id, boardName, pin_Id), 'method': 'POST'}
        ]
        js = {'User': user_id, 'Board': boardName, 'Pins': upins, 'Links': links}
        resp = Response(json.dumps(js, indent=4), status=200, mimetype='application/json')
        return resp
    else:
        print "DELETE Request"
        db_util.delete_pin(user_id, boardName, pin_Id)
        #Return List of Allowed Operations
        links = {'Links': [
            {'url': '/users/%d/boards/%s/pins/' % (user_id, boardName), 'method': 'POST'}
        ]}
        resp = Response(json.dumps(links), status=200, mimetype='application/json')
        return resp


#Create Comments (POST) or List all Comments(GET)
@app.route('/users/<int:user_id>/boards/<string:boardName>/pins/<int:pin_Id>/comments/', methods=['GET', 'POST'])
def comments(user_id, boardName, pin_Id):
    print 'Pin Name is: %s' % pin_Id
    if request.method == "GET":
        print "GET Request"
        data = {'User': user_id, 'Board': boardName, 'Pins': pin_Id, 'Comments': db_util.get_comments(user_id, boardName, pin_Id)}
        resp = Response(json.dumps(data, indent=4), status=200, mimetype='application/json')
        return resp
    else:
        comment_details = request.get_json()
        pinComment = comment_details.get('pinComment')
        comm = db_util.create_comment(user_id, boardName, pin_Id, pinComment)
        # Return List of Allowed Operations
        links = {'Links': [
            {'url': '/users/%d/boards/%s/pins/%d/comments/%d/' % (user_id, boardName, pin_Id, int(comm['comment_Id'])),
             'method': 'GET'},
            {'url': '/users/%d/boards/%s/pins/%d/comments/%d/' % (user_id, boardName, pin_Id, int(comm['comment_Id'])),
             'method': 'PUT'},
            {'url': '/users/%d/boards/%s/pins/%d/comments/%d/' % (user_id, boardName, pin_Id, int(comm['comment_Id'])),
             'method': 'DELETE'}
        ]}
        js = {'User': user_id, 'Board': boardName, 'Pins': pin_Id, 'Created Comment': comm, 'Links': links}
        resp = Response(json.dumps(js, indent=5), status=201, mimetype='application/json')
        return resp


#GET a single Comment
@app.route('/users/<int:user_id>/boards/<string:boardName>/pins/<int:pin_Id>/comments/<int:comment_Id>/', methods=['GET'])
def acomment(user_id, boardName, pin_Id, comment_Id):
    print "Comment id is: %d" % comment_Id
    ascomm = db_util.get_acomment(user_id, boardName, pin_Id, comment_Id)

    if ascomm == 0:
        abort(404)

    # Return List of Allowed Operations
    links = [
        {'url': '/users/%d/boards/%s/pins/%d/comments/%d' % (user_id, boardName, pin_Id, comment_Id),
         'method': 'PUT'},
        {'url': '/users/%d/boards/%s/pins/%d/comments/%d' % (user_id, boardName, pin_Id, comment_Id),
         'method': 'DELETE'},
        {'url': '/users/%d/boards/%s/pins/%d/comments/' % (user_id, boardName, pin_Id), 'method': 'POST'}
    ]
    js = {'User': user_id, 'Board': boardName, 'Pin': pin_Id, 'Comment': ascomm, 'Links': links}
    resp = Response(json.dumps(js, indent=5), status=200, mimetype='application/json')
    return resp


#Update or Delete Comments
@app.route('/users/<int:user_id>/boards/<string:boardName>/pins/<int:pin_Id>/comments/<int:comment_Id>/', methods=['PUT', 'DELETE'])
def updateComment(user_id, boardName, pin_Id, comment_Id):
    if request.method == "PUT":
        print 'PUT Request'
        comment_details = request.get_json()
        pinComment = comment_details.get('pinComment', None)
        cpins = db_util.update_comment(user_id, boardName, pin_Id, comment_Id, pinComment)
        # print "###################################################"
        # print cpins
        # print "###################################################"
        # Return List of Allowed Operations
        links = [
            {'url': '/users/%d/boards/%s/pins/%d/comments/%d/' % (user_id, boardName, pin_Id, comment_Id),
             'method': 'GET'},
            {'url': '/users/%d/boards/%s/pins/%d/comments/%d/' % (user_id, boardName, pin_Id, comment_Id),
             'method': 'DELETE'},
            {'url': '/users/%d/boards/%s/pins/%d/comments/' % (user_id, boardName, pin_Id), 'method': 'POST'}
        ]
        js = {'User': user_id, 'Board': boardName, 'Pin': pin_Id, 'Comments': cpins, 'Links': links}
        resp = Response(json.dumps(js, indent=5), status=200, mimetype='application/json')
        return resp
    else:
        print 'DELETE Request'
        db_util.delete_comment(user_id, boardName, pin_Id, comment_Id)
        #Return List of Allowed Operations
        links = {'Links': [
            {'url': '/users/%d/boards/%s/pins/%d/comments/' % (user_id, boardName, pin_Id), 'method': 'POST'}
        ]}
        resp = Response(json.dumps(links), status=200, mimetype='application/json')
        return resp


#Get all the public boards of all the other users
@app.route('/users/<int:user_id>/public/')
def all_boards(user_id):
    data = {'Boards': db_util.get_all_boards(user_id)}
    resp = Response(json.dumps(data, indent=len(data)), status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
