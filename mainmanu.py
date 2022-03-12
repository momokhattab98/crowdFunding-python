from CrowdFundingConsoleApp import login, getInfoForRegistration
from projects import *

userid = 0

def screen():
    print("hello!! the is a program for Crowd Funding ")
    isuser = input("Do you already have an account? if yes pres (y) or no (n) : ")
    while True:
        if isuser == 'y':
            userid = login()
            break
        elif isuser == 'n':
            userid = getInfoForRegistration()
            break
        else:
            isuser = input("sorry ): you can't continue if not user if you wont stop pres (s) : ")
            if isuser == 's':
                break
    if userid > 0:
        operat = input("if you want create a new project pres(c), \nEdit your project pres(e), "
                       "view all projects in program pres(v),\n"
                       "delete your project pres(d),\n"
                       "or search in projects by end date pres(s)\n ===> : ")
        flag = 0
        while True:
            if flag == 0:
                if operat == 'c':
                    projectinfo(userid)
                    flag = 1
                elif operat == 'e':
                    editproject(userid)
                    flag = 1
                elif operat == 'v':
                    displayall()
                    flag = 1
                elif operat == 'd':
                    deleteproject(userid)
                    flag = 1
                elif operat == 's':
                    searchofprojects()
                    flag = 1
                elif operat == 'x':
                    break
                else:
                    operat = input("please choose any char of this [c,e,v,d,s] only : ")
            else:
                operat = input("\nEdit your project pres(e), \n"
                               "view all projects in program pres(v),\n"
                               "delete your project pres(d),\n"
                               "search in projects by end date pres(s),\n"
                               "or Exit form program pres(x)\n ===> : ")
                flag = 0


screen()
