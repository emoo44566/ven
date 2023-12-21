import numpy as np

def calculate_dual_circuit_three_phase_line_inductance(mu, D, r):
   """
   Calculate the inductance of dual-circuit three-phase transmission line.

   Parameters:
   - mu: Magnetic permeability of the material
   - D: Distance between conductors (meters)
   - r: Radius of the conductor (conductor's cross-sectional radius) (meters)

   Returns:
   - inductance: Inductance of the dual-circuit three-phase transmission line (Henry)
   """
   inside_square_root = (D / r) ** 2 - 1
   if inside_square_root < 0:
     raise ValueError("Invalid parameters. The expression inside the square root must be non-negative.")
   
   inductance = (mu / (2 * np.pi)) * (
     np.log((D / r) + np.sqrt(inside_square_root)) + 
     1 / np.sqrt(inside_square_root)
   )
   return inductance

# ورودی‌ها
magnetic_permeability = 4e-7 * np.pi # ضریب مغناطش ماده (هنری بر متر)
distance_between_conductors = 1.0 # فاصله بین موصلین (متر)
radius_of_conductor = 0.01 # شعاع موصل (ردیف گلخانه) (متر)

# محاسبه اندوکتانس خطوط دو مداره سه فاز
inductance_value = calculate_dual_circuit_three_phase_line_inductance(
   magnetic_permeability, distance_between_conductors, radius_of_conductor
)

# نمایش نتیجه
print(f"The inductance of the dual-circuit three-phase transmission line is {inductance_value:.6f} Henry.")