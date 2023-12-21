def calculate_series_inductance(inductances):
   """
   Calculate the inductance of inductors connected in series.

   Parameters:
   - inductances: List of inductances connected in series (Henry)

   Returns:
   - total_inductance: Total inductance of the series connection (Henry)
   """
   total_inductance = sum(inductances)
   return total_inductance

# مثال: دو هادی به صورت سری
inductance1 = 2.0e-3 # هنری
inductance2 = 3.0e-3 # هنری

# محاسبه اندوکتانس هادی‌های مرکب در حالت سری
total_series_inductance = calculate_series_inductance([inductance1, inductance2])

# نمایش نتیجه
print(f"The total inductance of the series connection is {total_series_inductance:.6f} Henry.")