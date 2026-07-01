# A really simple Bruteforce-Simulator. 
with open("wordlist.txt") as f:
    wordlist = {line.strip() for line in f}

password = input("Password: ")

if password in wordlist:
    print("Password is really common.")
else:
    print("Password not really common.")
