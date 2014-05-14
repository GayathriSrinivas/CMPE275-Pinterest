#!/bin/bash
# 
#Create 4 users on Pinterest
#


echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST -d '{"firstName":"Priyanka", "lastName":"Deo", "emailId":"deo.priyanka02@gmail.com", "password":"frfe"}' http://127.0.0.1:5000/users/signUp/
echo -e "\n"

echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST -d '{"firstName":"Gayatri", "lastName":"Srini", "emailId":"gaya.0408@gmail.com", "password":"abcd"}' http://127.0.0.1:5000/users/signUp/
echo -e "\n"

echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST -d '{"firstName":"Madhu", "lastName":"Raman", "emailId":"madhuraman87@gmail.com", "password":"efgh"}' http://127.0.0.1:5000/users/signUp/
echo -e "\n"

echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST -d '{"firstName":"Aish", "lastName":"Indra", "emailId":"aish.indra@gmail.com", "password":"abcd"}' http://127.0.0.1:5000/users/signUp/
echo -e "\n"

