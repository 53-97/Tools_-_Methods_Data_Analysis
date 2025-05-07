import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from matplotlib.backends.backend_pdf import PdfPages

np.random.seed(42)

# Generate distributions
exponential_data = np.random.exponential(scale=1.0, size=10000)
uniform_data = np.random.uniform(low=0, high=100, size=10000)

def clt_visuals(dist_name, data, sample_sizes=[10, 30, 100, 300], num_samples=1000):
    fig_list = []
    population_mean = np.mean(data)

    for n in sample_sizes:
        sample_means = [
            np.mean(np.random.choice(data, size=n, replace=True))
            for _ in range(num_samples)
        ]
        sample_means = np.array(sample_means)
        mean_of_samples = np.mean(sample_means)
        std_of_samples = np.std(sample_means)
        z_score = (mean_of_samples - population_mean) / std_of_samples

        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        # Histogram of sample means
        if dist_name == 'Exponential':
            sns.histplot(sample_means, bins=30, kde=True, ax=axes[0], color="orange")
            axes[0].set_title(f'{dist_name} - Sample Means (n={n})')
            axes[0].set_xlabel('Sample Mean')
            axes[0].set_ylabel('Frequency')
            axes[0].text(0.95, 0.95, 
                        f'Population μ = {population_mean:.2f}\n'
                        f'Sample μ = {mean_of_samples:.2f}\n'
                        f'σ = {std_of_samples:.2f}\n'
                        f'Z = {z_score:.2f}',
                        transform=axes[0].transAxes,
                        verticalalignment='top',
                        horizontalalignment='right',
                        bbox=dict(boxstyle="round,pad=0.5", facecolor='white', alpha=0.7))
        
        elif dist_name == 'Uniform':
            sns.histplot(sample_means, bins=30, kde=True, ax=axes[0], color="green")
            axes[0].set_title(f'{dist_name} - Sample Means (n={n})')
            axes[0].set_xlabel('Sample Mean')
            axes[0].set_ylabel('Frequency')
            axes[0].text(0.95, 0.95, 
                        f'Population μ = {population_mean:.2f}\n'
                        f'Sample μ = {mean_of_samples:.2f}\n'
                        f'σ = {std_of_samples:.2f}\n'
                        f'Z = {z_score:.2f}',
                        transform=axes[0].transAxes,
                        verticalalignment='top',
                        horizontalalignment='right',
                        bbox=dict(boxstyle="round,pad=0.5", facecolor='white', alpha=0.7))

        # Q-Q plot
        stats.probplot(sample_means, dist="norm", plot=axes[1])
        axes[1].set_title(f'Q-Q Plot of Sample Means (n={n})')

        fig.suptitle(f'Demonstrating CLT for {dist_name} (Sample Size = {n})', fontsize=14)
        fig.tight_layout(rect=[0, 0, 1, 0.95])
        fig_list.append(fig)

    return fig_list

# === Raw Dataset Visuals ===
fig_raw, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(exponential_data, bins=30, kde=True, ax=axes[0], color='orange')
axes[0].set_title("Raw Data: Exponential Distribution")
axes[0].set_xlabel("Value")
axes[0].set_ylabel("Frequency")

sns.histplot(uniform_data, bins=30, kde=True, ax=axes[1], color='green')
axes[1].set_title("Raw Data: Uniform Distribution")
axes[1].set_xlabel("Value")
axes[1].set_ylabel("Frequency")

fig_raw.tight_layout()

# === Q-Q Plot Between Exponential and Uniform ===
min_len = min(len(exponential_data), len(uniform_data))
sorted_exp = np.sort(exponential_data[:min_len])
sorted_uni = np.sort(uniform_data[:min_len])

fig_qq = plt.figure(figsize=(6, 6))
plt.plot(sorted_exp, sorted_uni, marker='o', linestyle='', markersize=2)
plt.plot([sorted_exp.min(), sorted_exp.max()],
         [sorted_exp.min(), sorted_exp.max()],
         'r--', label='y = x')
plt.xlabel('Quantiles of Exponential')
plt.ylabel('Quantiles of Uniform')
plt.title('Q-Q Plot: Exponential vs Uniform')
plt.legend()
plt.grid(True)

# === CLT Visuals ===
exp_figs = clt_visuals("Exponential", exponential_data)
uni_figs = clt_visuals("Uniform", uniform_data)

# === Save to PDF ===
with PdfPages("CLT_Demonstration_With_Stats_3.pdf") as pdf:
    pdf.savefig(fig_raw)
    pdf.savefig(fig_qq)
    for fig in exp_figs + uni_figs:
        pdf.savefig(fig)
        plt.close(fig)

print("✅ PDF saved as 'CLT_Demonstration_With_Stats_3.pdf'")
