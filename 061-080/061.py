import math

def calculate_magnetic_field(I, r):
   """
   Calculate the magnetic field induced by a current in a loop.

   Parameters:
   - I: Current in the loop (Amperes)
   - r: Distance from the axis of the loop (meters)

   Returns:
   - B: Magnetic field strength at the specified distance (Teslas)
   """
   mu_0 = 4 * math.pi * 1e-7 # Permeability of free space (Teslas meter per Ampere)
   B = (mu_0 * I) / (2 * math.pi * r)
   return B

# ورودی‌ها
current_in_loop = 1.0 # جریان در حلقه (آمپر)
distance_from_axis = 0.05 # فاصله از محور حلقه (متر)

# محاسبه میدان مغناطیسی
magnetic_field_strength = calculate_magnetic_field(current_in_loop, distance_from_axis)

# نمایش نتیجه
print(f"The magnetic field strength at a distance of {distance_from_axis} meters is {magnetic_field_strength:.6e} Teslas.")