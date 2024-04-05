#Decrypt and encrypt caesar ciphers
#Either encrypts or decrypts
#force lowercase
# ALPHABET usedf to decode
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
# for easy encrypt in other files
def encrypt(MESSAGE,KEY):
    OUTPUT = ""
    for char in MESSAGE:
        if char.isupper():
            char.lower()
        elif char in ALPHABET:    
            c = ALPHABET.index(char)
            shifted = (c + KEY)% 26
            OUTPUT += ALPHABET[shifted] 
        else:
            OUTPUT += char
    return OUTPUT

# easy decrypt
def decrypt(MESSAGE,KEY):
    OUTPUT = ""
    for char in MESSAGE:
        if char.isupper():
            char.lower()
        elif char in ALPHABET:   
            c = ALPHABET.index(char)
            shifted = (26 + c - KEY) % 26
            OUTPUT += ALPHABET[shifted]
        else:    
            OUTPUT += char
    return OUTPUT

if __name__ == "__main__":
    val = "ERROR"
    Message = str(input('Message to proces '))
    key = int(input('How many letters to shift '))
    mode = int(input('type 1 or 2 for Encrypt/Decrypt(Default is Encrypt) '))
    print("Message:", Message)
    print("Key:", key)
    print("Mode:", mode)
    if mode == 1:
        val = encrypt(Message,key)
    elif mode == 2:
        val = decrypt(Message,key)
    print(val)
