import sys

def binDecoder(message):
    try: 
        
        if len(message) % 7 == 0:
            response = ""
            #run through the 7 bit ascii
            for i in range(0, len(message), 7):
                response += chr(int(message[i:i+7], 2))
            print(response)

        if len(message) % 8 == 0:
            response = ""
            #run through the 8 bit ascii
            for i in range(0, len(message), 8):
                response += chr(int(message[i:i+8], 2))
            print(response)

    except ValueError:
        print("use: ./binDecode <binary>")
        return

binDecoder(input(""))