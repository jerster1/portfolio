#comparing two strings and then making a function
var1 = True
def compareStrings(str1, str2):
    if str1.isalpha() and str2.isalpha():
        if len(str1) > len(str2):
            print "string 1 is higher"
        elif len(str2) > len(str1):
            print "sting 2 is higher"
        else:
            print "they are the same"
    else: 
        raise SyntaxError
    return


while var1: True
    str1 = raw_input("first string")
    str2 = raw_input("sec. string")
    
    try:
        func1 = compareStrings(str1, str2)
    except SyntaxError:
        print "invalid entry"
        continue

    if func1 == "str1":
         print "first string is longer"
    elif func1 == "str2":
        print "second string is longer"
    else:
        print "they are both equal"


#while var1:
#    str1 = raw_input("first string")
 #   str2 = raw_input("sec. string")
  #  if len(str1) > len(str2):
   #     print "string 1 is higher"
    #elif len(str2) > len(str1):
     #   print "sting 2 is higher"
#    else:
 #       print "they are the same"
  #  
   # while True:
    #    ans1 = raw_input("would u like to do again? y/n ")
     #   if ans1.lower().startswith('y'):
      #      var1 = True
       #     break
#        elif ans1.lower().startswith('n'):
 #           var1 = False
  #          break
   #     else:
    #        print "your a jerk"




    #if len(str1) > len(str2):
        #print "string 1 is higher"
    #elif len(str2) > len(str1):
        #print "sting 2 is higher"
    #else:
       # print "they are the same"
  #  
  #  while True:
   #     ans1 = raw_input("would u like to do again? y/n ")
    #    if ans1.lower().startswith('y'):
    #        var1 = True
    #        break
  #      elif ans1.lower().startswith('n'):
   #         var1 = False
  #         break
  #      else:
   #         print "your a jerk"            