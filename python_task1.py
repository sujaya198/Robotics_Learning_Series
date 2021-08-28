from random import *
from copy import *
def score_calculation(guessed_number,n,correctplace,wrongplace,m):
    if guessed_number==n:
        print("you have guessed the number correctly.You've won the game.")
        return 1
    else:
        for i in range(0,4):
           if guessed_number[i] in m:
              if guessed_number[i]==n[i]:
                 correctplace.append(guessed_number[i])
              else:
                 wrongplace.append(guessed_number[i])
        print(len(correctplace), " correct digits at correct position: ", correctplace)
        print(len(wrongplace), " correct digits at wrong position ", wrongplace)
        return 0
def result(ch):
 while ch==1:
    ran = randint(1000,9999)
    score=20
    n= [int(i) for i in str(ran)]
    no_of_guesses=10
    while no_of_guesses > 0:
           m,  correctplace,  wrongplace= deepcopy(n),  [],  []
           guess = int(input("Guess the 4 digit number : "))
           guessed_number = [int(i) for i in str(guess)]

           x=score_calculation(guessed_number,n,correctplace,wrongplace,m)

           if(x==1):
                score+=5
                break
           else:
                score-=2
           no_of_guesses -= 1
           print("Sorry wrong number. Guess again.\n no of guesses left : ",no_of_guesses)

    print("Your score is : ", score)
    ch = int(input("You have finished the game. Do you want to play again?\n1 - Yes\n0 - No\n"))
result(ch = int(input("Do you want to play the MASTERMIND GAME?\n1 - Yes\n0 - No\n")))


