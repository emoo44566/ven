class PIDController:
   def init(self, setpoint, kp, ki, kd):
     self.setpoint = setpoint
     self.kp = kp
     self.ki = ki
     self.kd = kd
     self.prev_error = 0
     self.integral = 0

   def compute(self, measured_value):
     error = self.setpoint - measured_value
     self.integral += error
     derivative = error - self.prev_error

     output = self.kp * error + self.ki * self.integral + self.kd * derivative

     self.prev_error = error
     return output

# تنظیم پارامترهای PID
setpoint_voltage = 12.0 # ولتاژ مطلوب
kp_value = 0.5 # ضریب متغیر متناسب
ki_value = 0.1 # ضریب متغیر انتگرال
kd_value = 0.01 # ضریب متغیر انحراف

# ساخت شیء PID Controller
pid_controller = PIDController(setpoint_voltage, kp_value, ki_value, kd_value)

# شبیه‌سازی کنترل ولتاژ
for _ in range(100):
   measured_voltage = 10.0 # فرض یک ولتاژ اندازه‌گیری شده
   control_output = pid_controller.compute(measured_voltage)
   print("Control Output:", control_output)