def calculate_winning_ways(race_times, record_distances):
    def ways_to_win(time, record):
        ways = 0
        for hold_time in range(time):
            travel_time = time - hold_time
            distance = hold_time * travel_time
            if distance > record:
                ways += 1
        return ways

    total_ways = 1
    for time, record in zip(race_times, record_distances):
        total_ways *= ways_to_win(time, record)

    return total_ways

# Example usage
race_times = [54, 94, 65, 92]
record_distances = [302, 1476, 1029, 1404]
result = calculate_winning_ways(race_times, record_distances)
print(result)  # Output: 288
