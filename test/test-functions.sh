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
curl -i -H "Content-Type: application/json" -X POST -d '{"boardName":"Food","boardDesc":"Amazing Food","Indian category": "Food","isPrivate": "false"}' http://127.0.0.1:5000/users/1/boards/
curl -i -H "Content-Type: application/json" -X POST -d '{"boardName":"Decor","boardDesc":"Beautiful Decor","category": "Home Decor","isPrivate": "True"}' http://127.0.0.1:5000/users/1/boards/
curl -i -H "Content-Type: application/json" -X POST -d '{"boardName":"Clothes","boardDesc":"Very Pretty Collection","category": "Summer Wear","isPrivate": "false"}' http://127.0.0.1:5000/users/1/boards/
echo -e "\n"

echo -e "\n"
echo "get all boards "
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/1/boards/Food/
echo -e "\n"

echo -e "\n"
echo "Upload images to server"
curl -F "file=@client-images/food1.jpg" http://127.0.0.1:5000/image/
curl -F "file=@client-images/food2.jpg" http://127.0.0.1:5000/image/
curl -F "file=@client-images/food3.jpg" http://127.0.0.1:5000/image/
curl -F "file=@client-images/food4.jpg" http://127.0.0.1:5000/image/
echo -e "\n"

echo -e "\n"
echo "Upload images to server"
curl -F "file=@client-images/clothes1.jpg" http://127.0.0.1:5000/image/
curl -F "file=@client-images/clothes2.jpg" http://127.0.0.1:5000/image/
curl -F "file=@client-images/clothes3.jpg" http://127.0.0.1:5000/image/
curl -F "file=@client-images/clothes4.jpg" http://127.0.0.1:5000/image/
echo -e "\n"

echo -e "\n"
echo "Upload images to server"
curl -F "file=@client-images/decor1.jpg" http://127.0.0.1:5000/image/
curl -F "file=@client-images/decor2.jpg" http://127.0.0.1:5000/image/
curl -F "file=@client-images/decor3.jpg" http://127.0.0.1:5000/image/
curl -F "file=@client-images/decor4.jpg" http://127.0.0.1:5000/image/
echo -e "\n"

echo -e "\n"
echo "Test create pin on board just created"
curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Food", "pinImage": "food1.jpg","pinDesc": "Amazing Food"}' http://127.0.0.1:5000/users/1/boards/Food/pins/
echo -e "\n"

echo -e "\n"
echo "get all pins "
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/1/boards/Food/pins/
echo -e "\n"

#Test create a comment on a pin on board just created
echo -e "\n"
echo "Test create comment on a pin on board just created"
curl -i -H "Content-Type: application/json" -X POST -d '{"pinComment": "Wish to eat"}' http://127.0.0.1:5000/users/1/boards/Food/pins/1/comments/
echo -e "\n"

echo "get all comments "
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/1/boards/Food/pins/
echo -e "\n"

