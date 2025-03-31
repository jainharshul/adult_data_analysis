import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("/Users/harshuljain/Desktop/adult_data_analysis/features/data_cleaned.csv")

# Remove accidental header rows
df = df[df["hours-per-week"] != "hours-per-week"]
df["hours-per-week"] = df["hours-per-week"].astype(int)

# Set style
sns.set(style="whitegrid")

# === 1. Grouped Bar Plot: Binned Hours vs Income Proportion ===

# Bin hours into defined ranges
bins = [0, 29, 39, 41, 49, 99]
labels = ["<30", "30–39", "40", "41–49", "50+"]
df["hours-binned"] = pd.cut(df["hours-per-week"], bins=bins, labels=labels, right=True)

# Calculate proportion of income groups per bin
binned_income_pct = df.groupby("hours-binned")["income"].value_counts(normalize=True).unstack() * 100
binned_income_pct.columns = binned_income_pct.columns.str.strip()

# Plot
binned_income_pct.plot(kind="bar", stacked=True, figsize=(10, 6))
plt.title("Proportion of Income Levels by Weekly Hours Worked")
plt.ylabel("Percentage")
plt.xlabel("Hours Worked per Week")
plt.xticks(rotation=0)
plt.legend(title="Income")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("proportion_income_by_hours_binned.png")
plt.show()
