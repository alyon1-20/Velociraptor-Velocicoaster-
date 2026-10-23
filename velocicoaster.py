class VelociCoaster:
"""Represents the physical roller coaster."""

def __init__(self, name, max_speed):
    self.name = name
    self.max_speed = max_speed
    self.status = "Stopped"
    self.ride_cycles = 0

def start_ride(self):
    """Starts the roller coaster ride."""
    self.status = "Running"
    print(f'\n The {self.name} is now Running!')

    def stop_ride(self):
        '''Stops the roller coaster ride.'''
        self.status = "Stopped"
        print(f'\n The {self.name} has been stopped.')

    def complete_cycle(self):
        '''Adds one completed ride cycle.'''
        self.ride_cycles += 1 
        print(f'\n The {self.name} has completed {self.ride_cycles} ride cycles.')

        class DigitalTwin:
        """Represents the digital twin monitoring the ride."""

        def _init_(self, ride, maintenance_threshold):
            self.ride = ride
            self.maintenance_threshold = maintenance_threshold

            def monitor_ride(self):
                """Displays current ride information."""
        print("\n----- DIGITAL TWIN STATUS -----")
        print(f"Ride Name: {self.ride.name}")
        print(f"Status: {self.ride.status}")
        print(f"Max Speed: {self.ride.max_speed} mph")
        print(f"Completed Cycles: {self.ride.ride_cycles}")

        def check_maintenance(self):
        """Determines if maintenance is needed."""
        if self.ride.ride_cycles >= self.maintenance_threshold:
            print("⚠️ Maintenance Required!")
        else:
            print("✅ Ride Operating Normally.")

         def generate_report(self):
        """Prints a summary report."""
        print("\n===== DAILY REPORT =====")
        print(f"Ride: {self.ride.name}")
        print(f"Total Cycles: {self.ride.ride_cycles}")
        print(f"Status: {self.ride.status}")

velocicoaster = VelociCoaster("VelociCoaster", 70)

twin = DigitalTwin(velocicoaster, 5)

velocicoaster.start_ride()

# Simulate multiple ride cycles
for cycle in range(6):
    velocicoaster.complete_cycle()
    twin.monitor_ride()
    twin.check_maintenance()

# Stop ride
velocicoaster.stop_ride()

# Generate final report
twin.generate_report()