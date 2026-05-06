import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
# Dataset
data = {
    "Income": [15, 20, 25, 30, 40, 50, 60, 70, 80, 90],
    "Spending": [10, 15, 20, 25, 38, 40, 56, 68, 70, 88]
}
df = pd.DataFrame(data)
# Features
X = df[["Income", "Spending"]]
# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Elbow Method
wcss = []
for i in range(1, 6):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 6), wcss)
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()
# Apply KMeans (K=3)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)
print(df)
print("\nCluster Labels:")
print(df["Cluster"])
# Plot clusters
plt.scatter(df["Income"], df["Spending"], c=df["Cluster"])
centers = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centers[:, 0], centers[:, 1], marker='X')
plt.xlabel("Income")
plt.ylabel("Spending")
plt.show()