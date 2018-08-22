myGlobal = 75

def doMath(num1, num2=1, oper='+'):
    if type(num1) is int and type(num2) is int:
        if oper == "+":
            return num1 + num2
        elif : == "-":
            return num1 - num2
        elif : == "*":
            return num1 * num2
        elif : == "/":
            return num1 / num2
        else:
            return None

def multipleValues():
        x =3
        y = x - 10
        return x, y

def messWithGlobal:
    global myGlobal
    print "the value of my global is %s" % myGlobal
    myGlobal = doMath(myGlobal)
    print "the value of my Global is %s" % myGlobal


try:
    input1 = raw_input('interger1 1: ')
    if input1.isalpha():
        print "thats a letter using 0 instead"
        input1 = 0
    else:
        input1 = int(input1)
    input2 = raw_input('interger2 2: ')
    if input2.isalpha():
        print "thats a letter using 0 instead"
        input2 = 0
    else:
        input2 = int(input2)

    sign = raw_input("which operation?")

    result = doMath(input1, input2, sign)
    if result is None
        print "Invalid operator"
    else:
        print "your result is %s" % result