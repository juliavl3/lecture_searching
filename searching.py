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
            if k == field:
                sequential_data = val

    return  sequential_data

def linear_search():
    pass

def main():
    print(read_data("sequential.json","unordered_numbers"))

if __name__ == '__main__':
    main()