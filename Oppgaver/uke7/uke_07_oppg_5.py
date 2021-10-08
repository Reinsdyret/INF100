"""
Write a function, calibration_readout(), that takes in a list of floats and returns the same list,
but every index that % 12 == 0 is a tuple with ("Calibration hour", value)
"""

def calibration_readout(windSpeeds:list) -> list:
    """Takes in a list of floats and returns the same list, but every index that % 12 == 0 is a tuple with ("Calibration hour", value)"""
    newWindSpeeds = []
    for index, windspeed in enumerate(windSpeeds):
        if index % 12 == 0:
            newWindSpeeds.append(("Calibration hour", windspeed))
            continue
        newWindSpeeds.append(windspeed)

    return newWindSpeeds
