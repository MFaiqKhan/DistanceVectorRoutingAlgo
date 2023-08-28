# Muhammad Faiq Khan , B20102084 , SECTION B
# Distance Vector Algorithm . 
# First Install matplotlib abd networkx library through pip
# then run : python distancevectoralgorithmB20102084.py
# then enter the number of vertices , edges , start , end and weight of an edge
# then enter the source vertex
# then you will get the distance from the source vertex
# then you will get the routing table
# then you will get the normal graph
# then you will get the shortest path graph

import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []

    def add_edge(self, start, end, weight):
        self.edges.append((start, end, weight))

    def bellman_ford(self, source):
        # Step 1: Initialize distances
        distances = [float('inf')] * self.num_vertices
        distances[source] = 0

        # Step 2: Relax edges repeatedly
        for _ in range(self.num_vertices - 1):
            for start, end, weight in self.edges:
                if distances[start] != float('inf') and distances[start] + weight < distances[end]:
                    distances[end] = distances[start] + weight

        # Step 3: Check for negative cycles
        for start, end, weight in self.edges:
            if distances[start] != float('inf') and distances[start] + weight < distances[end]:
                print("Negative cycle detected. The graph contains a negative-weight cycle.")
                return

        return distances

# Create a graph
num_vertices = int(input("Enter the number of vertices: "))
graph = Graph(num_vertices)

# Add edges to the graph
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    start, end, weight = map(int, input("Enter start, end, and weight of an edge (space-separated): ").split())
    graph.add_edge(start, end, weight)

# Run Bellman-Ford algorithm
source = int(input("Enter the source vertex: "))
distances = graph.bellman_ford(source)

# Print the distances
print("Distance from the source vertex:")
routing_table = []
for vertex, distance in enumerate(distances):
    print(f"Vertex {vertex}: {distance}" if distance != float('inf') else f"Vertex {vertex}: No path")
    routing_table.append((vertex, distance))

# Print the routing table list
print("\nRouting Table:")
for vertex, distance in routing_table:
    print(f"Vertex {vertex}: {distance}" if distance != float('inf') else f"Vertex {vertex}: No path")

# Create the normal graph
G_normal = nx.DiGraph()
G_normal.add_weighted_edges_from(graph.edges)

# Create the shortest path graph
G_shortest_path = nx.DiGraph()
shortest_path_edges = [(start, end, weight) for start, end, weight in graph.edges if distances[end] == distances[start] + weight]
G_shortest_path.add_weighted_edges_from(shortest_path_edges)

# Set node colors based on the distance from the source vertex
node_colors_normal = ['green' if distance != float('inf') else 'red' for distance in distances]
node_colors_shortest_path = ['green' if distance != float('inf') else 'red' for distance in distances]

# Set edge colors for the normal graph
edge_colors_normal = ['gray' for _ in graph.edges]

# Set edge colors for the shortest path graph
edge_colors_shortest_path = ['blue' for _ in shortest_path_edges]

# Draw the normal graph
pos = nx.spring_layout(G_normal)
nx.draw_networkx(G_normal, pos, node_color=node_colors_normal, edge_color=edge_colors_normal, with_labels=True, node_size=500)
nx.draw_networkx_edge_labels(G_normal, pos, edge_labels=nx.get_edge_attributes(G_normal, 'weight'))

# Show the normal graph
plt.title("Normal Graph")
plt.show()

# Draw the shortest path graph
pos = nx.spring_layout(G_shortest_path)
nx.draw_networkx(G_shortest_path, pos, node_color=node_colors_shortest_path, edge_color=edge_colors_shortest_path, with_labels=True, node_size=500)
nx.draw_networkx_edge_labels(G_shortest_path, pos, edge_labels=nx.get_edge_attributes(G_shortest_path, 'weight'))

# Show the shortest path graph
plt.title("Shortest Path Graph")
plt.show()


""" 
Handling Negative Cycles:
- The Bellman-Ford algorithm implemented in the bellman_ford method checks for negative cycles in the graph.

- After relaxing the edges repeatedly in Step 2, the algorithm performs an additional iteration to check for negative cycles in Step 3.

- If during this iteration, the algorithm finds a vertex where the distance can still be further reduced, it detects a negative cycle and
prints the message "Negative cycle detected. The graph contains a negative-weight cycle."

Handling Negative Weights:

- The Bellman-Ford algorithm is designed to handle negative weights in the graph.
 
- During the relaxation step in Step 2, if the sum of the distance from the source vertex to the current vertex and the weight of the edge connecting 
them is smaller than the current distance to the destination vertex, the algorithm updates the distance.
 
- This process continues until no further updates can be made, ensuring that the algorithm finds the shortest paths even with negative weights.

"""