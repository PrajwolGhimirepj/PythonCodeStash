
import random
import string

def get_length():
    while True:
        try:
            length = int(input("Enter the Password length (8-128): "))
            if 8 <= length <= 128:
                return length
            else:
                print("Please enter a number between 8 and 128.")
    

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


length = get_length()
password = generate_password(length)
print(f"Generated password: {password}")

