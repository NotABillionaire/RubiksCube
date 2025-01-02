#Thomas 
#Login System
#changed 29/9/2024

import Config #Imports my global variables
import time
import os, random
from hashlib import sha256
import linecache



#This will add the new file you created for generation
import Cube_Generation

file = "user.txt"

#Check if the files exist
if not os.path.exists("user.txt"):
    open("user.txt", "w").close()

if not os.path.exists("Hashed.txt"):
    open("Hashed.txt", "w").close()

#Login or signup
def start():
    while True:
        L = input("Login OR Signup \n").lower()
        if L == "signup":
            print("Hello, welcome to Signup \n")
            Signup1()
            break
        elif L == "login":
            print("Hello and welcome to login")
            login1()
            break
        else:
            print("Please enter 'Login' or 'Signup'")

#Code for signup
def Signup1():
    userfound = False
    user = input("Enter username: ")
    with open("user.txt", "r") as file:
        for line in file:
            line = line.rstrip("")
            data = line.split(",")
            if data[0] == user:  # Checks to see if the username is already in use
                userfound = True
                print("\nThis username is already taken. Try login\n")
                start()
                return
    if not userfound:
        user_id = str(len(open("user.txt").readlines()) + 1)  #Counts the number of lines in the file
        print("This username is valid\n")
        with open("user.txt", "a") as file:
            file.write(user + ",")
            file.write(user_id)
            file.write("\n")
        Next()

#Create account
def Next():
    password = input("Enter a password: ")
    user_id = str(len(open("Hashed.txt").readlines()) + 1)  #Adds one to the readlines because of the PLACEHOLDER
    with open("Hashed.txt", "a") as file:
        file.write(sha256(password.encode('utf-8')).hexdigest() + ",")  #Writes the hash to the file
    print("\nPlease answer our security question: ")
    fq = input("\nYour First Pet's Name? : ")
    with open("Hashed.txt", "a") as file:
        file.write(fq + ",")
        file.write(user_id)
        file.write("\n")
    print("Please could you login now")
    login1()

#Login to the account
def login1():
    user2 = input("Enter username: ")
    user_id = None
    with open("user.txt") as file:
        for line in file:
            data = line.split(",")  #Splits the username and user_id
            if data[0] == user2:
                user_id = data[1].strip()
                print("Username found")
                break
    if user_id:
        psn = input("Enter password: ")
        psn_hashed = sha256(psn.encode('utf-8')).hexdigest()  #Encodes the entered password
        hashed_line = linecache.getline("Hashed.txt", int(user_id))
        if psn_hashed in hashed_line:  #Uses the User_id to get the line number
            print("Password found")
            print("Hello", user2, "welcome to your account")
            #Game code here
            Config.sensitivity = float(input("please enter your preferred sensitivity (0 - 0.5)"))
            Cube_Generation.main()
        else:
            print("Password not found")
            start()
    else:
        print("Username not found")
        print("You are starting again for security reasons")
        start()

start()

