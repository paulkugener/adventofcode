import sys

LETTER_DIGITS = {
    'one': '1', 
    'two': '2', 
    'three': '3', 
    'four': '4', 
    'five': '5', 
    'six': '6', 
    'seven': '7', 
    'eight': '8', 
    'nine': '9'
    }


def get_first_digit(line, direction, include_letter_digits = False) -> int:
    start = 0
    end = len(line)
    step = 1
    if direction == 'reverse':
        start = len(line)-1
        end = -1
        step = -1
    letter_digits_index = {}
    if include_letter_digits == True:
        for k,v in LETTER_DIGITS.items():
            if direction == 'reverse':
                idx = line.rfind(k)
            else:
                idx = line.find(k)
            if idx > -1:
                letter_digits_index[k] = idx
    # print(letter_digits_index)
    for i in range(start, end, step):
        if line[i].isdigit():
            if include_letter_digits == True and len(letter_digits_index) > 0:
                if direction == 'reverse':
                    best_letter_digit_key = max(letter_digits_index, key=letter_digits_index.get)
                    if letter_digits_index[best_letter_digit_key] > i:
                        return LETTER_DIGITS[best_letter_digit_key]
                else:
                    best_letter_digit_key = min(letter_digits_index, key=letter_digits_index.get)
                    if letter_digits_index[best_letter_digit_key] < i:
                        return LETTER_DIGITS[best_letter_digit_key]
            return str(line[i])

def get_calibration_values_digits(lines, include_letter_digits = False):
    values = []
    for line in lines:
        # print(f"{line = }")
        x = str(get_first_digit(line, 'regular', include_letter_digits)) + str(get_first_digit(line, 'reverse', include_letter_digits))
        # print(f"{x = }")
        values.append(int(x))
    return values

def main():
    with open('./2023/01input.txt') as f:
        lines = f.read().splitlines()
    part1 = sum(get_calibration_values_digits(lines))
    part2 = sum(get_calibration_values_digits(lines, True))
    print(f"{part1 = }")
    print(f"{part2 = }")

if __name__ == '__main__':
    sys.exit(main())
