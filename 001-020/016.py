import numpy as np

class Impedance:
   def init(self, resistance, reactance):
     self.resistance = resistance
     self.reactance = reactance

class Load:
   def init(self, impedance):
     self.impedance = impedance

class Line:
   def init(self, impedance):
     self.impedance = impedance

class PowerNetwork:
   def init(self):
     # Define impedances
     impedance_source1 = Impedance(resistance=1, reactance=2)
     impedance_source2 = Impedance(resistance=2, reactance=3)
     impedance_load1 = Impedance(resistance=3, reactance=4)
     impedance_load2 = Impedance(resistance=2, reactance=1)

     # Define loads
     load_star = Load(impedance_load1)
     load_triangle = Load(impedance_load2)

      # Define lines
     line1 = Line(impedance_source1)
     line2 = Line(impedance_source2)

     # Connect loads to lines
     line1_loads = [load_star, load_triangle]
     line2_loads = [load_star, load_triangle]

     self.lines = {line1: line1_loads, line2: line2_loads}

   def calculate_currents(self):
     currents = {}
     for line, loads in self.lines.items():
       total_impedance = line.impedance
       for load in loads:
           total_impedance = Impedance(
             resistance=total_impedance.resistance + load.impedance.resistance,
             reactance=total_impedance.reactance + load.impedance.reactance
           )

       voltage = np.sqrt(3) * 400 # Assuming a balanced three-phase system with 400V line voltage
       current = voltage / total_impedance.resistance
       currents[line] = current

     return currents

# Create the power network
power_network = PowerNetwork()

# Calculate currents
currents = power_network.calculate_currents()

# Display results
for line, current in currents.items():
   print(f"Current in Line: {line} is {current} A")