import numpy as np

def calculate_mutual_inductance(L1, L2, k):
   """
   Calculate the mutual inductance between two coils.

   Parameters:
   - L1: Self-inductance of the first coil (Henry)
   - L2: Self-inductance of the second coil (Henry)
   - k: Coefficient of coupling between the coils

   Returns:
   - mutual_inductance: Mutual inductance between the coils (Henry)
   """
   mutual_inductance = k * np.sqrt(L1 * L2)
   return mutual_inductance

# ورودی‌ها
self_inductance_coil1 = 1.0e-3 # اندوکتانس خودی ملفون اول (هنری)
self_inductance_coil2 = 2.0e-3 # اندوکتانس خودی ملفون دوم (هنری)
coefficient_of_coupling = 0.8 # ضریب لچک‌گذاری

# محاسبه شار پیوندی
mutual_inductance_value = calculate_mutual_inductance(self_inductance_coil1, self_inductance_coil2, coefficient_of_coupling)

# نمایش نتیجه
print(f"The mutual inductance is {mutual_inductance_value:.6f} Henry.")