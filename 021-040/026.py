class TransformerParameters:
   def init(self, primary_voltage, secondary_voltage, primary_turns, secondary_turns):
     self.primary_voltage = primary_voltage
     self.secondary_voltage = secondary_voltage
     self.primary_turns = primary_turns
     self.secondary_turns = secondary_turns

   def calculate_turns_ratio(self):
     turns_ratio = self.primary_turns / self.secondary_turns
     return turns_ratio

   def calculate_voltage_ratio(self):
     voltage_ratio = self.primary_voltage / self.secondary_voltage
     return voltage_ratio

# ورودی‌ها
primary_voltage = 220
secondary_voltage = 110
primary_turns = 1000
secondary_turns = 500

# محاسبه پارامترهای مدار معادل
transformer_params = TransformerParameters(primary_voltage, secondary_voltage, primary_turns, secondary_turns)

turns_ratio = transformer_params.calculate_turns_ratio()
voltage_ratio = transformer_params.calculate_voltage_ratio()

# نمایش نتایج
print(f"N: {turns_ratio}, V: {voltage_ratio}")