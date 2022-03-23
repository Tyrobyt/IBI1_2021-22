#creat a dictionary to store the parental age and the risk
#of offspring with congen heart disease
dict = {'age:risk':
          {
              '30':'1.03',
          '35':'1.07',
          '40':'1.11',
          '45':'1.17',
          '50':'1.23',
          '55':'1.32',
          '60':'1.42',
          '65':'1.55',
          '70':'1.72',
          '75':'1.94',
          }}
# now, print the dictionary we created
print('parental_age:CHD_risk=',dict['age:risk'])
# then, draw tghe scatter plot
import matplotlib.pyplot as plt
import numpy as np
#creat two seperate list for x and y
x=np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75])
y=np.array([1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94])
#creat and print a scatter plot
plt.xlabel("age")
plt.ylabel("risk of CHD")
plt.scatter(x,y,marker='o')
plt.show()
