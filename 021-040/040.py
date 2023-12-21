import numpy as np

def calculate_single_phase_inductance(mu, N, A, l):
   """
   Calculate the inductance of a single-phase inductor.

   Parameters:
   - mu: Magnetic permeability of the material
   - N: Number of turns
   - A: Cross-sectional area of the inductor
   - l: Length of the inductor

   Returns:
   - inductance: Inductance of the inductor (Henry)
   """
   inductance = (mu * N**2 * A) / l
   return inductance

# ورودی‌ها
magnetic_permeability = 4e-7 * np.pi # ضریب مغناطش ماده (هنری بر متر)
number_of_turns = 100 # تعداد دورهای پیچ‌ها
cross_sectional_area = 1e-4 # مساحت مقطع هادی (متر مربع)
length_of_inductor = 0.1 # طول هادی (متر)

# محاسبه انداکتانس هادی تکی
inductance_value = calculate_single_phase_inductance(magnetic_permeability, number_of_turns, cross_sectional_area, length_of_inductor)

# نمایش نتیجه
print(f"The inductance of the single-phase inductor is {inductance_value:.6f} Henry.")