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

word2digit_mapper = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5,       
                     'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0} 
WORDS = word2digit_mapper.keys()

PATTERN = '|'.join(WORDS) + '|[0-9]'
REVERSED_PATTERN = '|'.join([word[::-1] for word in WORDS]) + '|[0-9]'


def readTxt(path='day1/input.txt'):
    with open(path, 'r') as f:
        for line in f:
            yield line.rstrip("\n")

# def find_first_digit(s: str, mapped_words=word2digit_mapper) -> int:
#     for i in range(0, len(s)-5, 1):
#         if s[i].isdigit():
#             return int(s[i])
        
#         substring = s[i : i+5]
#         for key in mapped_words.keys():
#             if key in substring:
#                 return mapped_words[key]
#     # check the last 5 characters in the string for digits       
#     for i in range(len(s)-5, len(s)):
#         print(i)
#         if s[i].isdigit():
#             return int(s[i])


def find_first_digit(s:str, pattern:str, mapper:dict) -> int :
    match = re.search(pattern, s).group()
    if match.isdigit():
        return int(match)
    else:
        return mapper[match]
    

if __name__ == "__main__" :
    doc = readTxt()
    callibration_values = []

    for line in doc:
        digit1 = find_first_digit(line, PATTERN, word2digit_mapper)
        digit2 = find_first_digit(line[::-1], REVERSED_PATTERN, {key[::-1]:val for (key, val) in word2digit_mapper.items()})
        callibration_values.append(digit1*10 + digit2)
    
    print(sum(callibration_values))