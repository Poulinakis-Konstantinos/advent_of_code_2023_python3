import re
from typing import Iterable

word2digit_mapper = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                     'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
WORDS = word2digit_mapper.keys()

PATTERN = '|'.join(WORDS) + '|[0-9]'
REVERSED_PATTERN = '|'.join([word[::-1] for word in WORDS]) + '|[0-9]'


def readTxt(path='day1/input.txt'):
    with open(path, 'r') as f:
        for line in f:
            yield line.rstrip("\n")

def find_first_digit(s: str, pattern: str, mapper: dict) -> int:
    match = re.search(pattern, s).group()
    if match.isdigit():
        return int(match)
    else:
        return mapper[match]


if __name__ == "__main__":
    doc = readTxt()
    callibration_values = []

    for line in doc:
        digit1 = find_first_digit(line, PATTERN, word2digit_mapper)
        digit2 = find_first_digit(
            line[::-1], REVERSED_PATTERN, {key[::-1]: val for (key, val) in word2digit_mapper.items()})
        callibration_values.append(digit1*10 + digit2)

    print(sum(callibration_values))
