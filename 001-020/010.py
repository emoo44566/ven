import numpy as np
import matplotlib.pyplot as plt

# پارامترهای مدار
V_line = 400 # ولتاژ خط (V)
Z_load = 10 + 5j # امپدانس بار (Ohm)
Z_line = 5 + 2j # امپدانس خط (Ohm)

# محاسبه جریان متغیر
I_line = V_line / Z_line

# محاسبه توان متغیر
S_load = np.power(np.abs(I_line), 2) * Z_load

# نمایش نتایج
print(f"جریان متغیر: {I_line:.2f} امپر")
print(f"توان متغیر بار: {S_load:.2f} وار")

# رسم دیاگرام فازهای مختلف
phases = ['A', 'B', 'C']
fig, ax = plt.subplots()
ax.plot(np.real(I_line), label='Real')
ax.plot(np.imag(I_line), label='Imaginary')
ax.set_xticks(range(len(phases)))
ax.set_xticklabels(phases)
ax.set_xlabel('Phase')
ax.set_ylabel('Current (A)')
ax.legend()
plt.title('Three-Phase Balanced Circuit Current')
plt.show()