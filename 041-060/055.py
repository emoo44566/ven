import math

def calculate_single_phase_line_capacitance(impedance, inductance):
   """
   Calculate the capacitance of a single-phase transmission line.

   Parameters:
   - impedance: Wave impedance of the transmission line (ohms)
   - inductance: Inductance of the transmission line (Henry)

   Returns:
   - capacitance: Capacitance of the transmission line (Farads)
   """
   capacitance = 1 / impedance * math.sqrt(inductance / capacitance)
   return capacitance

# ورودی‌ها
wave_impedance_of_line = 50.0 # اهم
inductance_of_single_phase_line = 1.0e-6 # هنری

# محاسبه ظرفیت خازنی خطوط یکفاز
capacitance_value_single_phase = calculate_single_phase_line_capacitance(
   wave_impedance_of_line, inductance_of_single_phase_line
)

# نمایش نتیجه
print(f"The capacitance of the single-phase transmission line is {capacitance_value_single_phase:.6e} Farads.")