#!/bin/bash
message=$1
key=$(echo {z..a}| tr -d ' ') #creates list of chracters mint he reverse order, will serve as key

#user can decrypt or encrypt
if [ "$2" = "encrypt" ]; then
  #prints the encrypted message
  echo "$message"| tr 'a-z' "$key"
fi
if [ "$2" = "decrypt" ]; then
  #prints decrypted message
  echo "$message"| tr "$key" 'a-z'
fi
