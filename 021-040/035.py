from sympy import symbols, Eq, solve

# تعریف متغیرها
Vin, Vout, N1, N2, Iin, Iout = symbols('Vin Vout N1 N2 Iin Iout') # ولتاژ‌ها و تعداد دور پیچ‌ها و جریان‌ها

# معادلات اصلی ترانسفورماتور تنظیم‌کننده
eq1 = Eq(Vout, N2/N1 * Vin)
eq2 = Eq(Iout, N1/N2 * Iin)

# حل معادلات
sol = solve((eq1, eq2), (Vout, Iout))

# چاپ نتایج
print("نتایج:")
print("ولتاژ خروجی ترانسفورماتور (Vout):", sol[Vout])
print("جریان خروجی ترانسفورماتور (Iout):", sol[Iout])