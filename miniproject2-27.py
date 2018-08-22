import sys
import os

path = raw_input("place ur path here")
os.path.exists(path), "i did not find the directory at, " +str(path)
f = open(path,'r')
print("Hooray we found your file!")