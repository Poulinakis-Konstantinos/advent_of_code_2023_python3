import re
from collections.abc import Generator
from typing import Tuple


def readTxt(path="day2/input.txt") -> Generator:
    with open(path, 'r') as f:
        for line in f:
            yield line.rstrip("\n")


def extract_game_id(s: str) -> str:
    return re.search(r"\d{1,10}", s).group()
    # keyword1 = re.search("Game *", line)
    # keyword2 = re.search(":", line)
    # game_id = line[keyword1.end():keyword2.start()]


def extract_color_occurence_per_round(game_round_info: str):
    per_round_color_info = game_round_info.split(',')
    red_occurences, green_occurences, blue_occurences = 0, 0, 0
    for single_color_info in per_round_color_info:
        # re.search returns None in case no match is found in the string
        red_match = re.search(r" red", single_color_info)
        if red_match:
            red_occurences = int(single_color_info[:red_match.start()].strip())
        green_match = re.search(r" green", single_color_info)
        if green_match:
            green_occurences = int(single_color_info[:green_match.start()].strip())
        blue_match = re.search(r" blue", single_color_info)
        if blue_match:
            blue_occurences = int(single_color_info[:blue_match.start()].strip())
    return (red_occurences, green_occurences, blue_occurences)


def form_color_frequency_tuple_per_game(color_info):
    color_freq_per_game = []
    for round in color_info.split(';'):
        color_freq_per_game.append(extract_color_occurence_per_round(round))
    return tuple(color_freq_per_game)


def process_data_line(line: str) -> Tuple:
    id_info, color_info = line.split(':')
    game_id = extract_game_id(id_info)
    return game_id, form_color_frequency_tuple_per_game(color_info)
    

def ingest_dataset(path="day2/input.txt") -> dict:
    ''' A dictionary with key=GameID and values tuple(tuple) containing the occurences of each color
    in each round is returned. E.g. game_stats={1:(12, 3, 4), 2: (5, 0, 2)}'''
    doc = readTxt(path)
    game_stats = {}
    for line in doc:
        game_id, color_freq = process_data_line(line)
        game_stats[game_id] = color_freq
    return game_stats


def is_game_valid(color_freqs: tuple, red_limit: int, green_limit: int, blue_limit: int) -> bool:
    limits = (red_limit, green_limit, blue_limit)
    for round_freqs in color_freqs:
        if any(lim < f for lim, f in zip(limits, round_freqs)):
            return False
    return True


def main():
    game_stats = ingest_dataset()
    id_sum = 0
    for id, color_freqs in game_stats.items():
        if is_game_valid(color_freqs, 12, 13, 14):
            id_sum += int(id)
    print(id_sum)


if __name__ == "__main__":
    main()