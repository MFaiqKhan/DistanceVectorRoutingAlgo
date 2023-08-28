# Muhammad Faiq Khan , B20102084 , SECTION B
# Distance Vector Algorithm . 
# First Install matplotlib abd networkx library through pip
# then run : python distancevectoralgorithmB20102084.py
# then enter the number of vertices , edges , start , end and weight of an edge
# then enter the source vertex
# then you will get the distance from the source vertex
# then you will get the routing table
# then you will get the normal graph

import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.distance_table = [[float('inf') for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.next_hop_table = [[None for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, start, end, weight):
        self.distance_table[start][end] = weight
        self.distance_table[end][start] = weight

    def distance_vector_routing(self):
        # Step 1: Initialize distance table
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if i == j:
                    self.distance_table[i][j] = 0
                elif self.distance_table[i][j] != float('inf'):
                    self.next_hop_table[i][j] = j

        iteration = 1
        while True:
            updated = False
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    if i != j:
                        #min_distance = min(self.distance_table[i][k] + self.distance_table[k][j] for k in range(self.num_vertices))
                        min_distance = min(self.distance_table[i][k] + self.distance_table[k][j] for k in range(self.num_vertices) if self.distance_table[i][k] != float('inf') and self.distance_table[k][j] != float('inf'))
                        if min_distance < self.distance_table[i][j]:
                            self.distance_table[i][j] = min_distance
                            # Update the next hop table correctly
                            self.next_hop_table[i][j] = min((k for k in range(self.num_vertices)), key=lambda k: self.distance_table[i][k] + self.distance_table[k][j])
                            updated = True
            print(f"Iteration {iteration} Routing Table:")
            self.print_routing_table()
            iteration += 1
            if not updated:
                break

    def print_routing_table(self):
        print("Routing Table:")
        for i in range(self.num_vertices):
            print(f"Node {i}:")
            for j in range(self.num_vertices):
                if i != j:
                    next_hop = self.next_hop_table[i][j]
                    distance = self.distance_table[i][j]
                    if next_hop is not None:
                        print(f"  -> Node {j} (Next Hop: {next_hop}), Distance: {distance}")
                    else:
                        print(f"  -> Node {j} (Next Hop: None), Distance: {distance}")

    def visualize_graph(self):
    # Create the normal graph
        G_normal = nx.DiGraph()
        G_normal.add_weighted_edges_from([(i, j, self.distance_table[i][j]) for i in range(self.num_vertices) for j in range(self.num_vertices) if i != j])

        # Set node colors based on the distance from the source vertex
        node_colors_normal = ['green' if self.distance_table[i][j] != float('inf') else 'red' for i in range(self.num_vertices) for j in range(self.num_vertices) if i != j]
        node_colors_normal = [color for i, color in enumerate(node_colors_normal) if i in G_normal.nodes()]

        # Set edge colors for the normal graph
        edge_colors_normal = ['gray' for i in range(self.num_vertices) for j in range(self.num_vertices) if i != j]

        # Draw the normal graph
        pos = nx.spring_layout(G_normal)
        nx.draw_networkx(G_normal, pos, node_color=node_colors_normal, edge_color=edge_colors_normal, with_labels=True, node_size=500)
        nx.draw_networkx_edge_labels(G_normal, pos, edge_labels=nx.get_edge_attributes(G_normal, 'weight'))

        # Show the normal graph
        plt.title("Normal Graph")
        plt.show()


# Create a graph
num_vertices = int(input("Enter the number of vertices: "))
graph = Graph(num_vertices)

# Add edges to the graph
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    start, end, weight = map(int, input("Enter start, end, and weight of an edge (space-separated): ").split())
    graph.add_edge(start, end, weight)

# Print the initial routing table
print("Initial Routing Table:")
graph.print_routing_table()

# Run Distance Vector Routing algorithm
graph.distance_vector_routing()

# Print the final routing table
print("Final Routing Table:")
graph.print_routing_table()

# Visualize the graph
graph.visualize_graph()
