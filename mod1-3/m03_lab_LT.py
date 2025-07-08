# m03_lab_LT.py
# Logan Till
# 2025-06-28
# Auto Details Program


# this will print the title of the program
print('\n***************************************')
print('Auto Details Program (by Logan Till)')
print('***************************************\n')


# Import Libraries
# Input File
# Output File
# Constants
WELCOME = ('Welcome!\nThis program collect data about an automobile.\n')
GOODBYE = ('Thank you for using this program!')
# Variables



# Program Starts Here
# Print Welcome Message
print(WELCOME)

# Main Loop
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
   def __init__(self, vehicle_type, year, make, model, door, roof):
      super().__init__(vehicle_type)
      self.year = year
      self.make = make
      self.model = model
      self.door = door
      self.roof = roof

while True:
   # Collect the type of vehicle from the user
   vehicle_type = input('Enter the type of vehicle (e.g. car, boat, etc.): ').lower()

   # If the vehicle type is 'car', collect additional details
   if vehicle_type == 'car':
      year = input('Enter the year of the car(e.g. 2017): ')
      make = input('Enter the make of the car(e.g. Hyundai): ')
      model = input('Enter the model of the car(e.g. Elantra): ')
      door = input('Enter the number of doors on the car(2 or 4): ')
      roof = input('Does the car have a sunroof? (yes/no): ')

      # Create an instance of Automobile
      my_car = Automobile(vehicle_type, year, make, model, door, roof)
      
      # Display the details
      print(f'\nVehicle Type: {my_car.vehicle_type}')
      print(f'Year: {my_car.year}')
      print(f'Make: {my_car.make}')
      print(f'Model: {my_car.model}')
      print(f'Doors: {my_car.door}')
      print(f'Sunroof: {my_car.roof}\n')
      
      # Ask if the user wants to enter another vehicle
      another = input('Would you like to enter another? (yes/no): ').lower()
      if another != 'yes':
         break
      
   # If the vehicle type is unsupported
   else: 
      print('Sorry. That vehicle type is not yet supported.')
# End of Program
print(GOODBYE)