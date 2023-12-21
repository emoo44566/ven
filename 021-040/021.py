import numpy as np

def calculate_power_factor_and_power_angle(voltage, current, power):
   apparent_power = voltage * current
   power_factor = power / apparent_power
   power_angle = np.arccos(power_factor) # in radians, convert to degrees if needed

   return power_factor, np.degrees(power_angle)

# Example usage
voltage = 230 # in volts
current = 10 # in amperes
power = 2000 # in watts

power_factor, power_angle = calculate_power_factor_and_power_angle(voltage, current, power)

print(f"Power Factor: {power_factor}")
print(f"Power Angle: {power_angle} degrees")