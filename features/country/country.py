import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("/Users/harshuljain/Desktop/adult_data_analysis/features/data_cleaned.csv")

# Remove accidental header rows
df = df[df["native-country"] != "native-country"]

# Set visual style
sns.set(style="whitegrid")

# === 1. Proportion Plot: Income % by Native Country (Sorted by >50K, Top 10 Only) ===
country_income_pct = df.groupby("native-country")["income"].value_counts(normalize=True).unstack() * 100
country_income_pct.columns = country_income_pct.columns.str.strip()

# Filter and sort
country_income_pct_top10 = country_income_pct.loc[top_countries]
country_income_pct_top10 = country_income_pct_top10.sort_values(by=">50K", ascending=False)

# Plot
country_income_pct_top10.plot(kind="bar", stacked=True, figsize=(12, 6))
plt.title("Proportion of Income Levels by Native Country (Top 10 Sorted by >50K)")
plt.ylabel("Percentage")
plt.xlabel("Native Country")
plt.xticks(rotation=45, ha='right')
plt.legend(title="Income")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("income_proportion_by_native_country_top10_sorted.png")
plt.show()
