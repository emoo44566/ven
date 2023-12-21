import cmath

def calculate_complex_power(voltage, current, power_factor):
    # محاسبه توان مختلط
    apparent_power = voltage * current
    angle_rad = cmath.phase(complex(power_factor, cmath.sqrt(1 - power_factor**2)))
    active_power = apparent_power * cmath.cos(angle_rad)
    reactive_power = apparent_power * cmath.sin(angle_rad)

    complex_power = active_power + 1j * reactive_power

    return complex_power

def calculate_power_factor(complex_power):
    # محاسبه ضریب توان
    return cmath.cos(cmath.phase(complex_power))

def check_power_balance(complex_power):
    # بررسی توازن توان مختلط با ضریب توان
    power_factor = calculate_power_factor(complex_power)
    if power_factor == 1:
        return "توازن توان مختلط برقرار است."
    else:
        return "توازن توان مختلط برقرار نیست. ضریب توان مختلف از 1 است."

# مقادیر ورودی
voltage = 230  # ولت
current = 10   # آمپر
power_factor = 0.9  # ضریب توان

# محاسبه توان مختلط
result_complex_power = calculate_complex_power(voltage, current, power_factor)

# بررسی توازن توان مختلط
result = check_power_balance(result_complex_power)

print(f"Complex Power: {result_complex_power} VA")
print(f"Power Factor: {power_factor}")
print(result)