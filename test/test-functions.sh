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
curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Food", "pinImage": "food2.jpg","pinDesc": "Food2"}' http://127.0.0.1:5000/users/1/boards/Food/pins/
curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Food", "pinImage": "food3.jpg","pinDesc": "Food3"}' http://127.0.0.1:5000/users/1/boards/Food/pins/
curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Food", "pinImage": "food4.jpg","pinDesc": "Food4"}' http://127.0.0.1:5000/users/1/boards/Food/pins/
echo -e "\n"

echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Home Decoration1", "pinImage": "decor1.jpg", "pinDesc": "simple and neat designs"}' http://127.0.0.1:5000/users/1/boards/Decor/pins/
curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Home Decoration2", "pinImage": "decor2.jpg", "pinDesc": "simple and neat designs"}' http://127.0.0.1:5000/users/1/boards/Decor/pins/
curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Home Decoration3", "pinImage": "decor3.jpg", "pinDesc": "simple and neat designs"}' http://127.0.0.1:5000/users/1/boards/Decor/pins/
curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Home Decoration4", "pinImage": "decor4.jpg", "pinDesc": "simple and neat designs"}' http://127.0.0.1:5000/users/1/boards/Decor/pins/
echo -e "\n"

echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Clothes 1", "pinImage": "clothes1.jpg", "pinDesc": "nice clothes"}' http://127.0.0.1:5000/users/1/boards/Clothes/pins/
curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Clothes 2", "pinImage": "clothes2.jpg", "pinDesc": "nice clothes"}' http://127.0.0.1:5000/users/1/boards/Clothes/pins/
curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Clothes 3", "pinImage": "clothes3.jpg", "pinDesc": "nice clothes"}' http://127.0.0.1:5000/users/1/boards/Clothes/pins/
curl -i -H "Content-Type: application/json" -X POST -d '{"pinName": "Clothes 4", "pinImage": "clothes4.jpg", "pinDesc": "nice clothes"}' http://127.0.0.1:5000/users/1/boards/Clothes/pins/
echo -e "\n"
echo "get all pins "
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/1/boards/Food/pins/
echo -e "\n"

echo -e "\n"
echo "get all boards "
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/1/boards/Food/
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/1/boards/Clothes/
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/1/boards/Decor/
echo -e "\n"


#Test create a comment on a pin on board just created
echo -e "\n"
echo "Test create comment on a pin on board just created"
curl -i -H "Content-Type: application/json" -X POST -d '{"pinComment": "Wish to eat"}' http://127.0.0.1:5000/users/1/boards/Food/pins/1/comments/
curl -i -H "Content-Type: application/json" -X POST -d '{"pinComment": "superb"}' http://127.0.0.1:5000/users/1/boards/Food/pins/1/comments/
echo -e "\n"

echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST -d '{"pinComment": "nice decor"}' http://127.0.0.1:5000/users/1/boards/Decor/pins/5/comments/
curl -i -H "Content-Type: application/json" -X POST -d '{"pinComment": "cool decor"}' http://127.0.0.1:5000/users/1/boards/Decor/pins/5/comments/
echo -e "\n"

echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST -d '{"pinComment": "nice clothes"}' http://127.0.0.1:5000/users/1/boards/Clothes/pins/9/comments/
curl -i -H "Content-Type: application/json" -X POST -d '{"pinComment": "clothes"}' http://127.0.0.1:5000/users/1/boards/Clothes/pins/9/comments/

echo "get all comments "
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/1/boards/Food/pins/
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/1/boards/Decor/pins/
curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/users/1/boards/Clothes/pins/
echo -e "\n"

