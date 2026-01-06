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
  # UC8
        print("\n --- Search Vehicle by Hub --- ")
        hub_name = input("Enter hub to search: ")
        vehicles = fm.search_by_hub(hub_name)

        for v in vehicles:
            print(v.vehicle_id,v.model,v.get_battery_percentage())

        print("\n ~~~ Vehicle with Battery > 80% ~~~")
        high_battery = fm.search_high_battery_vehicles()

        for v in high_battery:
            print(v.vehicle_id,v.model,v.get_battery_percentage())
    #UC9
        print("\n ---  Categorized View (UC 9) ---")
        categorized = fm.categorized_view()

        print("\n --- Car ---")
        for car in categorized["Car"]:
            print(car.vehicle_id,car.model,car.get_battery_percentage())

        print("\n --- Scooters --- ")
        for scooter in categorized["Scooter"]:
            print(scooter.vehicle_id,scooter.model,scooter.get_battery_percentage())

    #UC-10
        print("\n --- Fleet Analytics (UC 10) ---")
        analytics = fm.fleet_analytics()
        print("---------------------")
        print(f"Available Vehicles   :{analytics['Available']}")
        print(f"Vehicles On Trip     :{analytics['On Trip']}")
        print(f"under maintenance    :{analytics['Under Maintenance']}")
        print("---------------------")

if __name__ == "__main__":
    app = EcoRideMain()
    app.main()



