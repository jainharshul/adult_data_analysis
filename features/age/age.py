import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("/Users/harshuljain/Desktop/adult_data_analysis/features/data_cleaned.csv")

# Remove accidental header rows and ensure 'age' is numeric
df = df[df["age"] != "age"]
df["age"] = df["age"].astype(int)

# Set visual style
sns.set(style="whitegrid")

# === 1. Histogram: Age Distribution by Income ===
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="age", hue="income", multiple="stack", bins=20)
plt.title("Age Distribution by Income")
plt.xlabel("Age")
plt.ylabel("Number of Individuals")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("age_distribution_by_income.png")
plt.show()

# === 2. Line Plot: Probability of Earning >50K by Age ===
# Create binary income column
df["income_binary"] = df["income"].apply(lambda x: 1 if x.strip() == ">50K" else 0)

# Group by age and calculate the mean (probability of earning >50K)
age_income_prob = df.groupby("age")["income_binary"].mean()

# Plot
plt.figure(figsize=(10, 6))
sns.lineplot(x=age_income_prob.index, y=age_income_prob.values)
plt.title("Probability of Earning >50K by Age")
plt.xlabel("Age")
plt.ylabel("P(Income > 50K)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("probability_income_over_50K_by_age.png")
plt.show()
