# What does this piece of code do?
# Answer:
#1. process is used for recording the number of loop and limiting the time of while loop
#so set progress = 0 is give a starting number of while loop
#2.whlie process<10 give the while loop a limitation to avoid endless loop
#3.process+=1 makes the value of process +1 after each while loop
#4.n = radint(1,100) give n a new value between 1 and 100
#5.print(n) prints n value when process value = 10
   
# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress<10:
	progress+=1
	n = randint(1,100)

print(n)
