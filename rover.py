import math

# ENDG 233 Fall 2023
# Portfolio Project 1 - rover.py
# This script computes the travel time for a rover by taking into account its specific parameters and any storm conditions.
# Original Author: Mujtaba Zia

# Prompt the user to input the rover number, mission distance, and whether a storm is expected.
rover_choice = int(input("Which rover would you like to move? "))  # Get the rover identifier
mission_distance = int(input("Enter the mission distance in km: "))  # Get the distance for the mission in kilometers
storm_forecast = input("Will there be a storm (True or False)? ")  # Determine if a storm is forecasted

# Validate that the selected rover number is among the available options.
if rover_choice not in [1, 2, 3]:
    print("The chosen rover number is invalid.")
    exit()

# Set the rover parameters based on the user's selection.
if rover_choice == 1:  # Charlie rover
    battery_capacity = 100         # Battery capacity in kW
    energy_efficiency = 50 / 100     # Energy usage in kWh per km
    solar_output = 5               # Solar panel capacity in kW
    cruising_speed = 5             # Average speed in km/h
elif rover_choice == 2:  # Alpha rover
    battery_capacity = 130         # Battery capacity in kW
    energy_efficiency = 40 / 100     # Energy consumption per km in kWh/km
    solar_output = 8               # Solar capacity in kW
    cruising_speed = 4             # Average speed in km/h
elif rover_choice == 3:  # November rover
    battery_capacity = 80          # Battery capacity in kW
    energy_efficiency = 30 / 100     # Consumption rate in kWh per km
    solar_output = 4               # Solar panel output in kW
    cruising_speed = 6             # Average speed in km/h

# Calculate the base travel time without considering any recharging stops.
total_travel_time = mission_distance / cruising_speed

# Compute how far the rover can travel on a full battery charge.
max_distance_one_charge = battery_capacity / energy_efficiency

# If the mission distance exceeds the maximum range per charge, determine additional charging time.
if mission_distance >= max_distance_one_charge:
    extra_charges_needed = math.ceil(mission_distance / max_distance_one_charge - 1)
    charging_time = (battery_capacity / solar_output) * extra_charges_needed
    total_travel_time += charging_time

# Increase the travel time by 20% if a storm is predicted.
if storm_forecast == "True":
    total_travel_time *= 1.2

# Output the final calculated travel time.
print("The total travel time for Rover {0} to travel {1:0.1f} km is {2:0.1f} hours.".format(rover_choice, mission_distance, total_travel_time))
