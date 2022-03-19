#p = the number of pizza piece, n = the number of cuts
#we have 64 people in IBI1 class
#aim: calculate the number of cut(n) to make 64 piece(p=64)

p=0
n=0
while p<64:
 p=(n**2+n+2)/2
 if(p>64):
     print n
 else:
     n+=1

