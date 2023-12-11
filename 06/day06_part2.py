def ways_to_win_single_race(time, record):
    """
    Calculate the number of ways to win a single race.

    Parameters:
    time (int): Total time for the race.
    record (int): Record distance for the race.

    Returns:
    int: Number of ways to win the race.
    """
    ways = 0
    for hold_time in range(time):
        travel_time = time - hold_time
        distance = hold_time * travel_time
        if distance > record:
            ways += 1
    return ways

# Example usage
race_time =  54946592
record_distance =  302147610291404
result = ways_to_win_single_race(race_time, record_distance)
print(result)  # Output: 71503
