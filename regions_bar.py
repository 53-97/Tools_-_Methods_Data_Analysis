# importing the module
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

# for i in range(1,len(all_year)):
#     int(all_year[i]) = int(all_year[i])/1000000
#     str(all_year[i])

plt.bar(entity,all_year,color='Blue',width=0.5)

plt.xlabel("Region")
plt.ylabel("Population")
plt.title("Population by Region")
plt.show()
 
# printing lists
# print('Entity:', entity)
# print('Year:', year)
# print('All years:', all_year)