# Day-9: K-Means Clustering & Principal Component Analysis (PCA)

## Objective

The objective of this project is to understand Unsupervised Learning by applying K-Means Clustering and Principal Component Analysis (PCA) on the Iris dataset. The project focuses on grouping similar data points, selecting the optimal number of clusters using the Elbow Method, and visualizing high-dimensional data in two dimensions.

---

## Topics Covered

- Unsupervised Learning
- Clustering
- K-Means Clustering
- Choosing the Value of K
- Elbow Method
- Cluster Visualization
- Principal Component Analysis (PCA)
- Dimensionality Reduction
- Data Visualization
- Real-World Applications of Clustering

---

## Dataset

**Dataset:** Iris Dataset (Built into Scikit-learn)

Features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Target Classes:

- Setosa
- Versicolor
- Virginica

---

## Project Workflow

1. Load the Iris dataset.
2. Convert the dataset into a Pandas DataFrame.
3. Explore the dataset.
4. Standardize the features using StandardScaler.
5. Apply the Elbow Method to determine the optimal number of clusters.
6. Train the K-Means clustering model.
7. Visualize the clusters.
8. Apply PCA to reduce the dataset from four dimensions to two principal components.
9. Visualize the PCA-transformed data.
10. Compare the clustering results with the PCA visualization.

---

## What is Clustering?

Clustering is an Unsupervised Machine Learning technique that groups similar data points together without using labeled data. Objects within the same cluster are more similar to each other than to objects in other clusters.

---

## What is PCA?

Principal Component Analysis (PCA) is a dimensionality reduction technique that transforms high-dimensional data into a smaller number of principal components while preserving most of the important information. PCA makes complex datasets easier to visualize and analyze.

---

## How was the Best Value of K Determined?

The Elbow Method was used to determine the optimal number of clusters.

The Within-Cluster Sum of Squares (WCSS) was calculated for different values of K. The Elbow graph showed a clear bend at **K = 3**. After this point, the decrease in WCSS became gradual, indicating that adding more clusters did not significantly improve the clustering performance.

Therefore, **K = 3** was selected as the optimal number of clusters.

---

## Observations

- Three clusters were formed by the K-Means algorithm.
- The Setosa flowers were clearly separated into one cluster.
- Versicolor and Virginica showed slight overlap because their features are similar.
- PCA reduced the dataset from four features to two principal components.
- PCA made the clusters much easier to visualize in a two-dimensional scatter plot.

---

## Insights Gained

- K-Means can effectively group similar observations without using labels.
- The Elbow Method is useful for selecting an appropriate number of clusters.
- PCA simplifies high-dimensional datasets while preserving most of the important information.
- Combining K-Means with PCA provides better visualization and understanding of cluster structures.

---

## Files Included

- Dataset Exploration.py
- K-Means Clustering.py
- PCA.py
- Iris Flower Clustering & Visualization.py / Notebook
- Generated Graphs / Folder
- README.md
- requirements.txt

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---

## Conclusion

This project demonstrated how K-Means Clustering can group similar data points and how PCA can reduce dimensionality for effective visualization. The Elbow Method identified **K = 3** as the optimal number of clusters, which closely matched the three species in the Iris dataset. PCA further improved the interpretation of the clustering results by representing the data in two dimensions.

---

## Author

**Muhammad Asad Ali**