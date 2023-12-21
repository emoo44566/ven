from sympy import symbols, Eq, solve

# تعریف متغیرها
V_ref, V_actual = symbols('V_ref V_actual') # ولتاژ مرجع و ولتاژ واقعی
K_p, K_i = symbols('K_p K_i') # ضرایب کنترلی

# معادله کنترل PID
eq = Eq(V_actual, V_ref + K_p * (V_ref - V_actual) + K_i * V_actual)

# حل معادله برای به دست آوردن مقادیر K_p و K_i
sol = solve((eq), (K_p, K_i))

# چاپ نتایج
print("ضرایب کنترلی:")
print("K_p =", sol[K_p])
print("K_i =", sol[K_i])