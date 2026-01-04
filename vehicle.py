class Vehicle:
     def __init__(self, vehicle_id, model, battery_percentage):
         self.vehicle_id = vehicle_id
         self.model = model
         self.battery_percentage = battery_percentage
         #private attribute
         self.__maintenance_status = "Good"
         self.__rental_price = 1500

        #correct setter call
         self.set_battery_percentage(battery_percentage)

     #-----------Battery Percentage-------
     def get_battery_percentage(self):
         return self.__battery_percentage
     def set_battery_percentage(self, battery_percentage):
         if 0 <= battery_percentage <= 100:
             self.__battery_percentage = battery_percentage
         else:
             print("Battery percentage must be between 0 and 100")
     # ---------Maintenance Status ----------
     def get_maintenance_status(self):
         return self.__maintenance_status
     def set_maintenance_status(self, status):
         self.__maintenance_status = status

    # --------Rental Price --------
     def get_rental_price(self):
        return self.__rental_price

     def set_rental_price(self,price):
        if price > 0:
            self.__rental_price = price
        else:
            print("Rental price must be greater than 0")
if __name__ == "__main__":
         v1 = Vehicle("v101","Tesla Model 3",85)

         # print("Vehicle ID:",v1.vehicle_id)
         # print("Model:",v1.model)
         # print("Battery Percentage:",v1.battery_percentage)

         print("Battery:",v1.get_battery_percentage(),"%")
         print("Maintenance status:",v1.get_maintenance_status())
         print("Rental Price:",v1.get_rental_price())

         v1.set_battery_percentage(120)
         v1.set_battery_percentage(80)

         v1.set_rental_price(-500)
         v1.set_rental_price(1200)
