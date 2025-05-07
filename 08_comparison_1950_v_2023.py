import csv
import numpy as np
import matplotlib.pyplot as plt
 
# open the file in read mode
filename = open(r'C:\Users\ABHISHEK\Desktop\Tools_Methods_Data_Analysis\population_1950_v_2023.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
entity = []
population_1950 = []
population_2023 = []
 
# iterating over each row and append
# values to empty list
for col in file:
    entity.append(col['Entity'])
    population_1950.append(col['Population 1950 (in 100 million)'])
    population_2023.append(col['Population 2023 (in 100 million)'])

x = np.arange(8)
# y =  np.arange(0,80,20)
y1 = population_1950
y2 = population_2023
y_1950 = list(map(float, y1))
y_2023 = list(map(float, y2))
width = 0.4

plt.bar(x-0.2, y_1950, width, color='cyan')
plt.bar(x+0.2, y_2023, width, color='green')
plt.xticks(x, ['Oceania ', 'Northern America ', 'LAC ', 'Africa ', 'Americas ', 'Europe ', 'Asia ', 'World' ], fontsize = 16)
plt.xlabel("Regions", fontsize  = 18)
plt.ylabel("Population (in 100 million)", fontsize = 18)
plt.legend(["1950", "2023"], fontsize = 18)
plt.show()