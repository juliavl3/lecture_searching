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
    dict_data = {}
    index = []
    for i,val in enumerate(sequential_data):
        if val == number:
            index.append(i)
            dict_data["positions"] = index
        else:
            continue

        dict_data["count"] = len(index)

    return dict_data

def main():
    seq_data = read_data("sequential.json","unordered_numbers")
    print(linear_search(seq_data, 9))

if __name__ == '__main__':
    main()