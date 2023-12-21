import numpy as np
import matplotlib.pyplot as plt

def load_curve(day_of_year):
    # یک تابع منحنی بار ساختگی برای نمونه
    return 100 + 50 * np.sin((day_of_year / 365) * 2 * np.pi)

def annual_average_load(load_curve):
    # محاسبه متوسط بار سالانه
    daily_load = [load_curve(day) for day in range(1, 366)]
    return np.mean(daily_load)

def annual_variation_coefficient(load_curve):
    # محاسبه ضریب تغییر سالانه
    daily_load = [load_curve(day) for day in range(1, 366)]
    max_load = np.max(daily_load)
    min_load = np.min(daily_load)
    return (max_load - min_load) / np.mean(daily_load)

# تابع منحنی بار را رسم کن
days_of_year = np.arange(1, 366, 1)
load_values = [load_curve(day) for day in days_of_year]

plt.plot(days_of_year, load_values)
plt.title('Load Curve for Annual Power System')
plt.xlabel('Day of the Year')
plt.ylabel('Load (MW)')
plt.grid(True)
plt.show()

# محاسبه متوسط بار و ضریب تغییر سالانه
avg_load = annual_average_load(load_curve)
variation_coefficient = annual_variation_coefficient(load_curve)

print(f'Annual Average Load: {avg_load} MW')
print(f'Annual Variation Coefficient: {variation_coefficient:.2f}')