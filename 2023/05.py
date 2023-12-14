import sys

def get_maps(input_blocks):
    maps = {}
    current_map_name = ''
    for block in input_blocks[1:]:
        for line in block.splitlines():
            if ':' in line:
                current_map_name = line.split(' ')[0].strip().lower().replace('-', '_')
                maps[current_map_name] = []
            else:
                target_start, source_start, range_length = map(int, line.split())
                maps[current_map_name].append({
                        'action': target_start - source_start,
                        'target_start': target_start,
                        'target_end': target_start + range_length-1,
                        'source_start': source_start,
                        'source_end': source_start + range_length-1,
                        'range_length': range_length
                    }
                )
    return maps

def get_seeds(input_blocks, variant = 'single'):   
    seeds = []
    seed_list = list(map(int, input_blocks[0].split(':')[1].split()))
    if variant == 'single':
        seeds = [[seed_list[i], 1] for i in range(len(seed_list))]
    elif variant == 'pair':
        seeds = [[seed_list[i], seed_list[i+1]] for i in range(0, len(seed_list), 2)]
    return seeds

def do_mapping(seeds, maps):
    current_values = seeds
    for map_key, map_slices in maps.items():
        print('start mapping..', map_key)
        new_values = []
        for c in current_values:
            slices_with_intersection = []
            for slice in map_slices:
                if has_intersection(c, slice):
                    slices_with_intersection.append(slice)
            if len(slices_with_intersection) > 0:
                new_values.extend(get_mapped_ranges(c, slices_with_intersection))
            else:
                new_values.append(c)
        current_values = new_values
    return current_values

def has_intersection(c, slice):
    start, length = c
    end = start + length-1
    if slice['source_start'] <= start <= slice['source_end'] \
            or slice['source_start'] <= end <= slice['source_end'] \
            or (start <= slice['source_start'] and slice['source_end'] <= end):
        return True
    return False

def get_mapped_ranges(c, slices):
    mapped_ranges = []
    ranges_to_treat = [c]
    while len(ranges_to_treat) > 0:
        range = ranges_to_treat.pop(0)
        start, length = range
        end = start + length-1
        no_slice_apply = True
        for slice in slices:
            if slice['source_start'] <= start and end <= slice['source_end']:
                # range completely in slice
                no_slice_apply = False
                mapped_ranges.append([start+slice['action'], length])
                break
            elif start < slice['source_start'] and end >= slice['source_start'] and end < slice['source_end']:
                # range starts before, and ends inside slice
                no_slice_apply = False
                pre_length = slice['source_start'] - start
                assert pre_length < length
                inside_length = length - pre_length
                ranges_to_treat.append([start, pre_length])
                mapped_ranges.append([slice['target_start'], inside_length])
                break
            elif start >= slice['source_start'] and start <= slice['source_end'] and end > slice['source_end']:
                # range starts inside slice, and ends after
                no_slice_apply = False
                inside_length = slice['source_end']+1 - start
                assert inside_length < length
                post_length = length - inside_length
                mapped_ranges.append([start + slice['action'], inside_length])
                ranges_to_treat.append([start + inside_length +1, post_length])
                break
            elif start < slice['source_start'] and slice['source_end'] < end:
                # range starts before, is inside slice, and ends after
                no_slice_apply = False
                pre_length = slice['source_start'] - start
                assert pre_length < length
                inside_length = slice['range_length']
                assert inside_length < length
                post_length = length - pre_length - inside_length
                ranges_to_treat.append([start, pre_length])
                mapped_ranges.append([slice['target_start'], inside_length])
                ranges_to_treat.append([start+pre_length+inside_length+1 , post_length])
                break
        if no_slice_apply:
            mapped_ranges.append(range)
    return mapped_ranges

def get_min_location(locations):
    return min(start for [start, _] in locations)

def main():
    with open('./2023/05input.txt') as f:
        input_blocks = f.read().split('\n\n')
    maps = get_maps(input_blocks)
    seeds = get_seeds(input_blocks)
    locations = do_mapping(seeds, maps)
    part1 = get_min_location(locations)
    print(f"{part1 = }")
    seeds = get_seeds(input_blocks, 'pair')
    locations = do_mapping(seeds, maps)
    part2 = get_min_location(locations)
    print(f"{part2 = }")

if __name__ == '__main__':
    sys.exit(main())
