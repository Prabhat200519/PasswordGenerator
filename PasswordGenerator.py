#Password generator
import random
import string

print("Password Generator...")
length = int(input("Enter the length of the password:"))

print("""Choose character set for the password
      1. Numbers
      2. Characters
      3. Punctuation
      4. Exit""")

char = ""
while(True):
    choice = int(input("Pick a number:"))
    if (choice == 1):
        char += string.digits
    elif(choice == 2):
        char += string.ascii_letters
    elif(choice == 3):
        char += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Enter valid choice!")
        
password = []
for i in range(length):
    pswd = random.choice(char)
    
    password.append(pswd)
    
    
print("\nThe password is:","".join(password))