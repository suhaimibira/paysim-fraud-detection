import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create the folder if it doesn't exist
os.makedirs("eda_visualizations", exist_ok=True)

# Load the cleaned data
df = pd.read_csv("data/cleaned_paysim.csv")

print("✅ Cleaned data loaded")
print(df.info())
print(df.describe())

# Fraud vs Non-Fraud count
plt.figure(figsize=(6,4))
sns.countplot(x='isFraud', data=df)
plt.title("Fraud vs Non-Fraud Transactions")
plt.xlabel("Is Fraud")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("eda_visualizations/fraud_vs_nonfraud.png")
plt.show()

# Transaction types
plt.figure(figsize=(8,4))
sns.countplot(x='type', data=df)
plt.title("Transaction Types")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("eda_visualizations/transaction_types.png")
plt.show()

# Fraud by transaction type
plt.figure(figsize=(8,4))
sns.countplot(x='type', hue='isFraud', data=df)
plt.title("Fraud by Transaction Type")
plt.xlabel("Type")
plt.ylabel("Count")
plt.legend(title="Is Fraud")
plt.tight_layout()
plt.savefig("eda_visualizations/fraud_by_type.png")
plt.show()
