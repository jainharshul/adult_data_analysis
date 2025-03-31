import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("/Users/harshuljain/Desktop/adult_data_analysis/features/data_cleaned.csv")

# Remove accidental header rows if present
df = df[df["education"] != "education"]

# Set plot style
sns.set(style="whitegrid")

# === 1. Count Plot: Income by Education ===
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="education", hue="income", order=df["education"].value_counts().index)
plt.title("Income Distribution by Education Level")
plt.ylabel("Number of Individuals")
plt.xlabel("Education Level")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("income_distribution_by_education.png")
plt.show()

# === 2. Proportion Plot: Income % by Education (Sorted by >50K %) ===
education_income_pct = df.groupby("education")["income"].value_counts(normalize=True).unstack() * 100

# Remove extra whitespace from column names
education_income_pct.columns = education_income_pct.columns.str.strip()

# Sort by >50K in descending order
education_income_pct = education_income_pct.sort_values(by=">50K", ascending=False)

# Plot
education_income_pct.plot(kind="bar", stacked=True, figsize=(12, 6))
plt.title("Proportion of Income Levels by Education (Sorted by >50K)")
plt.ylabel("Percentage")
plt.xlabel("Education Level")
plt.xticks(rotation=45, ha='right')
plt.legend(title="Income")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("income_proportion_by_education_sorted.png")
plt.show()

