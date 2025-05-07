import networkx as nx
import matplotlib.pyplot as plt

# Load the dataset
G = nx.karate_club_graph()

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='blue', node_size=800, edge_color='gray')
plt.title("Zachary's Karate Club Network")
plt.show()

# Print some basic info
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# Total degree of all nodes
total_degree = sum(dict(G.degree()).values())
# Average degree
avg_degree = total_degree / G.number_of_nodes()
print(f"Average Degree: {avg_degree:.2f}")

# Global clustering coefficient
global_clustering = nx.transitivity(G)
print(f"Global Clustering Coefficient: {global_clustering:.4f}")

# Average global clustering coefficient
avg_clustering = nx.average_clustering(G)
print(f"Average Clustering Coefficient: {avg_clustering:.4f}")


# Get all degrees
degrees = [deg for _, deg in G.degree()]

# Plot histogram
plt.figure(figsize=(8, 5))
plt.hist(degrees, bins=range(1, max(degrees)+2), align='left', color='skyblue', edgecolor='black')
plt.title("Degree Distribution of Karate Club Graph")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Overview
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Average Degree:", avg_degree)
print("Global Clustering Coefficient (Transitivity):", global_clustering)
print("Average Clustering Coefficient:", avg_clustering)


# Analyze the graph
centrality = nx.degree_centrality(G)
most_central = max(centrality, key=centrality.get)
print(f"Most central node (by degree): {most_central}")

# Community detection
from networkx.algorithms.community import girvan_newman
communities = next(girvan_newman(G))
print("Detected communities:", [list(c) for c in communities])

