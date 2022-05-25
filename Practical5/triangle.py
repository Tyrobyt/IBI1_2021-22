# triangle sequence = 1+2+...+n (0<=n<10, n is integer)
# set a to store the values of triangle sequence, set n to present the time of circle
# in circle 1, n=1, a=0
# change the value of a in each circle by a = a+n
# use while loop

a=1
n=1
for i in range(1,10):
 n=n+1
 a+=n
 print('the '+str(n)+'th triangle number is '+str(a))

