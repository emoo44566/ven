import numpy as np

def calculate_symmetrical_three_phase_line_inductance(mu, D, r):
   """
   Calculate the symmetrical inductance of a three-phase transmission line.

   Parameters:
   - mu: Magnetic permeability of the material
   - D: Distance between conductors (meters)
   - r: Radius of the conductor (conductor's cross-sectional radius) (meters)

   Returns:
   - inductance: Symmetrical inductance of the three-phase transmission line (Henry)
   """
   inside_square_root = (D / r) ** 2 - 1
   if inside_square_root < 0:
     raise ValueError("Invalid parameters. The expression inside the square root must be non-negative.")
   
   inductance = (mu / (2 * np.pi)) * np.log((D / r) + np.sqrt(inside_square_root))
   return inductance

# ورودی‌ها
magnetic_permeability = 4e-7 * np.pi # ضریب مغناطش ماده (هنری بر متر)
distance_between_conductors = 1.0 # فاصله بین موصلین (متر)
radius_of_conductor = 0.01 # شعاع موصل (ردیف گلخانه) (متر)

# محاسبه اندوکتانس خطوط سه فاز با فاصله گذاری متقارن
inductance_value = calculate_symmetrical_three_phase_line_inductance(
   magnetic_permeability, distance_between_conductors, radius_of_conductor
)

# نمایش نتیجه
print(f"The symmetrical inductance of the three-phase transmission line is {inductance_value:.6f} Henry.")