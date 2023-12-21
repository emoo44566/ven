def calculate_electrostatic_induction(Q, r):
   """
   Calculate the electrostatic induction at a point due to a positive charge.

   Parameters:
   - Q: Electric charge (Coulombs)
   - r: Distance from the charge (meters)

   Returns:
   - E: Electrostatic induction at the specified distance (Newtons per Coulomb)
   """
   k = 8.9875e9 # Electrostatic constant (N m^2/C^2)
   E = k * Q / r**2
   return E

# ورودی‌ها
electric_charge = 1e-9 # بار الکتریکی موجب (Coulombs)
distance_from_charge = 0.1 # فاصله از بار الکتریکی (meters)

# محاسبه القای الکترواستاتیک
electrostatic_induction = calculate_electrostatic_induction(electric_charge, distance_from_charge)

# نمایش نتیجه
print(f"The electrostatic induction at a distance of {distance_from_charge} meters is {electrostatic_induction:.6e} N/C.")