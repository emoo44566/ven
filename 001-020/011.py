import numpy as np
import matplotlib.pyplot as plt

def simulate_star_connections(num_stars, connection_prob):
   # Create random positions for stars
   star_positions = np.random.rand(num_stars, 2)

   # Create adjacency matrix based on connection probability
   adjacency_matrix = np.random.choice([0, 1], size=(num_stars, num_stars), p=[1 - connection_prob, connection_prob])

   # Ensure diagonal elements are zero (stars are not connected to themselves)
   np.fill_diagonal(adjacency_matrix, 0)

   # Extract connected star pairs
   connected_stars = np.column_stack(np.where(adjacency_matrix == 1))

   # Plot the stars and connections
   plt.scatter(star_positions[:, 0], star_positions[:, 1], marker='o', label='Stars')
   for connection in connected_stars:
    plt.plot(star_positions[connection, 0], star_positions[connection, 1], 'k-', alpha=0.5)

   plt.title('Star Connections Simulation')
   plt.xlabel('X-axis')
   plt.ylabel('Y-axis')
   plt.legend()
   plt.show()

# Example usage
simulate_star_connections(num_stars=10, connection_prob=0.3)