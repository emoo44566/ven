import simpy
import numpy as np

class PowerPlant:
   def init(self, env, name, capacity, voltage, frequency):
     self.env = env
     self.name = name
     self.capacity = capacity
     self.voltage = voltage
     self.frequency = frequency
     self.generator = simpy.Resource(env, capacity=1)

def generator_behavior(env, generator):
   while True:
     yield env.timeout(np.random.exponential(scale=1)) # Time between events
     print(f"{env.now}: {generator.name} generating power")

# Create the simulation environment
env = simpy.Environment()

# Create generators
generator1 = PowerPlant(env, name="Generator 1", capacity=100, voltage=230, frequency=60)
generator2 = PowerPlant(env, name="Generator 2", capacity=120, voltage=230, frequency=60)

# Start generator behaviors
env.process(generator_behavior(env, generator1))
env.process(generator_behavior(env, generator2))

# Run the simulation for a specific duration (e.g., 10 time units)
env.run(until=10)