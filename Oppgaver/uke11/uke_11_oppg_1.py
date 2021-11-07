"""A module for the functions mean, median and mode"""

def mean(data:list) -> float:
    """Return the mean of a list of numbers"""
    sum_data = 0
    for num in data:
        sum_data += num
    return sum_data / len(data)


def median(data:list) -> float:
    """Return the median of a list of numbers"""
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 0:
        sum_two_middle = sorted_data[int(len(sorted_data)/2)] + sorted_data[int(len(sorted_data)/2 - 1)]
        return sum_two_middle / 2
    return sorted_data[int(len(sorted_data) / 2)]


def mode(data:list):
    """Take in list of numbers and return the most accuring number"""
    # Create dict for counting all numbers
    numbers = {}
    # Add all numbers to the dict
    # Not really a set but i dont want to sort the data
    data_set = []
    for number in data:
        if number not in data_set:
            data_set.append(number)
    for number in data_set:
        numbers[number] = 1

    # Loop over list and update count
    for num in data:
        numbers[num] += 1

    # Loop over dict to find mode
    most_occuring = 0
    most_occuring_count = 0
    for i,(key, count) in enumerate(numbers.items()):
        if count > most_occuring_count:
            most_occuring = key
            most_occuring_count = count

    return most_occuring
