from sympy import symbols, Eq, solve

# تعریف متغیرها
V1, V2, N1, N2 = symbols('V1 V2 N1 N2') # ولتاژ‌ها و تعداد دور پیچ‌ها برای ترانسفورماتور
V_out, N_out, N_in = symbols('V_out N_out N_in') # ولتاژ و تعداد دور پیچ‌ها برای تغییردهنده تپ

# معادلات اصلی ترانسفورماتور
eq1 = Eq(V1 / V2, N1 / N2)

# معادلات تغییردهنده تپ
eq2 = Eq(V_out / V1, N_out / N_in)

# حل معادلات
sol = solve((eq1, eq2), (V1, V2, N1, N2))

# چاپ نتایج
print("نتایج:")
print("ولتاژ ورودی ترانسفورماتور (V1):", sol[V1])
print("ولتاژ خروجی ترانسفورماتور (V2):", sol[V2])
print("تعداد دور پیچ‌های ترانسفورماتور (N1, N2):", sol[N1], sol[N2])
print("ولتاژ خروجی تغییردهنده تپ (V_out):", sol[V_out])
print("تعداد دور پیچ تغییردهنده تپ (N_out):", sol[N_out])
print("تعداد دور پیچ ورودی تغییردهنده تپ (N_in):", sol[N_in])