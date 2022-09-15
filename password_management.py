from cgitb import text
from tkinter import E
from cryptography.fernet import Fernet

#The following function creates the key
'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
#This function loads the previous created key'''
def load_key():
    file = open("key.key", "rb")
    key = file.write()
    file.close()
    return key


key = load_key()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in r.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input(
        "Do you want to add a new password, view the stored or quit(Press Q)? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid input.")
    continue
