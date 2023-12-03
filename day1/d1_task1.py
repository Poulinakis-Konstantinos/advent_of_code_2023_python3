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
all_digits = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
calibrationSum = 0

def readTxt(path='day1/input.txt'):
    with open(path, 'r') as f:
        for line in f:
            yield line.rstrip("\n")

def formCalibrationValue(line):
    digits = []

    for char in line:
        if char in all_digits:
            digits.append(char)
    assert len(digits) != 0 , "Fatal Error: Line does not contain calibration value"
    return int(digits[0] + digits[-1]) # concatenation of chars

def fastFormCalibrationValue(line):
    for char in line:
        if char in all_digits:
            digit1 = char
            break
    for char in reversed(line) : 
        if char in all_digits:
            digit2 = char
            break
    return int(digit1 + digit2) # concatenation of chars

for line in readTxt():
    cal_value = formCalibrationValue(line)
    calibrationSum += cal_value
print(calibrationSum)
calibrationSum=0

for line in readTxt():
    cal_value = fastFormCalibrationValue(line)
    calibrationSum += cal_value
print(calibrationSum)



# if __name__ == "__main__": 


# if __name__ == "__test__" : 
     