import csv
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Step 1: Load dataset
df = pd.read_csv(r'C:\Users\ABHISHEK\Desktop\Tools_Methods_Data_Analysis\world_cup_goals_1930_2022.csv', encoding='latin-1')

matches = ()
# Step 2: Calculate total goals and matches
total_goals = df['key_id'].__len__()
matches = df['match_id']
total_matches = list(dict.fromkeys(matches))
# print(matches)
# print(len(total_matches))
# print(total_goals)

# Step 3: Compute average goals per match (λ)
lambda_goals = total_goals / len(total_matches)

# Step 4: Estimate matches in 2026 (FIFA confirmed 104 matches)
matches_2026 = 64
expected_goals = lambda_goals * matches_2026

# Step 5: Poisson distribution - probabilities for range of possible goals
x = range(int(expected_goals - 50), int(expected_goals + 50))
y = poisson.pmf(x, mu=expected_goals)

# Step 6: Plot the Poisson distribution
plt.figure(figsize=(10, 6))
plt.bar(x, y, color='skyblue', edgecolor='black')
plt.title('Poisson Distribution of Goals in 2026 FIFA World Cup', fontsize = 18)
plt.xlabel('Number of Goals', fontsize = 16)
plt.ylabel('Probability', fontsize = 16)
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()
