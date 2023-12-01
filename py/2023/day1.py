from pathlib import Path

file_path = Path('2023/day1-calibration-doc.txt').resolve()
NUMBERS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_integer_start(string: str) -> int:
    for idx, number in enumerate(NUMBERS):
        if string.startswith(number):
            return idx
    try:
        return int(string[0])
    except ValueError:
        return get_integer_start(string[1:])

def get_integer_end(string: str) -> int:
    for idx, number in enumerate(NUMBERS):
        if string.endswith(number):
            return idx
    try:
        return int(string[-1])
    except ValueError:
        return get_integer_end(string[:-1])

answer = 0
with open(file_path, 'r') as file:
    for line in file:
        first_digit = get_integer_start(line)
        second_digit = get_integer_end(line)
        answer += 10*first_digit+second_digit

print(answer)
