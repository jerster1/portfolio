from os import utime, getcwd as cwd
from os.path import join

ourPath = path.join(cwd(), "checkfile")

with open(ourPath, 'a') as myFile:
    utime(ourPath, None)