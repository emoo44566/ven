import numpy as np

def calculate_power_angle(voltage_magnitude, voltage_angle, current_magnitude, current_angle):
   # Convert angles from degrees to radians
   voltage_angle_rad = np.radians(voltage_angle)
   current_angle_rad = np.radians(current_angle)

   # Calculate power angle
   power_angle_rad = np.arccos((voltage_magnitude * np.cos(voltage_angle_rad) * current_magnitude * np.cos(current_angle_rad) +
                      voltage_magnitude * np.sin(voltage_angle_rad) * current_magnitude * np.sin(current_angle_rad)) /
                     (voltage_magnitude * current_magnitude))

   # Convert power angle from radians to degrees
   power_angle_deg = np.degrees(power_angle_rad)

   return power_angle_deg

# Example usage
voltage_magnitude = 230 # in volts
voltage_angle = 0 # in degrees
current_magnitude = 10 # in amperes
current_angle = 30 # in degrees

power_angle = calculate_power_angle(voltage_magnitude, voltage_angle, current_magnitude, current_angle)

print(f"Power Angle: {power_angle} degrees")