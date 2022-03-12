# Authentication System
import re
from re import fullmatch, compile


def getInfoForRegistration():
    print("welcome, you will be registrate")
    firstname = input("Enter First Name: ")
    lastname = input("Enter Last name : ")
    email = validateEmail()
    password = validatePassword()
    confirmPassword = input("Enter your password again :")
    while True:
        if confirmPassword == password:
            print("valid confirm")
            break
        else:
            confirmPassword = input("try agen : ")

    phonenumber = validatePhone()
    idofuser = getlastid() + 1
    info = ':'.join([str(idofuser), firstname, lastname, email, password, phonenumber])
    writeInFile(info)
    return idofuser


def validateEmail(usefor):
    email = input("Enter your E-Mail : ")
    regex = compile(r'([A-Za-z0-9]+[!-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    userisexit = 0
    while True:
        if fullmatch(regex, email):
            if usefor == 1:  # using for registration
                if searchInFile(email, 3) == 0 and (not userisexit):
                    print("Valid email")
                    break
                else:
                    userisexit = 1
                    print("E-mail is exist")
                    email = input("Enter other E-Mail : ")
            elif usefor == 2:  # using for login
                if searchInFile(email, 3) > 0:
                    print("Valid email")
                    return 1
                else:
                    return 0
        else:
            email = input("Invalid email: try enter agen the e-mail should be like this (example@mail.com) : ")
    return email


def validatePassword():
    password = input("Enter your password : ")
    regex = compile(r'([A-Za-z0-9]+[!-_])*([A-Za-z0-9]+[!-_])')
    while True:
        if fullmatch(regex, password):
            if len(password) >= 6:
                print("Valid password")
                break
            else:
                password = input("the password should be larger than 6 digit or equal. try agen : ")
        else:
            password = input(
                "Invalid password: try enter password agen, should be content the spatial character and number  : ")
    return password


def validatePhone():
    phonenumber = input("Enter your Phone Number : ")
    regex = compile(r'^(?:\+?44)?[07]\d{9,13}$')
    while True:
        if fullmatch(regex, phonenumber):
            print("Valid phonenumber")
            break
        else:
            phonenumber = input(
                "Invalid phonenumber: try enter agen, the phonenumber should be like this (01016529554) : ")
    return phonenumber


def writeInFile(info):
    write = open('users_info.txt', 'a', encoding='UTF-8')
    info = info + '\n'
    write.write(info)
    write.close()


def login():
    print("welcome, you will be login")
    validemil = 0
    while True:
        if validemil == 0:
            username = validateEmail(2)
            validemil = username
        if validemil > 0:
            password = input("Enter you password : ")
            idowner = searchInFile(password, 4)
            if idowner > 0:
                print(" welcome, you are login (: ")
                return idowner
            else:
                print("the password is incorrect ): try agen ")
        else:
            print(" you are not sign in. do you wont? if yes pres (y) or no pres (n) ")
    return 0


def searchInFile(search, section, filename='users_info.txt'):
    try:
        read = open(filename, 'r')
        result = read.readlines()
        try:
            for i in result:
                if i.split(':')[section] == search:
                    return int(i.split(':')[0])
        except IndexError:
            print("file empty")
            if result:
                print("file empty")
                return 0
    except FileNotFoundError:
        return 0
    read.close()
    return 0


def getlastid():
    try:
        read = open('users_info.txt', 'r')
        result = read.readlines()
        if result:
            id = result[-1].split(':')[0]
            return int(id)
        else:
            return 0
    except FileNotFoundError:
        return 0

# validatePassword()
#
# write = open('users_info.txt', 'r', encoding='UTF-8')
# allLines = write.readlines()
# print(allLines)
# allLines[-1] = '15' + '\n'
#
# write = open('users_info.txt', 'w', encoding='UTF-8')
# write.writelines(allLines)
