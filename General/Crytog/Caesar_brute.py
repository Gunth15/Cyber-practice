from Caesar import decrypt
active = True

#mass decryption into a file
while(active):
    #file to place decrypted text
    f = open(str(input("Name of File: "))+".txt","w")
    #message to decrypt
    message=str(input("What is the meassage: "))
    
    #Tries every possible Caesar_based rotation and places it in specified file
    for rotate in range(27):
        d = decrypt(message,rotate)
        f.write(f"message: {d} with rotation: {rotate}\n")
        
    f.close()

    stop = str(input("Stop? y/n "))
    if stop == "y":
        active = False
        print("exiting")
