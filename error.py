#excercise 2
print "we're going to see how high we can count!"

num = 0

while True:
    try:
        num = num + 1
    except:
        break

print "your max number is %s" % (num) 