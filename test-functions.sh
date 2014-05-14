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


echo -e "\n"
echo "Test create a pin on board just created"
curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Beach", "pinDesc": "Beach in Seychelles"}' http://127.0.0.1:5000/users/2/boards/PlacesToVisit/pins/
echo -e "\n"

echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Mountain", "pinImage": "Everest.jpg", "pinDesc": "Amazing mountain"}' http://127.0.0.1:5000/users/2/boards/PlacesToVisit/pins/
echo -e "\n"


echo -e "\n"
echo "get all pins "
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/2/boards/PlacesToVisit/pins/
echo -e "\n"


#echo -e "\n"
#echo "update pin"
#curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Beach", "pinDesc": "Beach in Seychelles"}' http://127.0.0.1:5000/users/2/boards/PlacesToVisit/pins/13/
#echo -e "\n"


#Test create a comment on a pin on board just created
echo -e "\n"
echo "Test create a comment on a pin on board just created"
curl -i -H "Content-Type: application/json" -X POST -d '{"pinComment": "Wish to visit"}' http://127.0.0.1:5000/users/2/boards/PlacesToVisit/pins/13/comments/
echo -e "\n"


echo -e "\n"
echo "get all comments "
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/2/boards/PlacesToVisit/pins/
echo -e "\n"

