import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("/Users/harshuljain/Desktop/adult_data_analysis/features/data_cleaned.csv")

# Remove any rows where the value in the 'sex' column is 'sex' (accidental header row)
df = df[df["sex"] != "sex"]

# Set style
sns.set(style="whitegrid")

# === 1. Count Plot ===
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="sex", hue="income")
plt.title("Income Distribution by Sex")
plt.ylabel("Number of Individuals")
plt.xlabel("Sex")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("income_distribution_by_sex.png")
plt.show()

# === 2. Proportion Plot ===
# Calculate percentages
income_by_sex_percent = df.groupby("sex")["income"].value_counts(normalize=True).unstack() * 100

# Plot
income_by_sex_percent.plot(kind="bar", stacked=True, figsize=(8, 5))
plt.title("Proportion of Income Levels by Sex")
plt.ylabel("Percentage")
plt.xlabel("Sex")
plt.legend(title="Income")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("income_proportion_by_sex.png")
plt.show()
