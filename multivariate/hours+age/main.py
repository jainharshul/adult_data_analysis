import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load and clean the dataset
df = pd.read_csv("/Users/harshuljain/Desktop/adult_data_analysis/features/data_cleaned.csv")
df = df[(df["age"] != "age") & (df["hours-per-week"] != "hours-per-week") & (df["income"] != "income")]
df["age"] = df["age"].astype(int)
df["hours-per-week"] = df["hours-per-week"].astype(int)
df["income"] = df["income"].str.strip()

# Bin age and hours into groups
df["age_bin"] = pd.cut(df["age"], bins=np.arange(10, 81, 10))  # 10–80 in 10-year bins
df["hours_bin"] = pd.cut(df["hours-per-week"], bins=np.arange(0, 81, 10))  # 0–80 in 10-hour bins

# Group and count combinations
heatmap_counts = df.groupby(["income", "age_bin", "hours_bin"]).size().reset_index(name="count")

# Create pivot tables for each income group
pivot_low = heatmap_counts[heatmap_counts["income"] == "<=50K"].pivot(index="hours_bin", columns="age_bin", values="count")
pivot_high = heatmap_counts[heatmap_counts["income"] == ">50K"].pivot(index="hours_bin", columns="age_bin", values="count")

# Plot heatmaps
sns.set(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

# <=50K Heatmap
sns.heatmap(pivot_low, annot=True, fmt=".0f", cmap="Blues", ax=axes[0])
axes[0].set_title("<=50K Income")
axes[0].set_xlabel("Age Group")
axes[0].set_ylabel("Hours Worked (Grouped)")

# >50K Heatmap
sns.heatmap(pivot_high, annot=True, fmt=".0f", cmap="Greens", ax=axes[1])
axes[1].set_title(">50K Income")
axes[1].set_xlabel("Age Group")
axes[1].set_ylabel("")

# Final formatting
plt.suptitle("Grouped Count Heatmap of Age vs Hours Worked per Week by Income", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("grouped_count_heatmap_age_hours_income.png")
plt.show()
