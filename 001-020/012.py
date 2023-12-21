import numpy as np
import matplotlib.pyplot as plt

def simulate_triangle_connections(num_nodes):
   # Create random positions for nodes
   node_positions = np.random.rand(num_nodes, 2)

   # Create adjacency matrix for triangle connections
   adjacency_matrix = np.zeros((num_nodes, num_nodes))

   for i in range(num_nodes):
     for j in range(i + 1, num_nodes):
       # Connect nodes to form triangles
        if np.random.rand() < 0.5:
           adjacency_matrix[i, j] = 1
           adjacency_matrix[j, i] = 1

   # Extract connected node pairs
   connected_nodes = np.column_stack(np.where(adjacency_matrix == 1))

   # Plot the nodes and connections
   plt.scatter(node_positions[:, 0], node_positions[:, 1], marker='o', label='Nodes')
   for connection in connected_nodes:
    plt.plot(node_positions[connection, 0], node_positions[connection, 1], 'k-', alpha=0.5)

   plt.title('Triangle Connections Simulation')
   plt.xlabel('X-axis')
   plt.ylabel('Y-axis')
   plt.legend()
   plt.show()

# Example usage
simulate_triangle_connections(num_nodes=10)