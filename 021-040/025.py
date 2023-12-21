import numpy as np
import matplotlib.pyplot as plt

# پارامترهای ترانسفورماتور
primary_voltage = 220 # ولتاژ اولیه
turns_ratio = 1/2   # نسبت دور به دور

# تولید سیگنال ولتاژ اولیه
frequency = 50     # فرکانس (هرتز)
time = np.linspace(0, 0.02, 1000) # بازه زمانی

voltage_primary = primary_voltage * np.sin(2 * np.pi * frequency * time)

# محاسبه ولتاژ ثانویه با توجه به نسبت دور به دور
voltage_secondary = voltage_primary / turns_ratio[0] * turns_ratio[1]

# نمایش نمودار ولتاژ اولیه و ثانویه
plt.plot(time, voltage_primary, label='ولتاژ اولیه')
plt.plot(time, voltage_secondary, label='ولتاژ ثانویه')
plt.title('مدار معادل ترانسفورماتور')
plt.xlabel('زمان (ثانیه)')
plt.ylabel('ولتاژ (ولت)')
plt.legend()
plt.show()