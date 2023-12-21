import numpy as np

def calculate_mutual_inductance(mu, N1, N2, A12, l12):
   """
   Calculate the mutual inductance between two coils or loops.

   Parameters:
   - mu: Magnetic permeability of the material
   - N1: Number of turns for coil or loop 1
   - N2: Number of turns for coil or loop 2
   - A12: Cross-sectional area of the common face between the coils or loops
   - l12: Distance between the centers of the coils or loops

   Returns:
   - mutual_inductance: Mutual inductance between the coils or loops (Henry)
   """
   mutual_inductance = (mu * N1 * N2 * A12) / l12
   return mutual_inductance

# ورودی‌ها
magnetic_permeability = 4e-7 * np.pi # ضریب مغناطش ماده (هنری بر متر)
number_of_turns_coil1 = 100 # تعداد دورهای پیچ‌ها برای حلقه یا هادی ۱
number_of_turns_coil2 = 80 # تعداد دورهای پیچ‌ها برای حلقه یا هادی ۲
cross_sectional_area_common = 1e-4 # مساحت مقطع پیشانی مشترک (متر مربع)
distance_between_centers = 0.2 # فاصله بین مراکز حلقه یا هادی‌ها (متر)

# محاسبه اندوکتانس ناشی از شار پیوند خارجی
mutual_inductance_value = calculate_mutual_inductance(
   magnetic_permeability,
   number_of_turns_coil1,
   number_of_turns_coil2,
   cross_sectional_area_common,
   distance_between_centers
)

# نمایش نتیجه
print(f"The mutual inductance between the coils or loops is {mutual_inductance_value:.6f} Henry.")