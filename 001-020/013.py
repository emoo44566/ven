import numpy as np
import matplotlib.pyplot as plt

def convert_triangle_to_star(num_nodes):
   # Create random positions for nodes
   node_positions = np.random.rand(num_nodes, 2)

   # Create adjacency matrix for triangle connections
   adjacency_matrix_triangle = np.zeros((num_nodes, num_nodes))

   for i in range(num_nodes):
     for j in range(i + 1, num_nodes):
       # Connect nodes to form triangles
       if np.random.rand() < 0.5:
           adjacency_matrix_triangle[i, j] = 1
           adjacency_matrix_triangle[j, i] = 1

   # Convert triangle connections to star connections
   adjacency_matrix_star = np.zeros((num_nodes, num_nodes))

   for i in range(num_nodes):
     neighbors = np.where(adjacency_matrix_triangle[i] == 1)[0]
     if len(neighbors) > 1:
       # Connect neighbors to form a star
       adjacency_matrix_star[i, neighbors] = 1
       adjacency_matrix_star[neighbors, i] = 1

   # Extract connected node pairs for star connections
   connected_nodes_star = np.column_stack(np.where(adjacency_matrix_star == 1))

   # Plot the nodes and connections
   plt.scatter(node_positions[:, 0], node_positions[:, 1], marker='o', label='Nodes')
   for connection in connected_nodes_star:
     plt.plot(node_positions[connection, 0], node_positions[connection, 1], 'k-', alpha=0.5)

   plt.title('Star Connections from Triangle')
   plt.xlabel('X-axis')
   plt.ylabel('Y-axis')
   plt.legend()
   plt.show()

# Example usage
convert_triangle_to_star(num_nodes=10)