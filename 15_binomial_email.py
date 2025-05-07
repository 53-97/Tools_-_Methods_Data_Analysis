import pandas as pd
from scipy.stats import binom
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"C:\Users\ABHISHEK\Desktop\Tools_Methods_Data_Analysis\emails.csv")  # Make sure the file is in the same directory

# Calculate total emails and number of spam emails
total_emails = len(df)
total_spam = df['spam'].sum()

# Estimate probability of an email being spam
p_spam = total_spam / total_emails

# Assume you receive 20 emails per day
n = 20

# Generate probabilities for getting 0 to 20 spam emails
k_values = range(0, n + 1)
probabilities = [binom.pmf(k, n, p_spam) for k in k_values]

# Plotting the binomial distribution
plt.figure(figsize=(10, 6))
plt.bar(k_values, probabilities, color='tomato', edgecolor='black')
plt.title('Probability Distribution of Spam Emails per Day (n = 20)')
plt.xlabel('Number of Spam Emails')
plt.ylabel('Probability')
plt.xticks(k_values)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
