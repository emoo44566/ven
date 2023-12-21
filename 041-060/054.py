import math

def calculate_line_capacitance(impedance, inductance, velocity_factor=1):
   """
   Calculate the capacitance of a transmission line.

   Parameters:
   - impedance: Characteristic impedance of the transmission line (ohms)
   - inductance: Inductance of the transmission line (Henry)
   - velocity_factor: Velocity factor of the transmission line (dimensionless)

   Returns:
   - capacitance: Capacitance of the transmission line (Farads)
   """
   capacitance = (1 / impedance) * math.sqrt(inductance / capacitance)
   return capacitance

# ورودی‌ها
characteristic_impedance = 50.0 # اهم
inductance_of_line = 1.0e-6 # هنری
velocity_factor_of_line = 0.9 # بدون واحد

# محاسبه ظرفیت خازنی خط انتقال
capacitance_value = calculate_line_capacitance(
   characteristic_impedance, inductance_of_line, velocity_factor_of_line
)

# نمایش نتیجه
print(f"The capacitance of the transmission line is {capacitance_value:.6e} Farads.")