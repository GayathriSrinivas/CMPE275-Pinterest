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
curl -i -H "Content-Type: application/json" -X POST -d '{"boardName":"Decor","boardDesc":"Beautiful Decor","category": "Home Decor","isPrivate": "True"}' http://127.0.0.1:5000/users/2/boards/
curl -i -H "Content-Type: application/json" -X POST -d '{"boardName":"Clothes","boardDesc":"Very Pretty Collection","category": "Summer Wear","isPrivate": "false"}' http://127.0.0.1:5000/users/2/boards/
echo -e "\n"

#get created boards 
echo -e "\n"
echo "get created boards "
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/2/boards/Food/
echo -e "\n"


#get all public boards 
echo -e "\n"
echo "get all public boards "
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/2/public/
echo -e "\n"


#update a board
echo -e "\n"
echo "update a board"
curl -i -H "Content-Type: application/json" -X PUT -d '{"boardName":"Food","boardDesc":"Amazing food","Indian category": "My Favorite Food","isPrivate": "false"}' http://127.0.0.1:5000/users/2/boards/Food/
echo -e "\n"

#delete a board
echo -e "\n"
echo "delete a board"
curl -i -H "Content-Type: application/json" -X DELETE http://127.0.0.1:5000/users/2/boards/Food/
echo -e "\n"


#get all boards 
echo -e "\n"
echo "get all boards "
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/2/boards/
echo -e "\n"





