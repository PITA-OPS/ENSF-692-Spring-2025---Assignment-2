# input_processing.py
# PETER OSAADE, ENSF 692 Spring 2025
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    def __init__(self):
        self.traffic_light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"

    def update_status(self, choice, value):
        """
        Updates the appropriate sensor status based on user input.

        Parameters:
        choice (an integer value): The menu selection are: (1, 2, or 3)
        value (a string value): The new status value
        """
        if choice == 1:
            self.traffic_light = value
        elif choice == 2:
            self.pedestrian = value
        elif choice == 3:
            self.vehicle = value

            

# The sensor object should be passed to this function to print the action message and current status
"""
    Determines and prints the appropriate driving action based on sensor values.
    Also displays the current status of all monitored conditions.

    Parameters:
    sensor (Sensor): The sensor object with current statuses
"""
def print_message(sensor):
    print("\n--- Action Message ---") #Prints on a new line

    if sensor.traffic_light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        print("STOP")
    elif sensor.traffic_light == "yellow" and (sensor.pedestrian == "no" or sensor.vehicle == "no"):
        print("Caution")
    elif sensor.traffic_light == "green" and (sensor.pedestrian == "no" or sensor.vehicle == "no"):
        print("Proceed")

    print("\n--- Current Sensor Status ---")
    print(f"Traffic Light: {sensor.traffic_light}")
    print(f"Pedestrian: {sensor.pedestrian}")
    print(f"Vehicle: {sensor.vehicle}\n")



def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()

    while True:
        try:
            choice = int(input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: "))
        except ValueError:
            print("Invalid input. Please enter a number: 0, 1, 2, or 3.\n")
            continue

        if choice == 0:
            print("Program terminated.")
            break
        elif choice == 1:
            value = input("Enter traffic light color (green, yellow, red): ")
            if value not in ["green", "yellow", "red"]:
                print("Invalid input. Must be 'green', 'yellow', or 'red'.\n")
                continue
        elif choice == 2:
            value = input("Is there a pedestrian? (yes or no): ")
            if value not in ["yes", "no"]:
                print("Invalid input. Must be 'yes' or 'no'.\n")
                continue
        elif choice == 3:
            value = input("Is there a vehicle? (yes or no): ")
            if value not in ["yes", "no"]:
                print("Invalid input. Must be 'yes' or 'no'.\n")
                continue
        else:
            print("Invalid menu option. Enter 0, 1, 2, or 3.\n")
            continue

        sensor.update_status(choice, value)
        print_message(sensor)





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()



    

