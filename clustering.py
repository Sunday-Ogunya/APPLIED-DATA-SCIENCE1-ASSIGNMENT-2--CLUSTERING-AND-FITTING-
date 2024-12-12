import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def perform_clustering(data, n_clusters=3):
    
    features = data[['Age', 'Sleep_Duration', 'Study_Hours', 'Screen_Time']]

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    data['Cluster'] = kmeans.fit_predict(features)

    plt.figure()
    for cluster in range(n_clusters):
        cluster_data = data[data['Cluster'] == cluster]
        plt.scatter(cluster_data['Age'], cluster_data['Sleep_Duration'], label=f'Cluster {cluster}')
    plt.xlabel('Age')
    plt.ylabel('Sleep Duration')
    plt.title('K-Means Clustering of Sleep Patterns')
    plt.legend()
    plt.show()
    
def create_elbow_plot(data, max_clusters=10, filename='elbow_plot.png'):
    from sklearn.cluster import KMeans
    
    features = data[['Age', 'Sleep_Duration', 'Study_Hours', 'Screen_Time']]
    inertia = []

    for k in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(features)
        inertia.append(kmeans.inertia_)

    plt.figure()
    plt.plot(range(1, max_clusters + 1), inertia, marker='o', linestyle='--')
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.savefig(filename)
    plt.close()
    print(f"Elbow plot saved as {filename}")
