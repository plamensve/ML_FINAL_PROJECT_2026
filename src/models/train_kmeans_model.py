from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def elbow_method_apply(data):
    """
    :param data: dataframe
    :return: None, shows elbow plot
    """
    # Create an empty list where the inertia values for each K-Means model will be stored.
    inertias = []

    # Test different numbers of clusters from 1 to 10.
    for i in range(1, 11):
        km = KMeans(n_clusters=i)
        km.fit(data)

        # Store the inertia value for the current number of clusters.
        # Inertia measures how close the data points are to their assigned cluster centers.
        inertias.append(km.inertia_)

    # Plot the inertia values for each number of clusters.
    # This helps us visually apply the Elbow Method.
    plt.plot(range(1, 11), inertias, marker='o')

    plt.title('Elbow method [KMeans clustering] / Personal performance stat')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.xticks(range(1, 11))

    plt.show()


def train_kmeans_model(data, n_clusters=5, random_state=42):
    """
    :param data: dataframe
    :param n_clusters: int
    :param random_state: default int
    :return: model, labels
    """

    model = KMeans(
        n_clusters=n_clusters,
        random_state=random_state
    )

    cluster_labels = model.fit_predict(data)

    return model, cluster_labels