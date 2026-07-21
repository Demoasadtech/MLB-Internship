'''Mini Project

Iris Flower Clustering & Visualization

For this project, use the Iris Dataset available in Scikit-learn.

Your application should:

Load the Iris dataset.
Convert it into a Pandas DataFrame.
Explore the dataset.
Apply K-Means clustering.
Use the Elbow Method to select the optimal number of clusters.
Reduce the dataset to 2 dimensions using PCA.
Visualize:

  
Original data (using selected features)
K-Means clusters
PCA-transformed data
Briefly explain your observations:

  
How many clusters were formed?
Did the clusters represent the flower species well?
How did PCA help in visualization?'''

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
data=load_iris()                                 #load iris dataset 
print(data.keys())                               #Convert it into a Pandas DataFrame.
print(data.feature_names)                        #Explore the dataset.
x=data.data
df=pd.DataFrame(data.data,columns=data.feature_names)
original_dataset=df
print(df)
print(df.shape)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

scaler=StandardScaler()                 # Feature Scaling however feature dataset becomes on one scale
x_scaled=scaler.fit_transform(x)

wcss = []                                # Apply elbow method find best k value
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(x_scaled)
    wcss.append(model.inertia_)

#print(wcss)


plt.plot(range(1, 11), wcss, marker="o")    # find k value using elbow method and then scatter plot show
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.savefig("Day9/Generated Graphs/wcss.png")
plt.show()

model=KMeans(n_clusters=3,random_state=42)    # Apply K_MEAN Clustering Model
labels=model.fit_predict(x_scaled)

'''df["Cluster"]=labels
df["target"]=data.target
print(pd.crosstab(df["target"], df["Cluster"]))'''  # Crosstab method for comparising clusters and target values (Note : because i know target values  exist  label data but If we don't have labeled data, then this method cannot be used.'

pca=PCA(n_components=2)   # apply PCA CONVERT 4 DIMENSIONS INTO 2 DIMENSIONS
x_pca=pca.fit_transform(x_scaled)    
centers = pca.transform(model.cluster_centers_)

plt.figure(figsize=(8,6))    # scatter plot show similar data points and then show centroid using marks x

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
plt.savefig("Day9/Generated Graphs/pca.png")
plt.show()

'''Original data (using selected features)
K-Means clusters
PCA-transformed data
Briefly explain your observations:'''

print("Original Data ")    # original values  
print(df.head())
df["Clusters"]=labels      # clusters values
print(df[["Clusters"]].head())

pca_df = pd.DataFrame(     # print values after apply pca
    x_pca,
    columns=["PC1", "PC2"]
)
print(pca_df.head())

'''How many clusters were formed?
Did the clusters represent the flower species well?
How did PCA help in visualization?'''

#Answer

'''Three clusters were formed. Although the Iris dataset
is labeled and i am already know it contains three flower
species, I,m used the Elbow Method to determine the optimal
number of clusters instead of relying on the labels. The 
Elbow graph showed a clear bend at K = 3. After K = 3, the
WCSS decreased only slightly, indicating diminishing returns.
Therefore, K = 3 was selected as the optimal number of clusters.'''

#Answer
'''Yes, the clusters represented the flower species reasonably well.
Setosa was completely separated into one cluster.
Versicolor and Virginica had some overlap because their features are similar.
This is expected behavior for the Iris dataset.'''

#Answer
'''PCA reduced the dataset from 4 features to 2 principal components (PC1 and PC2).
This made it possible to display the data on a 2D scatter plot while preserving 
most of the important information (variance). As a result, the clusters became much
easier to visualize and interpret.'''
