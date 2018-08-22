userList = {}

while True:
    try:
        user = raw_input("please input a name, ")
        if user != "":    
            number = raw_input("please input the number, ")
            dob = raw_input("please input the dob, ")
            ssn = raw_input("please input the ssn, ")
            userList[user] = [number, dob, ssn]
        else:
            break
    except KeyboardInterrupt:
        print "\n"
        break
print "name,number,DOB,ssn"



for name in sorted(userList.keys()):
    for x in userList[name]:
        name = name + "," + x
    print name

