def doAddition(num1, num2=1):
    if type(num1) == int and type (num2) is int:
        return num1 + num2
    else:
        return None


input1 = raw_input("interger 1: ")
if input1.isalpha():
    print "thats a letter . . .using 0"
    input1 = 0
else:
    input1 = int(input1)

input2 = raw_input("interger 2: ")
if input2.isalpha():
    print "thats a letter . . .using 0"
    input2 = 0
else:
    input2 = int(input2)


print "your result is %s" % (doAddition(input1, input2))

##

def doSubtraction(num3, num4):
    if type(num3) == int and type (num4) is int:
        return (num3-num4)
    else:
        return None


input3 = raw_input("interger 3: ")
if input3.isalpha():
    print "thats a letter . . .using 0"
    input3 = 0
else:
    input3 = int(input3)

input4 = raw_input("interger 4: ")
if input4.isalpha():
    print "thats a letter . . .using 0"
    input4 = 0
else:
    input4 = int(input4)


print "your result is %s" % (doSubtraction(input3, input4))

##

def doMultiplication(num5, num6):
    if type(num5) == int and type (num6) is int:
        return (num5*num6)
    else:
        return None


input5 = raw_input("interger 5: ")
if input5.isalpha():
    print "thats a letter . . .using 0"
    input5 = 0
else:
    input5 = int(input5)

input6 = raw_input("interger 6: ")
if input6.isalpha():
    print "thats a letter . . .using 0"
    input6 = 0
else:
    input6 = int(input6)


print "your result is %s" % (doMultiplication(input5, input6))

##

def doDivision(num7, num8):
    if type(num7) == int and type (num8) is int:
        return (num7/num8)
    else:
        return None


input7 = raw_input("interger 7: ")
if input7.isalpha():
    print "thats a letter . . .using 0"
    input7 = 0
else:
    input7 = int(input7)

input8 = raw_input("interger 8: ")
if input8.isalpha():
    print "thats a letter . . .using 0"
    input8 = 0
else:
    input8 = int(input8)


print "your result is %s" % (doDivision(input7, input8))



