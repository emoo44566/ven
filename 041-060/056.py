def calculate_potential_difference(current, impedance):
   """
   Calculate the potential difference in a multiple conductor arrangement.

   Parameters:
   - current: Current flowing through the arrangement (Amperes)
   - impedance: Impedance of the arrangement (Ohms)

   Returns:
   - potential_difference: Potential difference across the arrangement (Volts)
   """
   potential_difference = current * impedance
   return potential_difference

# ورودی‌ها
current_flow = 10.0 # آمپر
impedance_of_arrangement = 20.0 # اهم

# محاسبه اختلاف پتانسیل
potential_difference_value = calculate_potential_difference(current_flow, impedance_of_arrangement)

# نمایش نتیجه
print(f"The potential difference across the arrangement is {potential_difference_value:.6f} Volts.")