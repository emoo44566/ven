import numpy as np
import matplotlib.pyplot as plt

def model_autotransformer(voltage_primary, voltage_secondary, turns_ratio, resistance_primary, resistance_secondary, inductance_primary, inductance_secondary, frequency, time):
   # محاسبه ولتاژ اولیه و ثانویه
   voltage_primary_phase = voltage_primary * np.sin(2 * np.pi * frequency * time)
   voltage_secondary_phase = voltage_primary_phase / turns_ratio

   # محاسبه جریان از قانون اهم
   current_primary = voltage_primary_phase / (resistance_primary + 1j * (2 * np.pi * frequency * inductance_primary))
   current_secondary = voltage_secondary_phase / (resistance_secondary + 1j * (2 * np.pi * frequency * inductance_secondary))

   return voltage_primary_phase, voltage_secondary_phase, current_primary, current_secondary

# پارامترهای اتوترانسفورماتور
voltage_primary = 220       # ولتاژ اولیه
voltage_secondary = 110     # ولتاژ ثانویه
turns_ratio = voltage_primary / voltage_secondary # نسبت دور به دور
resistance_primary = 0.1     # مقاومت اولیه
resistance_secondary = 0.2   # مقاومت ثانویه
inductance_primary = 0.01   # لاکتانس اولیه
inductance_secondary = 0.02   # لاکتانس ثانویه
frequency = 50           # فرکانس (هرتز)
time = np.linspace(0, 0.02, 1000) # بازه زمانی

# مدل کردن اتوترانسفورماتور
voltage_primary_phase, voltage_secondary_phase, current_primary, current_secondary = model_autotransformer(
   voltage_primary, voltage_secondary, turns_ratio, resistance_primary, resistance_secondary, inductance_primary, inductance_secondary, frequency, time)

# نمایش نمودارها
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(time, voltage_primary_phase, label='Voltage Primary Phase')
plt.title('Voltage Primary Phase')
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(time, voltage_secondary_phase, label='Voltage Secondary Phase')
plt.title('Voltage Secondary Phase')
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(time, np.abs(current_primary), label='Current Primary')
plt.title('Current Primary')
plt.xlabel('Time')
plt.ylabel('Current Magnitude')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(time, np.abs(current_secondary), label='Current Secondary')
plt.title('Current Secondary')
plt.xlabel('Time')
plt.ylabel('Current Magnitude')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()