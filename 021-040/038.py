import numpy as np
import matplotlib.pyplot as plt

# پارامترهای خط
length = 100.0 # طول خط (متر)
frequency = 50.0 # فرکانس (هرتز)
velocity_of_light = 3e8 # سرعت نور (متر بر ثانیه)
characteristic_impedance = 50.0 # مقاومت آمپدانس خط (اهم)

# معادلات ترانسمیسیون مدل مخابراتی
def transmission_line_model(length, frequency, velocity_of_light, characteristic_impedance):
 wavelength = velocity_of_light / frequency
 beta = 2 * np.pi / wavelength
 alpha = 0.01 * beta # ضریب خنثیای محیط
 Zc = characteristic_impedance

 # زاویه فاز
 phase_angle = beta * length

 # مقاومت و آمپدانس در هر نقطه
 resistance = alpha * length
 impedance = Zc * np.exp(resistance + 1j * phase_angle)

 return phase_angle, impedance

# ایجاد خطوط انتقال هوایی
lengths = np.linspace(0, length, 100)
phase_angles, impedances = zip(*[transmission_line_model(l, frequency, velocity_of_light, characteristic_impedance) for l in lengths])

# نمایش نتایج
plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.plot(lengths, np.angle(impedances), label='Phase Angle')
plt.title('Phase Angle vs. Length')
plt.xlabel('Length (m)')
plt.ylabel('Phase Angle (radians)')
plt.legend()

plt.subplot(122)
plt.plot(lengths, np.abs(impedances), label='Impedance Magnitude')
plt.title('Impedance Magnitude vs. Length')
plt.xlabel('Length (m)')
plt.ylabel('Impedance Magnitude (Ohms)')
plt.legend()

plt.tight_layout()
plt.show()