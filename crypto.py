def encipher(cleanText, offset=1):
    cipherText = ''
    for c in cleanText:
        if ord(c) > 126:
            x = (ord(c) + offset) % 95
        else:
            x = ord(c) + offset
        print(x)
        c = chr(x)
        print(c)
        cipherText += c
     
    return cipherText
 
 
pText = input('What do you want to encipher? ')
print("Your input: {}".format(pText))
x = encipher(pText)
print("Your ciphertext: {}\nOrdinances: {}".format(x,0))