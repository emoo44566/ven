import numpy as np
import matplotlib.pyplot as plt

def calculate_steady_state_velocity(radius, viscosity, pressure_drop, length):
   # Constants
   rho = 1000 # density of the fluid (kg/m^3)
   
   # Hagen–Poiseuille equation for steady laminar flow in a cylindrical pipe
   velocity = (pressure_drop * radius**2) / (4 * viscosity * length)

   return velocity

# Example usage
radius = 0.01 # radius of the cylinder (m)
viscosity = 0.001 # dynamic viscosity of the fluid (Pa.s)
pressure_drop = 1000 # pressure drop across the cylinder (Pa)
length = 0.1 # length of the cylinder (m)

steady_state_velocity = calculate_steady_state_velocity(radius, viscosity, pressure_drop, length)
print(f"Steady State Velocity: {steady_state_velocity} m/s")