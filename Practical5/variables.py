a=19245301
b=4218520
c=271
d=b-c
# d = the rate of new cases in 2020
e=a-b
# e = the rate of new cases in 2021
if (d-e>0):
  print ("d>e, the rate of new cases in 2020 is greater than 2021")
elif (d-e==0):
  print ("d=e")
else:
  print ("d<e, the rate of new cases in 2021 is greater than 2020")

X="True"
Y="False"
#combine X and Y
W=X+Y
print (W)

