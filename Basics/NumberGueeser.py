import random;
import string

# number=int(random.choice(string.digits))
number=random.randint(0,100);
# print(number);
CorrectGuess=True
count=0;
while(CorrectGuess):
    count=count+1;
    userNumber=int(input("Enter Your Guess: "))
    if(userNumber>number):
        print("Lower")
    elif(userNumber<number):
     print("Higher")
    elif(userNumber==number):
       print("You guessed Correct:")
       print("You got corrct answer after:",count)
       CorrectGuess=False