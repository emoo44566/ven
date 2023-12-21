def calculate_parallel_inductance(inductances):
   """
   Calculate the inductance of inductors connected in parallel.

   Parameters:
   - inductances: List of inductances connected in parallel (Henry)

   Returns:
   - total_inductance: Total inductance of the parallel connection (Henry)
   """
   total_inductance = 1 / sum(1 / L for L in inductances)
   return total_inductance

# مثال: دو هادی به صورت موازی
inductance1 = 2.0e-3 # هنری
inductance2 = 3.0e-3 # هنری

# محاسبه اندوکتانس هادی‌های مرکب در حالت موازی
total_parallel_inductance = calculate_parallel_inductance([inductance1, inductance2])

# نمایش نتیجه
print(f"The total inductance of the parallel connection is {total_parallel_inductance:.6f} Henry.")