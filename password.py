import random as rand
import string as str
digits=str.digits
letters=str.ascii_letters
symbols=str.punctuation
print("Welcome to password generator \n")
length=int(input("Enter the length of the password:"))
password=[]
for i in range(0,length):
    password.append(rand.choice(letters+digits+symbols))
rand.shuffle(password)
pass_word=""
for char in password:
    pass_word+=char
print("Your password is \""+pass_word,"\"")





