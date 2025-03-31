# Updated version with diagonal break marks for a more natural-looking y-axis break

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean the dataset
df = pd.read_csv("/Users/harshuljain/Desktop/adult_data_analysis/features/data_cleaned.csv")
df = df[(df["race"] != "race") & (df["education"] != "education")]
df["race"] = df["race"].str.strip()
df["education"] = df["education"].str.strip()
df["income"] = df["income"].str.strip()

# Keep only the top 6 education levels
top_education_levels = df["education"].value_counts().head(6).index
df_top_edu = df[df["education"].isin(top_education_levels)]

# Set style
sns.set(style="whitegrid")
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 10), sharex=True)

incomes = df_top_edu["income"].unique()
colors = sns.color_palette("tab10")

for i, income_cat in enumerate(incomes):
    ax_upper = axes[0, i]
    ax_lower = axes[1, i]

    # Prepare data
    plot_data = df_top_edu[df_top_edu["income"] == income_cat]
    counts = plot_data.groupby(["education", "race"]).size().unstack(fill_value=0).reindex(index=top_education_levels)

    # Plot upper chart
    counts.plot(kind="bar", stacked=True, ax=ax_upper, legend=False, color=colors)
    ax_upper.set_ylim(2000, counts.values.max() + 1000)
    ax_upper.spines['bottom'].set_visible(False)
    ax_upper.tick_params(labelbottom=False)
    ax_upper.set_title(f"Income: {income_cat}")

    # Plot lower chart
    counts.plot(kind="bar", stacked=True, ax=ax_lower, legend=(i == 1), color=colors)
    ax_lower.set_ylim(0, 500)
    ax_lower.spines['top'].set_visible(False)
    ax_lower.set_xlabel("Education Level")
    ax_lower.set_ylabel("Count")
    ax_lower.tick_params(axis='x', rotation=45)

    # Diagonal lines to indicate the break
    d = .015  # diagonal break size
    kwargs = dict(transform=ax_upper.transAxes, color='k', clip_on=False)
    ax_upper.plot((-d, +d), (-d, +d), **kwargs)
    ax_upper.plot((1 - d, 1 + d), (-d, +d), **kwargs)

    kwargs.update(transform=ax_lower.transAxes)
    ax_lower.plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax_lower.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

# Final adjustments
plt.suptitle("Race and Education Level by Income Group (Natural-Looking Broken Y-Axis)", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("race_education_vs_income_broken_axis_diagonal.png")
plt.show()
