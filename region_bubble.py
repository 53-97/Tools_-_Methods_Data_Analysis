import csv
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
 
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

all_year_integer = list(map(int,all_year))

size = all_year_integer
fig = go.Figure(data=[go.Scatter(
    x=entity,
    # y=[100000, 200000, 300000, 400000, 500000, 600000],
    mode='markers',
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(200.**2),
        sizemin=4
    )
    
)])

fig.show()