import numpy as np

# تعریف اطلاعات منابع ولتاژ و امپدانس‌ها
voltages = [220, 230, 240] # ولتاژ منابع
impedances = [0.1 + 0.5j, 0.2 + 0.3j, 0.15 + 0.4j] # امپدانس خطوط

# تابع محاسبه توان تحویلی و دریافتی و تلفات توان
def calculate_power(voltage_source, impedance):
   current = np.conj(voltage_source) / np.conj(impedance) # جریان
   delivered_power = voltage_source * current # توان تحویلی
   received_power = np.abs(voltage_source)**2 / np.conj(impedance) # توان دریافتی
   power_loss = np.abs(current)**2 * impedance # تلفات توان

   return delivered_power, received_power, power_loss

# محاسبه توان برای هر منبع و خط
for i, voltage_source in enumerate(voltages):
   delivered_power, received_power, power_loss = calculate_power(voltage_source, impedances[i])
   print(f"Voltage Source {i+1}:")
   print(f"Delivered Power: {delivered_power:.2f} VA")
   print(f"Received Power: {received_power:.2f} VA")
   print(f"Power Loss: {power_loss:.2f} VAR")
   print("------------------------")