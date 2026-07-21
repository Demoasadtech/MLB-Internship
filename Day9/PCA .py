'''
Apply K-Means clustering.
Use the Elbow Method to select the optimal number of clusters.
then apply PCA for visualization'''
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data=load_iris()
x=data.data
df=pd.DataFrame(data.data,columns=data.feature_names)
scaler=StandardScaler()
x_scaled=scaler.fit_transform(x)

#print(x_scaled)
wcss = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(x_scaled)
    wcss.append(model.inertia_)
#print(wcss)

pca=PCA(n_components=2)
x_pca=pca.fit_transform(x_scaled)  

model1=KMeans(n_clusters=3,random_state=42)  
labels=model1.fit_predict(x_scaled)
df["Cluster"]=labels   # before PCA
df["target"]=data.target
print("This values before applying PCA ")
print(pd.crosstab(df["target"], df["Cluster"]))

model2=KMeans(n_clusters=3,random_state=42)    # after PCA
labels1=model1.fit_predict(x_pca)
df["Cluster"]=labels1
df["target"]=data.target
print ("after applying PCA")
print(pd.crosstab(df["target"], df["Cluster"]))

centers = pca.transform(model.cluster_centers_)   # for visualization
plt.figure(figsize=(8,6))

plt.scatter(
    x_pca[:,0],
    x_pca[:,1],
    c=labels,
    cmap="viridis",
    s=60
)

plt.scatter(
    centers[:,0],
    centers[:,1],
    c="red",
    marker="X",
    s=250,
    label="Centroids"
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("K-Means Clustering with PCA")
plt.legend()

plt.show()