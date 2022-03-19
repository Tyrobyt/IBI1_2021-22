#p = the number of pizza piece, n = the number of cuts
#we have 64 people in IBI1 class
#aim: calculate the number of cut(n) to make the number of piece>=64
#using while loop and if 
# if the number < 64, then print the number of piece and cut
# if the number >=64, then print the number of piece and cut, and add the word to indicate that we get enough piece.

p=0
n=0
while p<64:
 p=(n**2+n+2)/2
 if(p>64):
     print 'when the number of cut =',n,', the number of piece =',p,'we get enough piece of pizza for each member!'
 else:
     print 'when the number cut =',n,', the number of piece =',p
     n+=1
     

