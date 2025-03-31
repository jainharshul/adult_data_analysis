import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("/Users/harshuljain/Desktop/adult_data_analysis/features/data_cleaned.csv")

# Remove any accidental header rows
df = df[df["occupation"] != "occupation"]

# Set visual style
sns.set(style="whitegrid")

# === 1. Count Plot: Income by Occupation ===
plt.figure(figsize=(14, 6))
sns.countplot(data=df, x="occupation", hue="income", order=df["occupation"].value_counts().index)
plt.title("Income Distribution by Occupation")
plt.ylabel("Number of Individuals")
plt.xlabel("Occupation")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("income_distribution_by_occupation.png")
plt.show()

# === 2. Proportion Plot: Income % by Occupation (Sorted by >50K) ===
occupation_income_pct = df.groupby("occupation")["income"].value_counts(normalize=True).unstack() * 100
occupation_income_pct.columns = occupation_income_pct.columns.str.strip()
occupation_income_pct = occupation_income_pct.sort_values(by=">50K", ascending=False)

# Plot
occupation_income_pct.plot(kind="bar", stacked=True, figsize=(14, 6))
plt.title("Proportion of Income Levels by Occupation (Sorted by >50K)")
plt.ylabel("Percentage")
plt.xlabel("Occupation")
plt.xticks(rotation=45, ha='right')
plt.legend(title="Income")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("income_proportion_by_occupation_sorted.png")
plt.show()
