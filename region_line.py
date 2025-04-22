import csv
import numpy as np
import matplotlib.pyplot as plt
 
# open the file in read mode
filename = open(r'C:\Users\ABHISHEK\Desktop\Tools_Methods_Data_Analysis\population_2023.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
entity = []
year = []
all_year = []
 
# iterating over each row and append
# values to empty list
for col in file:
    entity.append(col['Entity'])
    year.append(col['Year'])
    all_year.append(col['all years'])

# plotting the points 
plt.plot(entity,all_year)

# naming the x axis
plt.xlabel('Region')
# naming the y axis
plt.ylabel('Population')

# giving a title to my graph
plt.title('Population by Region')

# function to show the plot
plt.show()