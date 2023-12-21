import numpy as np
import matplotlib.pyplot as plt

def plot_three_phase_connections():
   # اتصال‌های ترانسفورماتور سه فاز
   connections = ['Y-Y', 'Δ-Y', 'Y-Δ', 'Δ-Δ']

   for connection in connections:
     # تولید داده‌های سه فاز
     time = np.linspace(0, 1, 1000)
     phase_a = np.sin(2 * np.pi * 50 * time)
     phase_b = np.sin(2 * np.pi * 50 * time - (2/3) * np.pi)
     phase_c = np.sin(2 * np.pi * 50 * time + (2/3) * np.pi)

     # ترسیم نمودارها
     plt.figure()
     plt.title(f'Three-Phase Transformer Connection: {connection}')
     plt.plot(time, phase_a, label='Phase A')
     plt.plot(time, phase_b, label='Phase B')
     plt.plot(time, phase_c, label='Phase C')
     plt.xlabel('Time')
     plt.ylabel('Voltage')
     plt.legend()
     plt.grid(True)

   plt.show()

# ترسیم اتصال‌های ترانسفورماتور سه فاز
plot_three_phase_connections()