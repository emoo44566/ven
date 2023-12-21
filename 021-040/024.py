class PowerTransformer:
   def init(self, primary_voltage, secondary_voltage, power_rating):
     self.primary_voltage = primary_voltage
     self.secondary_voltage = secondary_voltage
     self.power_rating = power_rating

   def calculate_current(self):
     primary_current = self.power_rating / self.primary_voltage
     return primary_current

   def display_information(self):
     print(f"Primary Voltage: {self.primary_voltage} V")
     print(f"Secondary Voltage: {self.secondary_voltage} V")
     print(f"Power Rating: {self.power_rating} VA")

# نمونه ایجاد یک ترانسفورماتور با ولتاژ اولیه 220 ولت، ولتاژ ثانویه 110 ولت و توان 1000 وات
my_transformer = PowerTransformer(primary_voltage=220, secondary_voltage=110, power_rating=1000)

# نمایش اطلاعات ترانسفورماتور
my_transformer.display_information()

# محاسبه جریان در سیم اولیه
current = my_transformer.calculate_current()
print(f"Primary Current: {current} A")