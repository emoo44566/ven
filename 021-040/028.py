import numpy as np

def calculate_efficiency(turns_ratio, resistance_primary, resistance_secondary, inductance_primary, inductance_secondary, load_impedance):
   # محاسبه جریان اولیه
   primary_current = load_impedance / (resistance_primary + 1j * (2 * np.pi * 50 * inductance_primary))

   # محاسبه ولتاژ ثانویه
   secondary_voltage = turns_ratio * primary_current * (resistance_secondary + 1j * (2 * np.pi * 50 * inductance_secondary))

   # محاسبه توان ولتاژ اولیه و ثانویه
   input_power = primary_current * np.conj(primary_current) * (resistance_primary + 1j * (2 * np.pi * 50 * inductance_primary))
   output_power = secondary_voltage * np.conj(secondary_voltage) / turns_ratio

   # محاسبه کارائی
   efficiency = (output_power / input_power).real * 100

   return efficiency

# تعیین پارامترهای مدار معادل
turns_ratio = 2
resistance_primary = 0.1
resistance_secondary = 0.2
inductance_primary = 0.01
inductance_secondary = 0.02
load_impedance = 10 + 1j * 5

# محاسبه کارائی
efficiency = calculate_efficiency(turns_ratio, resistance_primary, resistance_secondary, inductance_primary, inductance_secondary, load_impedance)

# نمایش کارائی
print(f"کارائی ترانسفورماتور: {efficiency:.2f}%")