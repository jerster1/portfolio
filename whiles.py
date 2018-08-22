# pylint: disable=E1601
userList = {}

while True:
    user = raw_input('Enter a name: ')
    if user != "":
        phone = raw_input('Phone Number: ')
        dob = raw_input('Date of Birth: ')
        ssn = raw_input('Social Security Number: ')
        userList[user] = [phone, dob, ssn]
        clean_dict = {key.strip(): item.strip() for key, item in userList}
    else:
        break


print clean_dict


#print "name,phone,date of birth,ssn"
#for name in sorted(userList.keys()):
#    for x in userList[name]:
#        name = name + "," + x
#    print name

#strip special characters
#format the output
