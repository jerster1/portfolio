#lesson 1
#firstName = raw_input("what is your name? ")
#lasttName = raw_input("what is your last name? ")
#address = raw_input("what is your address? ")
#phonenumber = raw_input("what is your phone number? ")
#age = input("How old are you? ")
#
#lesson 2
#firstname = raw_input("what is ur name? ")
#
#print "Your name is %s characters long." % (len(firstname))
#
#Lesson 3
#
#userinput = raw_input("LmFaO RawR Eks DeEe")
#print userinput.lower()
#print userinput.upper()
#
#Lesson 5
#var1 = 'string ges here'
#var2 = 2
#var3 = 3.6
#
#print "your variable's type is %s" % (type(var3))
#
#print "the type of this thing is %s" % (type(str)(var2))

myList = []

num = 0

while num is not None:
    try:
      num = input('(blank line to quit)\nGive me a number: ')
      myList.append(num)
    except SyntaxError:
      num = None
      
print "your input it %s" % (myList)
print "the biggest number is %s" % (max(myList))
print "your input backwords is %s" % (list(reversed(myList)))
print "Your input in order is %s" % (sorted(myList))

