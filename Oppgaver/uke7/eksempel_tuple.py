# a tuple with three elements:
bergen = ("rain", 60.39, 5.32)  # bergen weather, latitude, longitude

# a tuple with one element (notice the comma - what happens if you remove the comma?)
bergen_weather = ("rain")

print("Two tuples:")
print(f"bergen = {bergen}\nbergen_weather = {bergen_weather}\n")

print("Tuple unpacking:")
weather, latitude, longitude = bergen  # we can assign multiple variables to values in a tuple
print(f"weather = {weather}")
print(f"latitude = {latitude}")
print(f"longitude = {longitude}")

print("Lists of tuples:")
# here is a list of tuples
bergen_temp_forecast = [(16.0, "onsdag"), (14.0, "torsdag"), (13.0, "fredag")]

# we can unpack them automatically while going through the list
for temp, day in bergen_temp_forecast:
    print(f"På {day} blir det {temp} grader.")