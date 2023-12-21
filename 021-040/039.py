def calculate_line_resistance(length, resistance_per_meter):
   """
   Calculate the resistance of a transmission line based on its length and resistance per meter.

   Parameters:
   - length: Length of the transmission line (in meters)
   - resistance_per_meter: Resistance per meter of the transmission line (in Ohms)

   Returns:
   - line_resistance: Total resistance of the transmission line (in Ohms)
   """
   line_resistance = length * resistance_per_meter
   return line_resistance

# ورودی‌ها
transmission_line_length = 100.0 # طول خط انتقال (متر)
resistance_per_meter = 0.01 # مقاومت هر متر خط انتقال (اهم)

# محاسبه مقاومت خط
line_resistance = calculate_line_resistance(transmission_line_length, resistance_per_meter)

# نمایش نتیجه
print(f"The resistance of the transmission line is {line_resistance:.4f} Ohms.")