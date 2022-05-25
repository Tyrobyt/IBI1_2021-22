#creat a list to store Rob's scores
Scorelist = [45, 36, 86, 57, 53, 92, 65, 45]
#sort the scorelist
Scorelist = sorted(Scorelist)
#print the sorted list
print(Scorelist)
#now draw the boxplot, first import the numpy and matplotlib
import matplotlib.pyplot as plt
import numpy as np
#set the value
plt.boxplot(Scorelist,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=True,
            showbox=True,
            showcaps=True,
            notch=False
            )
plt.xlabel("tests")
plt.ylabel("marks")
plt.show()
# then, I will calculate the average of Rob's scores
sum=sum(Scorelist)
avg=sum/8
# compare the average score and the pass line
if avg >= 60:
    print("Rob has passed this ICA!")
else:
    print("Rob has failed this ICA!")
