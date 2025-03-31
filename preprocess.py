import pandas as pd

# Load the dataset (update filename if needed)
df = pd.read_csv("data.csv", header=None)

# Add column headers
df.columns = [
    "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
    "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
    "hours-per-week", "native-country", "income"
]

# Remove rows with missing values marked as ' ?'
df_cleaned = df[
    (df["workclass"] != ' ?') &
    (df["occupation"] != ' ?') &
    (df["native-country"] != ' ?')
]

# Save the cleaned data
df_cleaned.to_csv("data_cleaned.csv", index=False)

print("Cleaned dataset saved as 'data_cleaned.csv'")
