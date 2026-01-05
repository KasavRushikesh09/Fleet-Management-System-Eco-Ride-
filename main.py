from fleet_manager import Fleetmanager

class EcoRideMain:
    def greet(self):
       print("Welcome to Eco-Ride urban Mobility system")
    def main(self):
        self.greet()
        fm = Fleetmanager()
        fm.add_hub()
        fm.add_vehicle_to_hub()
        fm.add_vehicle_to_hub()
if __name__ == "__main__":
    app = EcoRideMain()
    app.main()



