# Re-import necessary packages after execution state reset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset again
df = pd.read_csv("/Users/harshuljain/Desktop/adult_data_analysis/features/data_cleaned.csv")

# Remove accidental header rows if present
df = df[df["marital-status"] != "marital-status"]

# Set visual style
sns.set(style="whitegrid")

# === 1. Count Plot: Income by Marital Status ===
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="marital-status", hue="income", order=df["marital-status"].value_counts().index)
plt.title("Income Distribution by Marital Status")
plt.ylabel("Number of Individuals")
plt.xlabel("Marital Status")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("income_distribution_by_marital_status.png")
plt.show()

# === 2. Proportion Plot: Income % by Marital Status (Sorted by >50K) ===
marital_income_pct = df.groupby("marital-status")["income"].value_counts(normalize=True).unstack() * 100
marital_income_pct.columns = marital_income_pct.columns.str.strip()
marital_income_pct = marital_income_pct.sort_values(by=">50K", ascending=False)

# Plot
marital_income_pct.plot(kind="bar", stacked=True, figsize=(12, 6))
plt.title("Proportion of Income Levels by Marital Status (Sorted by >50K)")
plt.ylabel("Percentage")
plt.xlabel("Marital Status")
plt.xticks(rotation=45, ha='right')
plt.legend(title="Income")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("income_proportion_by_marital_status_sorted.png")
plt.show()
