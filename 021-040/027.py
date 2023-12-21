import numpy as np

def calculate_equivalent_circuit_parameters(primary_voltage, secondary_voltage, power_rating, frequency):
   # محاسبه روابط نسبت دور به دور
   turns_ratio = np.sqrt(primary_voltage / secondary_voltage)

   # محاسبه مقاومت اولیه
   primary_current = power_rating / primary_voltage
   resistance_primary = primary_voltage / primary_current ** 2

   # محاسبه مقاومت ثانویه
   secondary_current = power_rating / secondary_voltage
   resistance_secondary = secondary_voltage / secondary_current ** 2

   # محاسبه لاکتانس اولیه
   inductance_primary = (primary_voltage * turns_ratio) / (2 * np.pi * frequency * primary_current)

   # محاسبه لاکتانس ثانویه
   inductance_secondary = (secondary_voltage / turns_ratio) / (2 * np.pi * frequency * secondary_current)

   return {
     'Turns Ratio': turns_ratio,
     'Primary Resistance': resistance_primary,
     'Secondary Resistance': resistance_secondary,
     'Primary Inductance': inductance_primary,
     'Secondary Inductance': inductance_secondary
   }

# تعیین پارامترهای ورودی
primary_voltage = 220
secondary_voltage = 110
power_rating = 1000
frequency = 50

# محاسبه پارامترهای مدار معادل
equivalent_circuit_parameters = calculate_equivalent_circuit_parameters(primary_voltage, secondary_voltage, power_rating, frequency)

# نمایش پارامترها
for parameter, value in equivalent_circuit_parameters.items():
   print(f"{parameter}: {value}")