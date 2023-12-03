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

def readTxt(path='day1/input.txt') -> Iterable:
    with open(path, 'r') as f:
        for line in f:
            yield line.rstrip("\n")

def formCalibrationValue(line) -> int:
    for char in filter(str.isdigit, line):
        digit1 = int(char)
        break
    for char in filter(str.isdigit, line[::-1]):
        digit2 = int(char)
        break

    return digit1*10 + digit2

def computeSum(reader: Iterable) -> int:
    calibrationSum = 0 
    for line in reader:
        calVal = formCalibrationValue(line)
        calibrationSum += calVal
    return calibrationSum

def main():
    calibrationSum = computeSum(readTxt())
    print(calibrationSum)


if __name__ == "__main__": 
    main()