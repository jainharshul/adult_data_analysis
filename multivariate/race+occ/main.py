import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean dataset
df = pd.read_csv("/Users/harshuljain/Desktop/adult_data_analysis/features/data_cleaned.csv")
df = df[(df["occupation"] != "occupation") & (df["race"] != "race") & (df["income"] != "income")]
df["occupation"] = df["occupation"].str.strip()
df["race"] = df["race"].str.strip()
df["income"] = df["income"].str.strip()

# Group by income, occupation, and race
race_occ_group = df.groupby(["income", "occupation", "race"]).size().reset_index(name="count")

# Calculate proportions within each income + occupation group
race_occ_group["Total"] = race_occ_group.groupby(["income", "occupation"])["count"].transform("sum")
race_occ_group["Proportion"] = race_occ_group["count"] / race_occ_group["Total"]

# Split into two income groups
df_low_income = race_occ_group[race_occ_group["income"] == "<=50K"]
df_high_income = race_occ_group[race_occ_group["income"] == ">50K"]

# Get sorted list of occupations
occupation_sorted = sorted(df["occupation"].dropna().unique())

# Set visual style
sns.set(style="whitegrid")

# === PLOT 1: <=50K Income ===
plt.figure(figsize=(10, 10))
sns.barplot(
    data=df_low_income,
    x="Proportion",
    y="occupation",
    hue="race",
    order=occupation_sorted,
    palette="muted"
)
plt.title("Race Distribution by Occupation (<=50K Income)")
plt.xlabel("Proportion")
plt.ylabel("Occupation")
plt.legend(title="Race", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("race_by_occupation_low_income.png")
plt.show()

# === PLOT 2: >50K Income ===
plt.figure(figsize=(10, 10))
sns.barplot(
    data=df_high_income,
    x="Proportion",
    y="occupation",
    hue="race",
    order=occupation_sorted,
    palette="muted"
)
plt.title("Race Distribution by Occupation (>50K Income)")
plt.xlabel("Proportion")
plt.ylabel("Occupation")
plt.legend(title="Race", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("race_by_occupation_high_income.png")
plt.show()
