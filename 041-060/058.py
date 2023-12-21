import math

def calculate_phase_capacitance(epsilon_r, D, r):
   """
   Calculate the capacitance of one phase in a three-phase transmission line with bundled conductors.

   Parameters:
   - epsilon_r: Relative permittivity (dimensionless)
   - D: Distance between conductors (meters)
   - r: Radius of conductor (conductor's cross-sectional radius) (meters)

   Returns:
   - phase_capacitance: Capacitance of one phase (Farads)
   """
   epsilon_0 = 8.854e-12 # Permittivity of free space (Farads per meter)
   phase_capacitance = (2 * math.pi * epsilon_r * epsilon_0) / math.log(D / r)
   return phase_capacitance

# ورودی‌ها
relative_permittivity = 4.0 # ضریب دی‌الکتریک (بدون واحد)
distance_between_conductors = 1.0 # فاصله بین موصلین (متر)
radius_of_conductor = 0.01 # شعاع موصل (ردیف گلخانه) (متر)

# محاسبه ظرفیت خازنی یک فاز
capacitance_value = calculate_phase_capacitance(relative_permittivity, distance_between_conductors, radius_of_conductor)

# نمایش نتیجه
print(f"The capacitance of one phase is {capacitance_value:.6e} Farads.")