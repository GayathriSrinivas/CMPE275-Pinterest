#!/bin/bash
# 
#Test all functionalities 
#


#Login for user
echo "Login for user"
echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST -d '{"emailId":"deo.priyanka02@gmail.com", "password":"frfe"}' http://127.0.0.1:5000/users/login/
echo -e "\n"

#Test create boards
echo"Test create boards "
echo -e "\n"
echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST -d '{"boardName":"Food","boardDesc":"Amazing Food","Indian category": "Food","isPrivate": "false"}' http://127.0.0.1:5000/users/2/boards/

echo -e "\n"
echo "Upload images to server"
curl -F "file=@client-images/food1.jpg" http://127.0.0.1:5000/image/

#Test create a pin on board just created
echo -e "\n"
echo "Test create a pin on board just created"
curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Food", "pinImage": "food1.jpg","pinDesc": "Amazing Food"}' http://127.0.0.1:5000/users/2/boards/Food/pins/
echo -e "\n"



#Test create a comment on a pin on board just created
echo -e "\n"
echo "Test create a comment on a pin on board just created"
curl -i -H "Content-Type: application/json" -X POST -d '{"pinComment": "Very cool"}' http://127.0.0.1:5000/users/2/boards/Food/pins/1/comments/
echo -e "\n"

#get all comments
echo -e "\n"
echo "get all comments "
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/2/boards/Food/pins/
echo -e "\n"


#update a comment
echo -e "\n"
echo "update a comment"
curl -i -H "Content-Type: application/json" -X PUT -d '{"comment_Id": "2", "pinComment": "Very very cool"}' http://127.0.0.1:5000/users/2/boards/Food/pins/1/comments/2/ 
echo -e "\n"

#get all pins and their comments 
echo -e "\n"
echo "get all pins and comments "
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/2/boards/Food/pins/
echo -e "\n"

#delete a comment
echo -e "\n"
echo "delete a comment"
curl -i -H "Content-Type: application/json" -X DELETE http://127.0.0.1:5000/users/2/boards/Food/pins/2/
echo -e "\n"


#get all pins and comments
echo -e "\n"
echo "get all pins "
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/2/boards/Food/pins/
echo -e "\n"

