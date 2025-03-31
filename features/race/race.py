import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("/Users/harshuljain/Desktop/adult_data_analysis/features/data_cleaned.csv")

# Remove accidental header rows if present
df = df[df["race"] != "race"]

# Set visual style
sns.set(style="whitegrid")

# === 1. Count Plot: Income by Race ===
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x="race", hue="income", order=df["race"].value_counts().index)
plt.title("Income Distribution by Race")
plt.ylabel("Number of Individuals")
plt.xlabel("Race")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("income_distribution_by_race.png")
plt.show()

# === 2. Proportion Plot: Income % by Race (Sorted by >50K) ===
race_income_pct = df.groupby("race")["income"].value_counts(normalize=True).unstack() * 100
race_income_pct.columns = race_income_pct.columns.str.strip()
race_income_pct = race_income_pct.sort_values(by=">50K", ascending=False)

# Plot
race_income_pct.plot(kind="bar", stacked=True, figsize=(10, 5))
plt.title("Proportion of Income Levels by Race (Sorted by >50K)")
plt.ylabel("Percentage")
plt.xlabel("Race")
plt.xticks(rotation=45, ha='right')
plt.legend(title="Income")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("income_proportion_by_race_sorted.png")
plt.show()
