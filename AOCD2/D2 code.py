with open("D2 Dataset.py",'r') as f:
    # print(f.name)
    data = f.readlines()
helperData = []
helper2Data = []
passwordData = []
counter = 0
counter2 = 0
def tobbagan_checker(helper,helper2,password):
    listComp = []
    counter = 0
    length = len(password)
    passwordList = []

    # print(length)
    for i in range(length):
        passwordList.append(password[i])

    for i in range(length):
        if helper2 in passwordList:
            passwordList.remove(helper2)
            counter += 1
        else :
            break

    counterFloor = helper.split("-")[0]
    counterCeiling = helper.split("-")[1]
    print("counter ceiling is " + counterCeiling)
    if counter >= int(counterFloor) and counter <= int(counterCeiling):
        print(True)
        return True
    else:
        print(False)
        return False
        # if helper2 in password[0]:
        #     password.remove(helper2)
        #     counter += 1
        # else:
        #     break

# temp = data[i] for i in range(len(data))
    # tobbagan_checker(temp[0],temp[1],temp[2])
    # if i == 2:
    #     break



# print(counter)
# ansList = map()
def tobbagan_checker2(helper,helper2,password):
    firstpos, secondpos = int(helper.split('-')[0])-1, int(helper.split('-')[1])-1
    print(firstpos)
    print(secondpos)
    length = len(password)
    print(length)
    if firstpos >= length or secondpos >= length:
        return False
    elif password[firstpos] == helper2 and password[secondpos] == helper2:
        return False
    elif password[firstpos] == helper2 or password[secondpos] == helper2:
        return True

for i in range(len(data)):
    temp = data[i].split(" ")
    print(temp[0])
    print(temp[1][0])
    print(temp[2])
    if tobbagan_checker(temp[0],temp[1][0],temp[2]):
        counter += 1
    if tobbagan_checker2(temp[0],temp[1][0],temp[2]):
        counter2 += 1


print(counter2)