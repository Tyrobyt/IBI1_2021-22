import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. import the data from full_data(2).csv file works
os.chdir("C:/Users/Tyrobyt/Desktop/Practical7")
covid_data=pd.read_csv("full_data(2).csv")

# 2.  show the first and third columns from row 10-20(inclusive)
# note: we should write 10:21 to include row 20
print(covid_data.iloc[10:21,1:3:2])

# 3. show the "total_cases" for all rows corresponding to Afghanistan through a Boolean (let covid_data["location"=="Afghanistan")
# loc[] was used to fetch the data together with Boolean
print(covid_data.loc[covid_data["location"]=="Afghanistan","total_cases"])

# 4. compute the mean number of new cases and new deaths in China
# First, create a variable to store the new_cases and new_deaths in China
cases_deaths=covid_data.loc[covid_data["location"]=="China",["new_cases","new_deaths"]]
# Then, use "describe()" function to get the mean number and other datas of cases_death
print(cases_deaths.describe())

# 5. create a boxplot for new_cases and new_deaths in China.
# the command in last week lecture was used
#let x = cases_deaths, and print two kind of data in same box plot
plt.boxplot(x= cases_deaths,
            labels=["case","death"],
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=True,
            showbox=True,
            showfliers=True,
            notch=False
            )
plt.ylabel("number")
plt.title("Comparing the new cases and new deaths in China")
plt.show()

# 6. plot bothe new cases and new deaths in China overtime.
# create china_dates and china_new_cases
china_dates=covid_data.loc[covid_data["location"]=="China","date"]
china_new_cases=covid_data.loc[covid_data["location"]=="China","new_cases"]
china_new_deaths=covid_data.loc[covid_data["location"]=="China","new_deaths"]
# After tried ''b+','bo','r+', I know that "b" means the color of plot is blue, and 'r' means the color is red; "+" means the pattern of point is "+", while the "o" means the pattern of point is a little dot
# now make a plot comparing the new cases and new deaths in china, I choose ''bo'' and ''ro'' to make plot looks nicer
plt.plot(china_dates,china_new_cases,'bo')
plt.plot(china_dates,china_new_deaths,'ro')
# use the command from practical7 to make the x axis look nicer
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
# the function "plt.xticks() is to modify the coordinates on the x-axis
# the iloc[0:len(china_dates):4] means take a date from every 4 date
# the rotation = -90 means turn the coordinates on x-axis 90°， “-” means Counter clockwise
plt.xlabel("date")
plt.ylabel("number")
plt.title("New cases and new deaths in China")
plt.show()

# 7. Question: how have new cases and total cases developed over time in Spain?
# create Spain_dates, Spain_new_cases, and Spain_total_cases
Spain_dates=covid_data.loc[covid_data["location"]=="Spain","date"]
Spain_new_cases=covid_data.loc[covid_data["location"]=="Spain","new_cases"]
Spain_total_cases=covid_data.loc[covid_data["location"]=="Spain","total_cases"]
# then, use them to draw a plot, the red dot represents the new cases while the blue dot represents total cases
plt.plot(Spain_dates,Spain_total_cases,'bo')
plt.plot(Spain_dates,Spain_new_cases,'ro')
# modify the coordinates on x axis and y axis
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):4],rotation=-90)
plt.xlabel("date")
plt.ylabel("number")
plt.title("Total cases and new cases in Spain")
plt.show()
