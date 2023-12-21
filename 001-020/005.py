import cmath

def calculate_complex_power(voltage, current, power_factor):
    # محاسبه توان مختلط
    apparent_power = voltage * current
    angle_rad = cmath.phase(complex(power_factor, cmath.sqrt(1 - power_factor**2)))
    active_power = apparent_power * cmath.cos(angle_rad)
    reactive_power = apparent_power * cmath.sin(angle_rad)

    complex_power = active_power + 1j * reactive_power

    return complex_power

# مقادیر ورودی
voltage = 230  # ولت
current = 10   # آمپر
power_factor = 0.9  # ضریب توان

# محاسبه توان مختلط
result_complex_power = calculate_complex_power(voltage, current, power_factor)

print(f"Complex Power: {result_complex_power} VA")
print(f"Active Power (P): {result_complex_power.real} Watts")
print(f"Reactive Power (Q): {result_complex_power.imag} VAR")