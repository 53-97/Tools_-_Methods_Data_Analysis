import pandas as pd
import matplotlib.pyplot as plt

# Sample data structure based on the chart
data = {
    "Year": [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2023],
    "World": [2.5, 3.0, 3.7, 4.4, 5.3, 6.1, 6.9, 8.0],
    "Asia": [1.4, 1.7, 2.1, 2.6, 3.2, 3.8, 4.2, 4.8],
    "Europe": [0.55, 0.61, 0.67, 0.70, 0.72, 0.73, 0.74, 0.74],
    "Americas": [0.35, 0.44, 0.55, 0.69, 0.80, 0.89, 0.96, 1.0],
    "Africa": [0.24, 0.28, 0.36, 0.47, 0.63, 0.82, 1.04, 1.4],
    "Latin America and the Caribbean": [0.18, 0.22, 0.28, 0.36, 0.45, 0.52, 0.58, 0.66],
    "Northern America": [0.17, 0.20, 0.23, 0.26, 0.28, 0.31, 0.34, 0.37],
    "Oceania": [0.013, 0.016, 0.019, 0.022, 0.026, 0.030, 0.036, 0.043]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(14, 6))
regions = df.columns[1:]

for region in regions:
    plt.plot(df["Year"], df[region], label=region)

plt.title("World Population by Region (1950–2023)", fontsize=18)
plt.xlabel("Year", fontsize=16)
plt.ylabel("Population (in billions)", fontsize=16)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
