import random

print("welcome to password generator")
for_password="QWERTYUIOPASDFGHJKLZXCVBNMabcdefghijklmnpoqrstuvwzxy1234567890!@#$"

password_lenght= int(input("enter the lenght of password:"))
how_many_password = int(input("how many password do you need? enter here:"))

for x in range(how_many_password):
    password=""
    for y in range(password_lenght):
        password= password + random.choice(for_password)
    print(password)