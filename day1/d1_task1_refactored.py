'''
Given a document with multiple lines, each containing at least 1 digit, find the first and last digits of each line.
Given these two digits form a number. Finally sum up all the numbers formulated from each line.

eg. 
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

answer = 12, 38, 15, and sum=77.
'''
from typing import Iterable
from collections.abc import Generator


def readTxt(path='day1/input.txt') -> Generator[str, None, None]:
    with open(path, 'r') as f:
        for line in f:
            yield line.rstrip("\n")


def findFirstDigit(s: str) -> str:
    return next(filter(str.isdigit, s))


def formCalibrationValue(line) -> int:
    digit1 = int(findFirstDigit(line))
    digit2 = int(findFirstDigit(reversed(line)))

    return 10*digit1 + digit2


def computeSum(reader: Iterable) -> int:
    return sum(map(formCalibrationValue, reader))


def main():
    calibrationSum = computeSum(readTxt())
    print(calibrationSum)


if __name__ == "__main__":
    main()
