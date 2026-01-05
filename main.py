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

        print("\n --- Search Vehicle by Hub --- ")
        hub_name = input("Enter hub to search: ")
        vehicles = fm.search_by_hub(hub_name)

        for v in vehicles:
            print(v.vehicle_id,v.model,v.get_battery_percentage())

        print("\n ~~~ Vehicle with Battery > 80% ~~~")
        high_battery = fm.search_high_battery_vehicles()

        for v in high_battery:
            print(v.vehicle_id,v.model,v.get_battery_percentage())

if __name__ == "__main__":
    app = EcoRideMain()
    app.main()



