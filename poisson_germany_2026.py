import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Step 1: Load data
df = pd.read_csv(r'C:\Users\ABHISHEK\Desktop\Tools_Methods_Data_Analysis\world_cup_goals_1930_2022.csv', encoding='latin-1')

# Step 2: Filter data for Germany
germany_df = df[df['team_name'] == 'Germany']

# Step 3: Compute total goals and matches played by Germany
matches = ()
# Step 2: Calculate total goals and matches
total_goals = df['key_id'].__len__()
matches = df['match_id']
total_matches = list(dict.fromkeys(matches))

# Step 4: Calculate average goals per match (λ)
lambda_germany = total_goals / len(total_matches)

# Step 5: Estimate total goals in 2026 (e.g., 7 matches)
matches_2026 = 7
expected_goals = lambda_germany * matches_2026

# Step 6: Poisson distribution
x = range(int(expected_goals - 5), int(expected_goals + 10))
y = poisson.pmf(x, mu=expected_goals)

# Step 7: Plot
plt.figure(figsize=(10, 6))
plt.bar(x, y, color='mediumseagreen', edgecolor='black')
plt.title('Poisson Prediction: Germany Goals in 2026 World Cup', fontsize = 18)
plt.xlabel('Number of Goals', fontsize = 16)
plt.ylabel('Probability', fontsize = 16)
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()
