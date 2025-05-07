import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from matplotlib.backends.backend_pdf import PdfPages

# Set random seed for reproducibility
np.random.seed(42)

# Function to draw samples and generate CLT visuals
def clt_visuals(dist_name, data, sample_sizes=[10, 30, 100], num_samples=1000):
    fig_list = []

    for n in sample_sizes:
        sample_means = [
            np.mean(np.random.choice(data, size=n, replace=True))
            for _ in range(num_samples)
        ]

        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        # Histogram of sample means
        sns.histplot(sample_means, bins=30, kde=True, ax=axes[0], color="skyblue")
        axes[0].set_title(f'{dist_name} - Sample Means (n={n})')
        axes[0].set_xlabel('Sample Mean')
        axes[0].set_ylabel('Frequency')

        # Q-Q plot
        stats.probplot(sample_means, dist="norm", plot=axes[1])
        axes[1].set_title(f'Q-Q Plot of Sample Means (n={n})')

        fig.suptitle(f'Demonstrating CLT for {dist_name} Distribution (Sample Size = {n})', fontsize=14)
        fig.tight_layout(rect=[0, 0, 1, 0.95])
        fig_list.append(fig)

    return fig_list

# Generate non-normal distributions
exponential_data = np.random.exponential(scale=1.0, size=10000)
uniform_data = np.random.uniform(low=0, high=100, size=10000)

# Generate plots
exp_figs = clt_visuals("Exponential", exponential_data)
uni_figs = clt_visuals("Uniform", uniform_data)

# Save all figures to a single PDF
with PdfPages("CLT_Demonstration.pdf") as pdf:
    for fig in exp_figs + uni_figs:
        pdf.savefig(fig)
        plt.close(fig)

print("✅ PDF saved as 'CLT_Demonstration.pdf'")
