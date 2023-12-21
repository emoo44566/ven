def calculate_mutual_inductance(mu, N1, N2, A, d):
   """
   Calculate the mutual inductance between two coils due to external flux linkage.

   Parameters:
   - mu: Magnetic permeability of the material
   - N1: Number of turns in the first coil
   - N2: Number of turns in the second coil
   - A: Cross-sectional area of the coils
   - d: Separation distance between the coils

   Returns:
   - mutual_inductance: Mutual inductance between the coils (Henry)
   """
   mutual_inductance = (mu * N1 * N2 * A) / d
   return mutual_inductance

# ورودی‌ها
magnetic_permeability = 4e-7 * np.pi # ضریب مغناطش ماده (هنری بر متر)
number_of_turns_coil1 = 100 # تعداد دورهای پیچ‌ها در هادی اول
number_of_turns_coil2 = 150 # تعداد دورهای پیچ‌ها در هادی دوم
cross_sectional_area = 1e-4 # مساحت مقطع هادی (متر مربع)
separation_distance = 0.1 # فاصله بین هادی‌ها (متر)

# محاسبه اندوکتانس ناشی از شار پیوند خارجی
mutual_inductance_value = calculate_mutual_inductance(
   magnetic_permeability, number_of_turns_coil1, number_of_turns_coil2, cross_sectional_area, separation_distance
)

# نمایش نتیجه
print(f"The mutual inductance due to external flux linkage is {mutual_inductance_value:.6f} Henry.")