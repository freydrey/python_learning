#computer guesses random number
from random import random
from time import clock

randVal = random()
print(randVal)

upper = 1.0
lower = 0.0

#guess 0.5 -> Too low -> lower->0.5
#guess 0.9 -> Too high -> upper->0.9
#guess = 0.5
startTime = clock()
while(True): #while true=true
    guess = (upper + lower)/2
    if guess == randVal:
        break
    elif guess < randVal:
        lower = guess  #lower - 0.5, upper-1.0
    else:
        upper = guess 
    guess = (upper + lower)/2
endTime = clock()
print(guess)
print("It took us:", endTime-startTime,"seconds")
