import random
import os

#Characters for the password
letters1="abcdefghijklmnñopqrstuvwxyz"
letters2="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numbers="0123456789"
simbols="!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~."
data=""

#Clear console
def defaultState():
    if os.name == "nt":
        os.system("cls")
        print("[-------------Password Generator-------------]\n"+
      "[---------by Franco Salvador Talarico--------]\n"
      "[---------------Version: 1.0.0---------------]\n"+data)
    else:
        os.system("clear")
        print("[-------------Password Generator-------------]\n"+
      "[---------by Franco Salvador Talarico--------]\n"
      "[---------------Version: 1.0.0---------------]\n"+data)
    
defaultState()
iLength=int(input("Enter the number of characters for your password:\n"))
data=f"\n[Length: {iLength}]\n"
defaultState()
iSimbols=str(input("With symbols? Type [yes] or [no]\n"))
data=f"\n[Length: {iLength}]\n[Simbols: {iSimbols}]\n"
defaultState()
iNumbers=str(input("With numbers? Type [yes] or [no]\n"))
data=f"\n[Length: {iLength}]\n[Simbols: {iSimbols}]\n[Numbers: {iNumbers}]\n"
defaultState()
iLetter2=str(input("With uppercase? Type [yes] or [no]\n"))
data=f"\n[Length: {iLength}]\n[Simbols: {iSimbols}]\n[Numbers: {iNumbers}]\n[Uppercase: {iLetter2}]\n"
defaultState()

mult=int(iLength/3)
unify=letters1*mult

if iSimbols == "yes":
    unify+=simbols*mult
if iNumbers == "yes":
    unify+=numbers*mult
if iLetter2 == "yes":
    unify+=letters2*mult

length=iLength
password = random.sample(unify,length)
final_password = "".join(password)

data=f"\n[Length: {iLength}]\n[Simbols: {iSimbols}]\n[Numbers: {iNumbers}]\n[Uppercase: {iLetter2}]\n\n[Password]:\n{final_password}\n"
defaultState()

iName=str(input("Enter the password name:\n"))

#Create folder and document
os.mkdir('Passwords')
arc=open("Passwords/"+iName+".txt","w") 
arc.write(final_password) 
arc.close() 

print("[Password saved and generated successfully.]")