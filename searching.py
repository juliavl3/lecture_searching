import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    sequential_data = {}
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        reader = json.load(json_file)
        for k,val in reader.items():
            if k in {"unordered_numbers","ordered_numbers","dna_sequence"}:
                if k == field:
                    sequential_data = val
                    return  sequential_data
            else:
                return None

def linear_search(sequential_data, number):
    """

    :param sequential_data:
    :param number:
    :return: dictionary with indices and occurrences of the number we are looking for
    """
    dict_data = {"positions":[] ,"count": 0}
    index = []
    for i,val in enumerate(sequential_data):
        if val == number:
            index.append(i)
        else:#keby mame break zhorsilo by to vypocetnu narocnost, teda teraz je narocnost O(n) linearne
            continue #alebo vnorene for cykly = zhorsuje = On exponencialna na druhu

    dict_data["count"] = len(index)
    dict_data["positions"] = index
    return dict_data

def pattern_search(seq_d, pattern):

    #je to dobre ale vypocetne je to narocnejsie jak by to mohlo byt lahsie
    pattern_indices = []
    for i in range(0, len(pattern)):
        kodon = ""
        for idx,nucleotide in enumerate(seq_d):
            kodon += nucleotide
            if kodon == pattern:
                pattern_indices.append(idx- 1)
                kodon = kodon[1:]

            if len(kodon) == len(pattern):
                kodon = kodon[1:]

            else:
                continue

    # indices = set()
    # for idx_left in range(len(seq_d) - len(pattern)+1):
    #     if seq_d[idx_left:idx_left + len(pattern)] == pattern:
    #         indices.add(idx_left + len(pattern) // 2)

    return set(pattern_indices)

def main():
    seq_data = read_data("sequential.json","dna_sequence")
    dict_data = linear_search(seq_data, 9)
    print(pattern_search(seq_data, "ATA"))



if __name__ == '__main__':
    main()