import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'C:\Users\ABHISHEK\Desktop\Tools_Methods_Data_Analysis\annual_deforestation.csv')  # Make sure the file is in the same directory

# Define the list of selected country codes
selected_codes = ['BRA', 'IDN', 'PER', 'COL', 'BOL', 'MEX', 'PRY', 'MMR', 'IND']

# Filter data for the year 1990 and selected countries
filtered_1990 = df[
    (df['Code'].isin(selected_codes)) &
    (df['Year'] == 1990) &
    (df['Deforestation'].notna())
]

filtered_2015 = df[
    (df['Code'].isin(selected_codes)) &
    (df['Year'] == 2015) &
    (df['Deforestation'].notna())
]

# Plot histogram with density curve
plt.figure(figsize=(10, 6))
sns.histplot(filtered_1990['Deforestation'], bins=10, kde=True, color='forestgreen')

plt.title('Histogram and Density Plot of Deforestation in 1990', fontsize=18)
plt.xlabel('Annual Deforestation (Hectares)', fontsize=16)
plt.ylabel('Frequency / Density', fontsize=16)
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(filtered_2015['Deforestation'], bins=10, kde=True, color='forestgreen')

plt.title('Histogram and Density Plot of Deforestation in 2015', fontsize=18)
plt.xlabel('Annual Deforestation (Hectares)', fontsize=16)
plt.ylabel('Frequency / Density', fontsize=16)
plt.grid(True)
plt.tight_layout()
plt.show()