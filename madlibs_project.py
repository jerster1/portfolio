#upper input
#complain if the enter a blank input
while True:
        adj1 = raw_input("enter an adjective ")
        adj2 = raw_input("enter another adjective ")
        noun = raw_input("enter a noun ")
        place1 = raw_input("enter a place in a house ")
        verb1 = raw_input("enter a verb 'past tense' ")
        verb4 = raw_input("enter another verb ")
        relNoun = raw_input("enter a relative's name ")
        noun2 = raw_input("enter another noun ")
        liquid = raw_input("enter a type of liquid ")
        verb2 = raw_input("enter another verb, ending with 'ing' ")
        noun3 = raw_input("enter a part of the human body ")
        noun4 = raw_input('enter a plural noun ')
        verb3 = raw_input('enter another verb ending with "ing" ')
        noun5 = raw_input("last one, enter one more noun ")

print "it was a %s, cold November day. " % (adj1)
print "I woke up to the %s smell of %s roasting in the %s downstairs. " % (adj2, noun, place1)
print "I %s down the stairs to see if i could help %s the dinner. " % (verb1, verb4)
print 'My mom said, "See if %s needs a fresh %s."' % (relNoun, noun2)
print 'So i carried a tray of glasses full of %s \ninto the %s room. ' % (liquid, verb2)
print "When i got there, I couldn't believe my %s !." % (noun3)
print "There were %s %s on the %s! " % (noun4, verb3, noun5)