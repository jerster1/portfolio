import os

print "current working directory %s" % (os.getcwd())

x = os.path.join(os.getcwd(), "test-dir")

print "Test path %s" % (x)

if os.path.exists(x) and os.path.isdir(x):
    print "directory alrdy exist"
    os.rmdir(x)
    print "i deleted it"
elif os.path.exists(x) and os.path.isfile(x):
    print "thats a file"
    ren = raw_input("should we rename it?")
    if ren.lower().startswith('y'):
        os.rename(x, os.path.join(os.getcwd(), "test-dir.file"))
        print "ok we renamed the file and created the directory
else:
    print "creating directory..."
    os.mkdir(x)
    print "done!"    