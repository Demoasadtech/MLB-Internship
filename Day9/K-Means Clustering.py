'''
Apply K-Means clustering.
Use the Elbow Method to select the optimal number of clusters.'''
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
data=load_iris()
x=data.data
df=pd.DataFrame(data.data,columns=data.feature_names)
scaler=StandardScaler()           #feature scaling
x_scaled=scaler.fit_transform(x)
#print(x_scaled)
wcss = []
for k in range(1, 11):              # find k value using elbow method and then scatter plot show
    plt.xlabel("Number of Clusters")
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(x_scaled)
    wcss.append(model.inertia_)
#print(wcss)


plt.plot(range(1, 11), wcss, marker="o")   # show visualization of elbow method
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.savefig("Day9/Generated Graphs/wcss.png")
plt.show()

model=KMeans(n_clusters=3,random_state=42)
labels=model.fit_predict(x_scaled)
df["Cluster"]=labels
df["target"]=data.target
print(pd.crosstab(df["target"], df["Cluster"]))