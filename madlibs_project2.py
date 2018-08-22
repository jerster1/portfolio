def getWord(type):
        while True:
            word = raw_input("Please enter a %s") % (word)
            if word == ""
                continue
            else:
                return word


myWords = ('adjective', 'plural noun')
userWords = []

for x in myWords:
    userWords[x] = getWord(x)

print "You %s opened the can of %s" % (userWords[0], userWords[1])