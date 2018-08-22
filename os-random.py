# pylint: disable=E1601

import os

print "Current Directory: %s" % (os.getcwd())

x = os.path.join(os.getcwd(), "test-dir")

print "Test path: %s" % (x)

if os.path.exists(x) and os.path.isdir(x):
    print "Directory already exists!"
    os.rmdir(x)
    print "I deleted it..."
elif os.path.exists(x) and os.path.isfile(x):
    print "That's a file."
    ren = raw_input("Should we rename it?")
    if ren.lower().startswith('y'):
        os.rename(x, os.path.join(os.getcwd(), "test-dir.file"))
        os.mkdir(x)
        print "Ok, we renamed the file and created the directory!"
else:
    print "Creating directory..."
    os.mkdir(x)
    print "Done!"

# print os.environ.items()
# print os.environ.get('HOME')
# os.remove(x)
