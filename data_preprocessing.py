import pandas as pd

# Load dataset
df = pd.read_csv("../data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Remove missing values
df = df.dropna()

print("\nDataset Shape After Cleaning:")
print(df.shape)

# Save cleaned dataset
df.to_csv("../data/cleaned_churn_data.csv", index=False)

print("\nCleaned dataset saved successfully!")