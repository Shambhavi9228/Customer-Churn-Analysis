import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("../data/cleaned_churn_data.csv")

# Churn Distribution
plt.figure(figsize=(6,4))
sns.countplot(x="Churn", data=df)

plt.title("Customer Churn Distribution")
plt.savefig("../results/churn_distribution.png")
plt.close()

# Contract Type Distribution
plt.figure(figsize=(8,5))
sns.countplot(x="Contract", hue="Churn", data=df)

plt.title("Contract Type vs Churn")
plt.xticks(rotation=15)
plt.savefig("../results/contract_vs_churn.png")
plt.close()

# Monthly Charges Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["MonthlyCharges"], bins=30)

plt.title("Monthly Charges Distribution")
plt.savefig("../results/monthly_charges_distribution.png")
plt.close()

print("Analysis graphs generated successfully!")