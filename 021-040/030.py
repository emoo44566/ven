import numpy as np
import matplotlib.pyplot as plt

def model_single_phase_transformer(voltage_primary, turns_ratio, resistance, inductance, frequency, time):
   # محاسبه ولتاژ اولیه
   voltage_primary_phase = voltage_primary * np.sin(2 * np.pi * frequency * time)

   # محاسبه ولتاژ ثانویه
   voltage_secondary_phase = voltage_primary_phase / turns_ratio

   # محاسبه جریان
   current_phase = voltage_primary_phase / (resistance + 1j * (2 * np.pi * frequency * inductance))

   return voltage_primary_phase, voltage_secondary_phase, current_phase

# پارامترهای ترانسفورماتور سه فاز
voltage_primary = 220       # ولتاژ اولیه
turns_ratio = 2           # نسبت دور به دور
resistance = 0.1         # مقاومت
inductance = 0.01         # لاکتانس
frequency = 50           # فرکانس (هرتز)
time = np.linspace(0, 0.02, 1000) # بازه زمانی

# مدل کردن هر فاز در ترانسفورماتور سه فاز
voltage_primary_phase, voltage_secondary_phase, current_phase = model_single_phase_transformer(
   voltage_primary, turns_ratio, resistance, inductance, frequency, time)

# نمایش نمودارها
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(time, voltage_primary_phase, label='Voltage Primary Phase')
plt.plot(time, voltage_secondary_phase, label='Voltage Secondary Phase')
plt.title('Voltage of Primary and Secondary Phase')
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time, np.abs(current_phase), label='Current Phase')
plt.title('Current of Phase')
plt.xlabel('Time')
plt.ylabel('Current Magnitude')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()