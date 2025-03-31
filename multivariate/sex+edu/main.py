import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean the dataset
df = pd.read_csv("/Users/harshuljain/Desktop/adult_data_analysis/features/data_cleaned.csv")
df = df[(df["sex"] != "sex") & (df["education"] != "education")]
df["education"] = df["education"].str.strip()
df["sex"] = df["sex"].str.strip()
df["income"] = df["income"].str.strip()

# Logical order of education levels
logical_order = [
    "Preschool", "1st-4th", "5th-6th", "7th-8th", "9th", "10th", "11th", "12th",
    "HS-grad", "Some-college", "Assoc-voc", "Assoc-acdm", "Bachelors",
    "Masters", "Prof-school", "Doctorate"
]

# Filter and reorder education levels
edu_in_data = df["education"].unique()
all_education_levels = [edu for edu in logical_order if edu in edu_in_data]
df_all_edu = df[df["education"].isin(all_education_levels)]

# Set visual style
sns.set(style="whitegrid")

# Create subplot layout
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 10), sharex=True)
incomes = df_all_edu["income"].unique()
colors = sns.color_palette("Set2")

for i, income_cat in enumerate(incomes):
    ax_upper = axes[0, i]
    ax_lower = axes[1, i]

    # Group and reorder counts
    plot_data = df_all_edu[df_all_edu["income"] == income_cat]
    counts = plot_data.groupby(["education", "sex"]).size().unstack(fill_value=0)
    counts = counts.reindex(index=all_education_levels).fillna(0)

    if not counts.empty:
        # Upper plot (zoomed out)
        counts.plot(kind="bar", stacked=True, ax=ax_upper, legend=False, color=colors)
        ax_upper.set_ylim(2000, counts.values.max() + 1000)
        ax_upper.spines['bottom'].set_visible(False)
        ax_upper.tick_params(labelbottom=False)
        ax_upper.set_title(f"Income: {income_cat}")

        # Lower plot (zoomed in)
        counts.plot(kind="bar", stacked=True, ax=ax_lower, legend=(i == 1), color=colors)
        ax_lower.set_ylim(0, 500)
        ax_lower.spines['top'].set_visible(False)
        ax_lower.set_xlabel("Education Level")
        ax_lower.set_ylabel("Count")
        ax_lower.tick_params(axis='x', rotation=45)

        # Add diagonal break lines
        d = .015
        kwargs = dict(transform=ax_upper.transAxes, color='k', clip_on=False)
        ax_upper.plot((-d, +d), (-d, +d), **kwargs)
        ax_upper.plot((1 - d, 1 + d), (-d, +d), **kwargs)

        kwargs.update(transform=ax_lower.transAxes)
        ax_lower.plot((-d, +d), (1 - d, 1 + d), **kwargs)
        ax_lower.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)
    else:
        ax_upper.set_visible(False)
        ax_lower.set_visible(False)

# Final formatting
plt.suptitle("Education Level and Sex by Income Group (Logically Ordered + Broken Y-Axis)", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("education_sex_vs_income_broken_axis_sorted.png")
plt.show()
