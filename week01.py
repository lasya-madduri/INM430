import csv     # imports the csv module
import sys      # imports the sys module
import numpy as np
import matplotlib.pyplot as plt

f = open('TB_burden_countries_2014-09-29.csv') # opens the csv file
    

# Part-1

acc = 0
rows = 0
for row in csv.reader(f):
    rows += 1
    try:
        float(row[11])
        acc += float(row[11]) 
    except ValueError:
        acc += 0
    

average = acc/rows
print("Average is: ", average)
    

# Part-2



#1.
print(np.arange(5,16))

#2.
print(np.linspace(0, 23, 7))

#3.
uniform = (np.random.uniform(low=-1.0, high=1.0, size=10))
print(uniform)

#4.
x = np.arange(0,1,0.1)
y = uniform
plt.plot(x,y)

#5.
random_array1 = np.random.randint(1,100,size=10, dtype=int)
random_array2 = np.random.randint(1,100,size=10, dtype=int)

result = 0.0

for i in range(10):
    result += (random_array1[i] - random_array2[i]) ** 2

print(np.sqrt(result))

