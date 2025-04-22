import csv
import numpy as np
import matplotlib.pyplot as plt
 
# open the file in read mode
filename = open(r'C:\Users\ABHISHEK\Desktop\Tools_Methods_Data_Analysis\annual_deforestation.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
coountry_code = ['BRA', 'IDN', 'PER', 'COL', 'BOL', 'MEX', 'PRY', 'MMR', 'IND', 'OWID_WRL']
 
# creating empty lists
entity = []
deforestation_1990 = []
deforestation_2015 = []
deforestation_2000 = []
deforestation_2010 = []
avg_deforestation_countries = []
 
# iterating over each row and append
# values to empty list
for col in file:
    if col['Code'] in coountry_code:
        entity.append(col['Code'])
        if col['Year'] == '1990':
            deforestation_1990.append(col['Deforestation'])
        elif col['Year'] == '2015':
            deforestation_2015.append(col['Deforestation'])
        elif col['Year'] == '2000':
            deforestation_2000.append(col['Deforestation'])
        elif col['Year'] == '2010':
            deforestation_2010.append(col['Deforestation'])


entity = list(dict.fromkeys(entity))
x = np.arange(10)
# y =  np.arange(0,80,20)
y1 = deforestation_1990
y2 = deforestation_2015
# print(entity)

y_1990 = list(map(int, y1))
y_2015 = list(map(int, y2))
# print(deforestation_1990)
# print(deforestation_2015)
# print(y_1990)
# print(y_2015)
width = 0.4
# print(deforestation_2000)
# print(deforestation_2010)

# plot bar
plt.bar(x-0.2, y_1990, width, color='cyan')
plt.bar(x+0.2, y_2015, width, color='green')
plt.xticks(x, ['BRA', 'IDN', 'PER', 'COL', 'BOL', 'MEX', 'PRY', 'MMR', 'IND', 'OWID_WRL'], fontsize = 16)
plt.xlabel("Regions", fontsize  = 18)
plt.ylabel("Deforestation (in 100,000 hectares)", fontsize = 18)
plt.legend(["1990", "2015"], fontsize = 18)
plt.show()