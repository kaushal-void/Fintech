import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset
data = {
    "Age": [25, 30, 35, np.nan, 45, 100, 28],
    "Salary": [25000, 30000, np.nan, 40000, 50000, 1080000, 27000],
    "Experience": [1, 3, 5, 2, np.nan, 38, 2]
}

df = pd.DataFrame(data)

# Basic Info
print(df.info())
print(df.describe())
print("\nMissing Values:\n", df.isnull().sum())

# Fill missing values
df = df.fillna(df.mean(numeric_only=True))

# Remove outliers (IQR)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)

IQR = Q3 - Q1

df_clean = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

print("\nCleaned Data:\n", df_clean)

# Plots
plt.hist(df["Age"])
plt.title("Age Distribution")
plt.show()

plt.scatter(df["Age"], df["Salary"])
plt.title("Age vs Salary")
plt.show()

df.boxplot()
plt.title("Boxplot")
plt.show()