import numpy as np

def calculate_three_phase_line_inductance(mu, D, r):
   """
   Calculate the inductance of a three-phase transmission line.

   Parameters:
   - mu: Magnetic permeability of the material
   - D: Distance between conductors (meters)
   - r: Radius of the conductor (conductor's cross-sectional radius) (meters)

   Returns:
   - inductance: Inductance of the three-phase transmission line (Henry)
   """
   inductance = (mu / (2 * np.pi)) * np.log(D / r)
   return inductance

# ورودی‌ها
magnetic_permeability = 4e-7 * np.pi # ضریب مغناطش ماده (هنری بر متر)
distance_between_conductors = 1.0 # فاصله بین موصلین (متر)
radius_of_conductor = 0.01 # شعاع موصل (ردیف گلخانه) (متر)

# محاسبه اندوکتانس خطوط سه فاز
inductance_value = calculate_three_phase_line_inductance(
   magnetic_permeability, distance_between_conductors, radius_of_conductor
)

# نمایش نتیجه
print(f"The inductance of the three-phase transmission line is {inductance_value:.6f} Henry.")