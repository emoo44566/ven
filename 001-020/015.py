import cmath

def calculate_power(voltage_line, current_line):
   # Calculate complex power
   complex_power = cmath.sqrt(3) * voltage_line * current_line

   # Extract real and reactive power components
   real_power = complex_power.real
   reactive_power = complex_power.imag

   return real_power, reactive_power

# Example usage
voltage_line = complex(400, 0) # Line-to-line voltage in volts
current_line = complex(100, -30) # Line current in amperes (with phase angle)

real_power, reactive_power = calculate_power(voltage_line, current_line)

print(f"Real Power: {real_power:.2f} Watts")
print(f"Reactive Power: {reactive_power:.2f} VAr")