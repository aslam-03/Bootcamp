Task 1: Basic K-Means
- Load a 2D dataset (Income vs. Spending Score).
- Apply K-Means to group data into k clusters.
- Visualize clusters and centroids using matplotlib.
  
Output: A scatter plot with data points grouped into clusters.

Task 2: Centroid Selection
- Test how initial centroid selection affects results.
- Compare random centroids vs. K-Means++ initialization.
- Observe how different starting points lead to different clusters.
  
Output: Two different cluster visualizations showing the impact of initialization.

Task 3: K-Means on a Real Dataset (Iris Data)
- Use the Iris dataset (without labels).
- Normalize the features for better clustering.
- Apply K-Means (k=3) and compare clusters with real species.
  
Output: Clusters of flowers, compared with actual labels.

Task 4: Finding the Best K (Elbow Method)
- Test different values of k (1 to 10).
- Calculate WCSS (Within-Cluster Sum of Squares) for each k.
- Plot an Elbow Curve to find the best k.
  
Output: A graph showing the optimal k where the curve bends.

Task 5: Cluster Analysis
- Analyze clusters from Task 3 or Task 4.
- Find patterns (e.g., "Cluster 1 = High spenders, Cluster 2 = Low income").
- Generate a summary report on the cluster characteristics.
  
Output: A text report explaining the patterns found in clusters.

Task 6: Handling High-Dimensional Data (Using PCA)
- Some datasets have too many features, making clustering hard.
- Apply PCA (Principal Component Analysis) to reduce dimensions.
- Perform K-Means on the reduced dataset.
- Visualize results in 2D or 3D scatter plots.
  
Output: Clusters in a lower-dimensional space for better interpretation.
