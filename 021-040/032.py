from sympy import symbols, Eq, solve

# تعریف متغیرها
V1, V2, V3 = symbols('V1 V2 V3') # ولتاژ‌های ورودی
I1, I2, I3 = symbols('I1 I2 I3') # جریان‌های ورودی
N1, N2, N3 = symbols('N1 N2 N3') # تعداد دور پیچ‌ها

# نسبت تعداد دور پیچ‌ها
eq1 = Eq(V1 / V2, N1 / N2)
eq2 = Eq(V2 / V3, N2 / N3)

# نسبت ترانسفورماتوری (ولتاژ به جریان)
eq3 = Eq(V1 / I1, V2 / I2)
eq4 = Eq(V2 / I2, V3 / I3)

# حل معادلات
sol = solve((eq1, eq2, eq3, eq4), (V1, V2, V3, I1, I2, I3))

# چاپ نتایج
print("نتایج:")
print("V1 =", sol[V1])
print("V2 =", sol[V2])
print("V3 =", sol[V3])
print("I1 =", sol[I1])
print("I2 =", sol[I2])
print("I3 =", sol[I3])