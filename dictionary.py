AgeDict = {'John': 32, 'Larry': 97, 'steven': 13}

who = ''
print "enter 0 to bail out"
while who != '0':
      who = raw_input("Whos age d u want to know ")
      who = who.title()

if who == '0':
       pass

elif AgeDict.has_key(who):
            print AgeDict[who.title]
    
else:
            print "there is nobody nameed %s " % who
            print "your options are: %s" % (AgeDict.keys()) 

print 'you rock'
