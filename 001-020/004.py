import cmath

def calculate_power(voltage, current, power_factor):
    # تبدیل زاویه به رادیان
    angle_rad = cmath.phase(complex(power_factor, cmath.sqrt(1 - power_factor**2)))

    # محاسبه توان اکتیو
    active_power = voltage * current * cmath.cos(angle_rad)

    return active_power.real  # بازگرداندن مقدار حقیقی توان

# مقادیر ورودی
voltage = 230  # ولت
current = 10   # آمپر
power_factor = 0.9  # ضریب توان

# محاسبه توان اکتیو
result_power = calculate_power(voltage, current, power_factor)

print(f"Active Power: {result_power} Watts")