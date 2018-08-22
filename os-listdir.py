# pylint: disable=E1601

import os

header = "{: <{w}}\tSize (B)\n{: <{w}}\t--------"
fmt = "{n: <{w}}\t{sz: <0.0f}"

path = os.getcwd() #Gets current wokring dir.
files = []

currFiles = os.listdir(path)

if currFiles == []:
    print "No files exist in %s" % (path)

else:
    print "Current files in %s\n" % (path)

    for f in currFiles: # For every files in currFiles display
        fileSize = os.path.getsize(os.path.join(path, f)) #gets the file size Path.join connects 2 strings
        if os.path.isdir(f):
            f = "%s (*)" % (f)
        fileTuple = (f, fileSize) #storing fil size in a tuple
        files.append(fileTuple) 

    files.sort(key=lambda myTuple: myTuple[1], reverse=True)#sorting list by filesize

    print header.format('Filename', "--------",
                        w=len(max(currFiles, key=len))+2)
    for f, s in files:
        print fmt.format(n=f, sz=s, w=len(max(currFiles, key=len))+2)
        print "%s\t%s" % (f, s)
