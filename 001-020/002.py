import numpy as np
import matplotlib.pyplot as plt

def load_curve(hour):
    # یک تابع منحنی بار ساختگی
    return 100 + 50 * np.sin((hour / 24) * 2 * np.pi)

def daily_average_load(load_curve):
    # محاسبه میانگین بار روزانه
    daily_load = [load_curve(hour) for hour in range(24)]
    return np.mean(daily_load)

def daily_variation_coefficient(load_curve):
    # محاسبه ضریب تغییر روزانه
    daily_load = [load_curve(hour) for hour in range(24)]
    max_load = np.max(daily_load)
    min_load = np.min(daily_load)
    return (max_load - min_load) / np.mean(daily_load)

# تابع منحنی بار را رسم کن
hours = np.arange(0, 24, 0.1)
load_values = [load_curve(hour) for hour in hours]

plt.plot(hours, load_values)
plt.title('Load Curve for Variable Power System')
plt.xlabel('Hour of the Day')
plt.ylabel('Load (MW)')
plt.grid(True)
plt.show()

# محاسبه متوسط بار و ضریب تغییر روزانه
avg_load = daily_average_load(load_curve)
variation_coefficient = daily_variation_coefficient(load_curve)

print(f'Daily Average Load: {avg_load} MW')
print(f'Daily Variation Coefficient: {variation_coefficient:.2f}')