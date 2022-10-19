import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Part 1

#1.
f1 = pd.read_csv('passengerData.csv')

f2 = pd.read_excel('ticketPrices.xlsx')

#2.
df = pd.merge(f1, f2, on='TicketType')
print(df)


# 3.: printing rows of passengers whos's age is above the mean of this dataset 
print(df[df.Age >= (df.Age.max()-df.Age.min())/2])

#4.

plt.scatter(df.Age, df.Fare)
plt.show()

#5.

df2 = df[(df.Age >= 40) & (df.Age <= 50) & (df.Sex == 'female') & (df.Fare >= 40)]
print(df2)


# Part 2

#1.
f3 = pd.read_csv('titanicSurvival_m.csv')

#2.
print(f3.isna().sum())

#3.
print(f3.describe())

#4.
f3['Age'] = f3['Age'].fillna(0)
f3['Fare'] = f3['Fare'].fillna(0)

#5.
f3['Age'] = f3['Age'].fillna(f3['Age'].mean())
f3['Fare'] = f3['Fare'].fillna(f3['Fare'].mean())


# Part 3

f4 = pd.read_csv('TB_burden_countries_2014-09-29.csv')
f4 = f4.fillna(0)
f4_log = np.log(f4)
print(f4_log)
