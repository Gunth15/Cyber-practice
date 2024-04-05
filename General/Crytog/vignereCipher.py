#   sadie sanders
#   a vignere cypher progam: can encode and decode
#   via ceasar with a key

import sys
#encryption function
def encrypt(message, key):
    #variables needed
    keyPos = 0
    encryptedText = ""

    #loop through entire message
    for i in message:
        #if character is a letter
        if ((ord(i) >= 97) and (ord(i) <= 122)) or (ord(i) >= 65 and (ord(i) <= 90)):
            #if character is a lowercase letter
            if (ord(i) >= 97) and (ord(i) <= 122):
                encryptedText += chr(((ord(i) - 97) + (ord(key[keyPos]) - 97)) % 26 + 97)
            
            #if character is an uppercase letter
            else:
                encryptedText += chr(((ord(i) - 65) + (ord(key[keyPos]) - 97)) % 26 + 65)
            #shift key position only if letter has been encrypted
            keyPos += 1
            if keyPos > len(key) - 1: keyPos = 0

            #if character is not a letter
        else:
            encryptedText += i
    return encryptedText

#decryption function
def decrypt(message, key):
    #variables needed
    keyPos = 0
    plainText = ""

    #loop through entire message
    for i in message:
        #if character is a letter
        if ((ord(i) >= 97) and (ord(i) <= 122)) or (ord(i) >= 65 and (ord(i) <= 90)):
            #if character is a lowercase letter
            if (ord(i) >= 97) and (ord(i) <= 122):
                plainText += chr(((26 + (ord(i) - 97) - (ord(key[keyPos]) - 97)) % 26) + 97)
            
            #if character is an uppercase letter
            else:
                plainText += chr(((26 + (ord(i) - 65) - (ord(key[keyPos]) - 97)) % 26) + 65)
            
            #shift key position only if letter has been decrypted
            keyPos += 1
            if keyPos > len(key) - 1: keyPos = 0
        #if character is not a letter, just add it on
        else:
            plainText += i
    return plainText

#check for proper useage
try: 
    if(sys.argv[1] == "-e" or sys.argv[1] == "-d") and (sys.argv[2]): isRun = True #add -e or -d detection
    else: print("useage: <-e/-d> <key>"); sys.exit()
except(IndexError): 
    print("useage: <-e/-d> <key>")
    sys.exit()

#if everything is correct, do the main function
#to exit, press "ctrl + c"
while isRun:
    try:
        message = input("")
        if(sys.argv[1] == "-e"):
            print(encrypt(message, sys.argv[2]))
        elif (sys.argv[1] == "-d"):
            print(decrypt(message, sys.argv[2]))
    except KeyboardInterrupt:
        print("break detected")
        sys.exit()
