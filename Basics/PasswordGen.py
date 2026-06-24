import random
import string

def get_lenght():
    user=int(input("enter the lebgth of password:"))
    print("Password Length =", user)
    return user

def generatePassword(Length):
    CombinedStrings=string.ascii_letters + string.digits + string.punctuation
    password="".join(random.choice(CombinedStrings) for i in range(Length))
    print("Generated Password =", password)

def passUseingLoop(length):
    CombinedStrings=string.ascii_letters + string.digits + string.punctuation
    passuseingRandint=""
    for i in range(Length):
        passuseingRandint+=random.choice(CombinedStrings)
    print("Loop", passuseingRandint)


Length=get_lenght()
generatePassword(Length)
passUseingLoop(Length)