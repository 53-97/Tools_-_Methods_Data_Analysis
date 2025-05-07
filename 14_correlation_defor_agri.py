import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
deforestation_df = pd.read_csv(r'C:\Users\ABHISHEK\Desktop\Tools_Methods_Data_Analysis\annual_deforestation.csv')
soybean_df = pd.read_csv(r'C:\Users\ABHISHEK\Desktop\Tools_Methods_Data_Analysis\soybean-production_countries.csv')

# Merge on 'Entity' (country) and 'Year'
merged_df = pd.merge(deforestation_df, soybean_df, on=["Year"], how="inner")

# Drop rows with missing values
merged_df = merged_df.dropna(subset=['Deforestation', 'Production (t)'])

# Rename for easier plotting
merged_df.rename(columns={'Production (t)': 'Production'}, inplace=True)


# Compute correlation
correlation = merged_df['Deforestation'].corr(merged_df['Production'])
print(f"Correlation between deforestation and soybean production: {correlation:.2f}")

# Plot
plt.figure(figsize=(10, 6))
sns.regplot(data=merged_df, x='Production', y='Deforestation', scatter_kws={'alpha':0.5})
plt.title("Correlation Between Deforestation and Soybean Production", fontsize = 18)
plt.xlabel("Soybean Production (tonnes)", fontsize = 16)
plt.ylabel("Deforestation (hectares)", fontsize = 16)
plt.grid(True)
plt.tight_layout()
plt.show()
