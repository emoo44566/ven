import cmath

def calculate_power_factor(complex_power):
    # محاسبه ضریب توان
    return cmath.cos(cmath.phase(complex_power))

def calculate_required_capacitor_bank(complex_power, target_power_factor):
    # محاسبه توان راکتیو قبل از اصلاح
    initial_power_factor = calculate_power_factor(complex_power)
    initial_reactive_power = complex_power.imag

    # محاسبه توان راکتیو مطلوب پس از اصلاح
    corrected_reactive_power = initial_reactive_power * (target_power_factor / initial_power_factor)

    # محاسبه توان مختلط پس از اصلاح
    corrected_complex_power = complex_power.real + 1j * corrected_reactive_power

    # محاسبه توان راکتیو اضافی پس از اصلاح
    additional_reactive_power = corrected_reactive_power - initial_reactive_power

    return corrected_complex_power, additional_reactive_power

# مقادیر ورودی
original_complex_power = 500 + 300j  # توان مختلط قبل از اصلاح
target_power_factor = 0.9  # ضریب توان مطلوب پس از اصلاح

# محاسبه توان مختلط پس از اصلاح و توان متعامل اضافی
corrected_power, additional_reactive_power = calculate_required_capacitor_bank(original_complex_power, target_power_factor)

print(f"Original Complex Power: {original_complex_power} VA")
print(f"Target Power Factor: {target_power_factor}")
print(f"Corrected Complex Power: {corrected_power} VA")
print(f"Additional Reactive Power: {additional_reactive_power} VAR")