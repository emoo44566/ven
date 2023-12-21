import numpy as np

def calculate_self_inductance(N, A, l):
   """
   Calculate the self-inductance of a coil or loop.

   Parameters:
   - N: Number of turns
   - A: Cross-sectional area of the coil or loop
   - l: Perimeter or circumference of the coil or loop

   Returns:
   - self_inductance: Self-inductance of the coil or loop (Henry)
   """
   mu_0 = 4e-7 * np.pi # Magnetic permeability of free space (Henry per meter)
   self_inductance = (mu_0 * N**2 * A) / l
   return self_inductance

# ورودی‌ها
number_of_turns = 100 # تعداد دورهای پیچ‌ها
cross_sectional_area = 1e-4 # مساحت مقطع حلقه یا هادی (متر مربع)
perimeter_of_coil = 0.2 # محیط حلقه یا هادی (متر)

# محاسبه اندوکتانس داخلی
self_inductance_value = calculate_self_inductance(number_of_turns, cross_sectional_area, perimeter_of_coil)

# نمایش نتیجه
print(f"The self-inductance of the coil or loop is {self_inductance_value:.6f} Henry.")