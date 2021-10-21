"""Write a program that presents a dictonary of weather stations"""

weather_stations = {
    "Bergen" : {
        "Wind speed": 3.6,
        "Wind direction": "northeast",
        "Precipitation": 5.2,
        "Device": "WeatherMaster500"
    },
    "Trondheim" : {
        "Wind speed": 8.2,
        "Wind direction": "northwest",
        "Precipitation": 0.2,
        "Device": "ClimateDiscoverer3000"
    },
    "Svalbard" : {
        "Wind speed": 7.5,
        "Wind direction": "southwest",
        "Precipitation": 1.1,
        "Device": "WeatherFinder5.0"
    }
}


for key in weather_stations:
    print(f"The weather in {key}:")
    values = weather_stations[key].values()
    values_list = []
    for value in values:
        values_list.append(value)
    print(f"The wind speed is {values_list[0]} m/s in the {values_list[1]} direction and the precipitation is {values_list[2]} mm.")
    print(f"The measurement was done using the {values_list[3]} weather station.\n")
