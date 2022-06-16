# Script Created by: Jukww2

import random
import datetime
import os.path

_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
_chars = [",", ".", "!", "?", ";", ":", "'", "`", "~", "^", "&", "*", "(", ")", "[", "]", "{", "}", "<", ">", "/", "|", "=", "+", "-", "_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

_filePath = input("Enter the folder path who the password will be save. Don't miss the \ or /: ")
_passwordChars = int(input("Enter the characters you want to use for the password: "))

os.path.normcase(_filePath)

password = ""

while True:
    num = random.randint(0, 2)

    if num == 0:
        password += random.choice(_keys)
    elif num == 1:
        password += random.choice(_chars)
    elif num == 2:
        key = random.choice(_keys)
        char = random.choice(_chars)
    
    if len(password) >= _passwordChars:
        break
    
print(f"The password is : {password}")

actualDate = datetime.datetime.now()
fileDate = f"{actualDate.strftime('%d')}-{actualDate.strftime('%m')}-{actualDate.strftime('%y')}-{actualDate.strftime('%H')}-{actualDate.strftime('%M')}-{actualDate.strftime('%S')}"

passwordFile = open(f"{_filePath}{fileDate}.txt", "w")
passwordFile.write(str(password))