try:
    with open(r"C:\Users\ajjer\Documents\hackeru\test.txt", "a+") as myFile:
    
        print "here are the contents of the file"
        for line in myFile:
            print line

        print 'Enter lines below to append. Use . on a by iteself to end'
        while True:
            userInput = raw_input("> ")
            
            if userInput == ".":
                break
            else:
                myFile.write(userInput + "\n")
                myFile.flush()  #Immedialty saves to file
            
        #myFile.close() #closees the file in the background

except IOError:
    print "that file doesn't exist"