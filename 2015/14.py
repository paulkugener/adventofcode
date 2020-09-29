#! python3

from collections import defaultdict
from pprint import pprint

reindeers = defaultdict(dict)

with open("./2015/14input", "r") as f:
    for line in f:
        reindeer, _, _, t_distance, _, _, t_duration, _, _, _, _, _, _, r_duration, _ = line.rstrip().split(" ")

        reindeers[reindeer] = {
            'travel_distance': int(t_distance), 
            'travel_duration': int(t_duration), 
            'rest_duration': int(r_duration), 
            'result_distance': -1
        }

for reindeer in reindeers:
    total_distance = 0
    i = 1
    current_action = "rest"
    current_time_left = 0
    while i <= 2503:
        if current_time_left == 0 and current_action == "rest":
            current_time_left = reindeers[reindeer]['travel_duration']
            current_action = "travel"
        elif current_time_left == 0 and current_action == "travel":
            current_time_left = reindeers[reindeer]['rest_duration']
            current_action = "rest"

        if current_action == "travel":
            total_distance += reindeers[reindeer]['travel_distance']
            
        current_time_left -= 1
        i += 1
    reindeers[reindeer]['result_distance'] = total_distance

#pprint(reindeers)

sorted_reindeers = sorted(reindeers.items(), key=lambda x: x[1]['result_distance'], reverse=True)

pprint(sorted_reindeers)

# TODO: part2
