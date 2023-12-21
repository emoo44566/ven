import math

def calculate_capacitance_three_phase_dual_circuit(epsilon_r, D, r):
   """
   Calculate the capacitance of a three-phase dual-circuit transmission line.

   Parameters:
   - epsilon_r: Relative permittivity (dimensionless)
   - D: Distance between conductors (meters)
   - r: Radius of conductor (conductor's cross-sectional radius) (meters)

   Returns:
   - capacitance: Capacitance of each phase (Farads)
   """
   epsilon_0 = 8.854e-12 # Permittivity of free space (Farads per meter)
   capacitance = (2 * math.pi * epsilon_r * epsilon_0) / math.log(D / r)
   return capacitance

# ورودی‌ها
relative_permittivity = 4.0 # ضریب دی‌الکتریک (بدون واحد)
distance_between_conductors = 1.0 # فاصله بین موصلین (متر)
radius_of_conductor = 0.01 # شعاع موصل (ردیف گلخانه) (متر)

# محاسبه ظرفیت خازنی هر فاز
capacitance_value = calculate_capacitance_three_phase_dual_circuit(relative_permittivity, distance_between_conductors, radius_of_conductor)

# نمایش نتیجه
print(f"The capacitance of each phase is {capacitance_value:.6e} Farads.")