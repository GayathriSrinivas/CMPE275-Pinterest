#!/bin/bash
# 
#Test all functionalities 
#


echo "Login for user"
echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST -d '{"emailId":"deo.priyanka02@gmail.com", "password":"frfe"}' http://127.0.0.1:5000/users/login/
echo -e "\n"

echo"Test create a board "
echo -e "\n"
echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST -d '{"boardName":"PlacesToVisit","boardDesc":"Nature photos","category": "Nature","isPrivate": "false"}' http://127.0.0.1:5000/users/2/boards/
echo -e "\n"

echo -e "\n"
echo "get all boards "
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/2/boards/PlacesToVisit/
echo -e "\n"



