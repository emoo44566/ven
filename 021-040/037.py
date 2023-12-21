class VoltageControlSystem:
   def init(self, setpoint_voltage, kp_voltage, ki_voltage, kd_voltage):
     self.setpoint_voltage = setpoint_voltage
     self.kp_voltage = kp_voltage
     self.ki_voltage = ki_voltage
     self.kd_voltage = kd_voltage
     self.prev_error_voltage = 0
     self.integral_voltage = 0

   def voltage_control(self, measured_voltage):
     error_voltage = self.setpoint_voltage - measured_voltage
     self.integral_voltage += error_voltage
     derivative_voltage = error_voltage - self.prev_error_voltage

     output_voltage = (
       self.kp_voltage * error_voltage +
       self.ki_voltage * self.integral_voltage +
       self.kd_voltage * derivative_voltage
     )

     self.prev_error_voltage = error_voltage
     return output_voltage


class PhaseAngleControlSystem:
   def init(self, setpoint_phase_angle, kp_phase_angle, ki_phase_angle, kd_phase_angle):
     self.setpoint_phase_angle = setpoint_phase_angle
     self.kp_phase_angle = kp_phase_angle
     self.ki_phase_angle = ki_phase_angle
     self.kd_phase_angle = kd_phase_angle
     self.prev_error_phase_angle = 0
     self.integral_phase_angle = 0

   def phase_angle_control(self, measured_phase_angle):
     error_phase_angle = self.setpoint_phase_angle - measured_phase_angle
     self.integral_phase_angle += error_phase_angle
     derivative_phase_angle = error_phase_angle - self.prev_error_phase_angle

     output_phase_angle = (
       self.kp_phase_angle * error_phase_angle +
       self.ki_phase_angle * self.integral_phase_angle +
       self.kd_phase_angle * derivative_phase_angle
     )

     self.prev_error_phase_angle = error_phase_angle
     return output_phase_angle


# تنظیم پارامترهای کنترل ولتاژ
setpoint_voltage = 120.0 # ولتاژ مطلوب
kp_voltage = 0.5 # ضریب متغیر متناسب
ki_voltage = 0.1 # ضریب متغیر انتگرال
kd_voltage = 0.01 # ضریب متغیر انحراف

# تنظیم پارامترهای کنترل زاویه فاز
setpoint_phase_angle = 0.0 # زاویه فاز مطلوب
kp_phase_angle = 0.1 # ضریب متغیر متناسب
ki_phase_angle = 0.01 # ضریب متغیر انتگرال
kd_phase_angle = 0.001 # ضریب متغیر انحراف

# ساخت شیء کنترل ولتاژ
voltage_control_system = VoltageControlSystem(setpoint_voltage, kp_voltage, ki_voltage, kd_voltage)

# ساخت شیء کنترل زاویه فاز
phase_angle_control_system = PhaseAngleControlSystem(setpoint_phase_angle, kp_phase_angle, ki_phase_angle, kd_phase_angle)

# شبیه‌سازی کنترل ولتاژ و زاویه فاز
for _ in range(100):
   measured_voltage = 110.0 # فرض یک ولتاژ اندازه‌گیری شده
   control_output_voltage = voltage_control_system.voltage_control(measured_voltage)

   measured_phase_angle = 2.0 # فرض یک زاویه فاز اندازه‌گیری شده
   control_output_phase_angle = phase_angle_control_system.phase_angle_control(measured_phase_angle)

   print("Control Output Voltage:", control_output_voltage)
   print("Control Output Phase Angle:", control_output_phase_angle)