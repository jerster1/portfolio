def getWord(wordType):
    while True:
        word = raw_input("Please enter a(n) %s: " % (wordType))
        if word == "":
            continue
        else:
            return word


myWords = ('adjective', 'plural noun', 'exclamation')
userWords = []

for x in myWords:
    userWords.append(getWord(x).upper())

print "You %s opened the can of %s. %s!" % (userWords[0],
    userWords[1], userWords[2])
