import random

class MarsEnvironment:
    def __init__(self):
        self.locations = ["Location A", "Location B", "Location C", "Location D"]
        self.location_conditions = {loc: random.randint(0, 1) for loc in self.locations}
    
    def change_environment(self):
        for loc in self.locations:
            self.location_conditions[loc] = random.randint(0, 1)
    
    def display_environment(self):
        for loc, condition in self.location_conditions.items():
            rock_status = "Rocks available" if condition == 1 else "No rocks"
            print(f"{loc}: {rock_status}")

class RoverAgent:
    def __init__(self, environment):
        self.environment = environment
        self.sampled_locations = set()
        self.samples_collected = 0
    
    def explore(self):
        print("\nRover starting exploration venture...")
        for loc in self.environment.locations:
            if loc not in self.sampled_locations and self.environment.location_conditions[loc] == 1:
                print(f"Sampling rocks at {loc}")
                self.sampled_locations.add(loc)
                self.samples_collected += 1
            else:
                print(f"{loc} has no rocks or already sampled.")
    
    def display_performance(self):
        print(f"\nRover Performance Summary:")
        print(f"Total samples collected: {self.samples_collected}")
        print(f"Locations sampled: {', '.join(self.sampled_locations)}")

class RoverPerformance:
    def __init__(self):
        self.environment = MarsEnvironment()
        self.rover = RoverAgent(self.environment)
    
    def run_simulation(self):
        print("Mars Environment (Before 1st exploration):")
        self.environment.display_environment()
        self.rover.explore()

        self.environment.change_environment()

        print("\nMars Environment (Before 2nd exploration):")
        self.environment.display_environment()
        self.rover.explore()

        self.rover.display_performance()

simulation = RoverPerformance()
simulation.run_simulation()
