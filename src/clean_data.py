import pandas as pd

print("📂 Loading dataset...")  
df = pd.read_csv("data/PS_20174392719_1491204439457_log.csv")
print("✅ Dataset loaded!")     

# 1. Drop duplicate rows (if any)
df = df.drop_duplicates()

# 2. Convert categorical columns
df["type"] = df["type"].astype("category")
df["isFraud"] = df["isFraud"].astype("category")
df["isFlaggedFraud"] = df["isFlaggedFraud"].astype("category")

# 3. Drop columns that won't help high-level EDA
# These are ID-like columns we won't analyze for now
df = df.drop(columns=["nameOrig", "nameDest"])

# 4. Reset index after cleaning
df = df.reset_index(drop=True)

# 5. Save cleaned data
df.to_csv("data/cleaned_paysim.csv", index=False)

print("✅ Data cleaned and saved to 'data/cleaned_paysim.csv'")
