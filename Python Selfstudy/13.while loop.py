i=0
while(i<=10):
    print(i)
    i=i+1

#Guessing Game

guess=""
secret_word="Alpha"
outOfGuesses=False
guess_count=0
guess_limit=3

while guess!=secret_word and not(outOfGuesses):
    if guess_count<guess_limit:
        guess=input("Enter Your Guesses: ")
        guess_count+=1
    else:
        outOfGuesses=True

if outOfGuesses:
    print("You are loss!,Out of Guesses!")
else:
    print("You are win!")