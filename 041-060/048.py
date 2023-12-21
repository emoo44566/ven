import numpy as np

def calculate_asymmetrical_three_phase_line_inductance(mu, D1, D2, r):
   """
   Calculate the asymmetrical inductance of a three-phase transmission line.

   Parameters:
   - mu: Magnetic permeability of the material
   - D1: Distance between conductor 1 and the neutral point (meters)
   - D2: Distance between conductor 2 and the neutral point (meters)
   - r: Radius of the conductor (conductor's cross-sectional radius) (meters)

   Returns:
   - inductance: Asymmetrical inductance of the three-phase transmission line (Henry)
   """
   inside_square_root = (D1 * D2 / r**2) - 1
   if inside_square_root < 0:
     raise ValueError("Invalid parameters. The expression inside the square root must be non-negative.")
   
   inductance = (mu / (2 * np.pi)) * (
     np.log((D1 + D2) / (2 * r)) + 
     ((D2 - D1) / (D1 + D2)) * np.sqrt(inside_square_root)
   )
   return inductance

# ورودی‌ها
magnetic_permeability = 4e-7 * np.pi # ضریب مغناطش ماده (هنری بر متر)
distance_to_neutral_point_conductor1 = 1.0 # فاصله تا نقطه نیوترال برای موصل 1 (متر)
distance_to_neutral_point_conductor2 = 2.0 # فاصله تا نقطه نیوترال برای موصل 2 (متر)
radius_of_conductor = 0.01 # شعاع موصل (ردیف گلخانه) (متر)

# محاسبه اندوکتانس خطوط سه فاز با فاصله گذاری نامتقارن
inductance_value = calculate_asymmetrical_three_phase_line_inductance(
   magnetic_permeability, distance_to_neutral_point_conductor1, distance_to_neutral_point_conductor2, radius_of_conductor
)

# نمایش نتیجه
print(f"The asymmetrical inductance of the three-phase transmission line is {inductance_value:.6f} Henry.")