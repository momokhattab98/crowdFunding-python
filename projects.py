# from CrowdFundingConsoleApp import login
from datetime import datetime as dt


def projectinfo(ownerid):
    print('hey, you will new add project')
    title = input("enter the project title : ")
    details = input("Enter project details : ")
    totaltarget = input("Enter total target for project : ")
    startingtime = validdate(input("Enter time of start the project : "))
    endingtime = validdate(input("Enter time of end the project : "))
    idofowner = str(ownerid)
    info = ':'.join([idofowner, title, details, totaltarget, startingtime, endingtime])
    writeprojectsinfile(info)
    print('done (: ')


def displayall():
    try:
        read = open('projects.txt', 'r')
        result = read.readlines()
        try:
            for i in result:
                value = i.split(':')
                print(value[1], value[2], value[3], value[5])
        except IndexError:
            print("file empty")
            if result:
                print("file empty")
                return 0
    except FileNotFoundError:
        return 0
    else:
        read.close()
    return 0


def editproject(idowner):
    try:
        read = open('projects.txt', 'r')
        result = read.readlines()
        for i in range(len(result)):
            index = result[i].split(':')
            if index[0] == str(idowner):
                print("what are you wont to change?")
                sectionch = input("if wont change title press (t), details pres (d), total target (tt),"
                                  "start date (s) or end date (e) : ")
                result[i] = ':'.join(changeonproject(sectionch, index))
                break
        read = open('projects.txt', 'w')
        read.writelines(result)
    except FileNotFoundError:
        print("the file isn't exist")
    else:
        print('done (: ')
        read.close()


# proplem not found
def deleteproject(idowner):
    try:
        read = open('projects.txt', 'r')
        result = read.readlines()
        index = -1
        for i in range(len(result)):
            if result[i].split(':')[0] == str(idowner):
                index = i
                break
        if index != -1:
            result.pop(index)
        else:
            print("not found")
        read = open('projects.txt', 'w')
        read.writelines(result)
    except FileNotFoundError:
        print("the file isn't exist")
    else:
        print('done ): ')
        read.close()


def searchofprojects():
    date = validdate(input("please, write the date you search for."))
    try:
        read = open('projects.txt', 'r')
        result = read.readlines()
        found = 0
        try:
            for i in result:
                value = i.split(':')
                if value[5] == date:
                    print(value[1], value[2], value[3], value[5])
                    found = 1
            else:
                if found == 0:
                    print('No project has this date :', date)
        except IndexError:
            print("file empty")
            if result:
                print("file empty")
                return 0
    except FileNotFoundError:
        print("file not exist")
        return 0
    else:
        read.close()
    return 0


def writeprojectsinfile(info):
    write = open('projects.txt', 'a', encoding='UTF-8')
    info = info + '\n'
    write.write(info)
    write.close()


def changeonproject(scch, project):
    while True:
        if scch == 't':
            project[1] = input("what are you change title for? : ")
            return project
        elif scch == 'd':
            project[2] = input("You change details for what? : ")
            return project
        elif scch == 'tt':
            project[3] = input("You change details for what? : ")
            return project
        elif scch == 's':
            project[4] = validdate(input("You change details for what? : "))
            return project
        elif scch == 'e':
            project[5] = validdate(input("You change details for what? : "))
            return project
        else:
            scch = input("you can chose form [t,d,tt,s,e] nothing else : ")


def validdate(date):
    while True:
        try:
            dt.strptime(date, "%Y-%m-%d")
        except ValueError:
            date = input("date should be like this '2022-01-15' : ")
        else:
            return date

# editproject(2)
# deleteproject(3)
