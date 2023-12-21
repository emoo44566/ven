import math

def calculate_capacitance_with_ground_effect(epsilon_r, D, h):
   """
   Calculate the capacitance of a transmission line considering the ground effect.

   Parameters:
   - epsilon_r: Relative permittivity (dimensionless)
   - D: Distance between conductors (meters)
   - h: Height above ground (meters)

   Returns:
   - capacitance: Capacitance of each phase (Farads)
   """
   epsilon_0 = 8.854e-12 # Permittivity of free space (Farads per meter)
   capacitance = (2 * math.pi * epsilon_r * epsilon_0) / math.acosh(D / (2 * h))
   return capacitance

# ورودی‌ها
relative_permittivity = 4.0 # ضریب دی‌الکتریک (بدون واحد)
distance_between_conductors = 1.0 # فاصله بین موصلین (متر)
height_above_ground = 2.0 # ارتفاع از زمین (متر)

# محاسبه ظرفیت خازنی هر فاز با در نظر گرفتن اثر زمین
capacitance_value = calculate_capacitance_with_ground_effect(relative_permittivity, distance_between_conductors, height_above_ground)

# نمایش نتیجه
print(f"The capacitance of each phase considering ground effect is {capacitance_value:.6e} Farads.")