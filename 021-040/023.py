import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# System parameters
base_frequency = 60 # base frequency in Hz
synchronous_speed = 2 * np.pi * base_frequency # synchronous speed in rad/s

# Generator parameters
M = 2.0 # Inertia constant in seconds
D = 0.1 # Damping factor
E_prime = 1.0 # Internal voltage magnitude
Xd = 1.8 # Direct-axis synchronous reactance
Xq = 1.5 # Quadrature-axis synchronous reactance

# System of differential equations
def generator_equations(y, t):
   delta, omega = y
   P_mechanical = 1.0 # Constant mechanical power input

   # Differential equations
   d_delta = synchronous_speed * (omega - 1)
   d_omega = (1 / M) * (P_mechanical - D * (omega - 1) - E_prime * E_prime / Xd * np.sin(delta))

   return [d_delta, d_omega]

# Initial conditions
initial_conditions = [0, 1] # initial delta and omega values

# Time vector
time = np.linspace(0, 5, 1000) # 5 seconds simulation time

# Solve the differential equations
solution = odeint(generator_equations, initial_conditions, time)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(time, solution[:, 0], label='Rotor Angle (delta)')
plt.plot(time, solution[:, 1], label='Rotor Speed (omega)')
plt.xlabel('Time (seconds)')
plt.ylabel('Angle/Speed')
plt.legend()
plt.grid(True)
plt.show()