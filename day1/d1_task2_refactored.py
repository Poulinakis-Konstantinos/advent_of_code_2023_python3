'''
Given a document with multiple lines, each containing at least 1 digit, find the first and last digits of each line.
Given these two digits form a number. Finally sum up all the numbers formulated from each line.

Attention: The digits might come in holographic form i.e. 1='one', 2='two'

eg. 
two1nine
eightwothree
abcone2threexyz

answer = 29, 83, 13, and sum=77.

Approach (the straightforward one): Parse the string in substrings of five chars (max number of chars present in mapper.)
Scan the substrings for digit_words or digits. Once you find one stop. Do the same for the reversed string with
reversed values in the mapper.
'''
import re

WORDS = ("zero", "one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine")
WORD_2_DIGIT_MAP = {word: digit for (word, digit) in zip(WORDS, range(10))}
REVERSED_WORD_2_DIGIT_MAP = {
    word[::-1]: digit for (word, digit) in zip(WORDS, range(10))}

PATTERN = '|'.join(WORDS) + '|[0-9]'
REVERSED_PATTERN = '|'.join([word[::-1] for word in WORDS]) + '|[0-9]'


def readTxt(path='day1/input.txt'):
    with open(path, 'r') as f:
        for line in f:
            yield line.rstrip("\n")


def find_first_digit(s: str, pattern: str, mapper: dict) -> str:
    match = re.search(pattern, s).group()
    return int(match) if match.isdigit() else mapper[match]


def form_calibration_value(s: str) -> int:
    d1 = int(find_first_digit(s, PATTERN, WORD_2_DIGIT_MAP))
    d2 = int(find_first_digit(s[::-1], REVERSED_PATTERN, REVERSED_WORD_2_DIGIT_MAP))
    return 10 * d1 + d2


def main():
    doc = readTxt()
    print(sum(map(form_calibration_value, doc)))


if __name__ == "__main__":
    main()