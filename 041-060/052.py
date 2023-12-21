import math

def calculate_gmr(diameters):
   """
   Calculate the Geometric Mean Radius (GMR) of conductors.

   Parameters:
   - diameters: List of diameters of conductors (meters)

   Returns:
   - gmr: Geometric Mean Radius (meters)
   """
   n = len(diameters)
   product_of_diameters = math.prod(diameters)
   gmr = product_of_diameters ** (1/n)
   return gmr

# مثال: سه هادی گروهی با قطرهای مختلف
diameter1 = 0.01 # متر
diameter2 = 0.015 # متر
diameter3 = 0.02 # متر

# محاسبه GMR
gmr_value = calculate_gmr([diameter1, diameter2, diameter3])

# نمایش نتیجه
print(f"The Geometric Mean Radius (GMR) is {gmr_value:.6f} meters.")