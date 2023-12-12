import sys
import json

def interpret_blocks(input_blocks):
    seeds = list(map(int, input_blocks[0].split(':')[1].split()))
    maps = {}
    current_map_name = ''
    for block in input_blocks[1:]:
        for line in block.splitlines():
            if ':' in line:
                current_map_name = line.split(' ')[0].strip().lower().replace('-', '_')
                maps[current_map_name] = []
            else:
                target_start, source_start, range_length = map(int, line.split())
                maps[current_map_name] = {
                    'action': target_start - source_start,
                    'target_start': target_start,
                    'target_end': target_start + range_length,
                    'source_start': source_start,
                    'source_end': source_start + range_length,
                    'range_length': range_length
                }

    return {'seeds': seeds, **maps}

def do_mapping(s):
    seeds = s['seeds']
    x = {}
    for seed in seeds:
        soil = _get_mapped_value(s, seed, 'seed_to_soil')
        fertilizer = _get_mapped_value(s, soil, 'soil_to_fertilizer')
        water = _get_mapped_value(s, fertilizer, 'fertilizer_to_water')
        light = _get_mapped_value(s, water, 'water_to_light')
        temperature = _get_mapped_value(s, light, 'light_to_temperature')
        humidity = _get_mapped_value(s, temperature, 'temperature_to_humidity')
        location = _get_mapped_value(s, humidity, 'humidity_to_location')
        x[seed] = {
            'soil' : soil,
            'fertilizer' : fertilizer,
            'water' : water,
            'light' : light,
            'temperature' : temperature,
            'humidity' : humidity,
            'location' : location
        }
    return x

def _get_mapped_value(s, source_val, mapping):
    if s[mapping]['source_start'] <= source_val <= s[mapping]['source_end']:
        return source_val + s[mapping]['action']
    return source_val

def main():
    with open('./2023/05test.txt') as f:
    # with open('./2023/05input.txt') as f:
        input_blocks = f.read().split('\n\n')
    start_state = interpret_blocks(input_blocks)
    print(start_state)
    data_p1 = do_mapping(start_state)
    print(json.dumps(data_p1, sort_keys=False, indent=2))
    part1 = min(item['location'] for item in data_p1.values())
    # part2 = sum_scores(cards, 'instances')
    print(f"{part1 = }")
    # print(f"{part2 = }")

if __name__ == '__main__':
    sys.exit(main())
