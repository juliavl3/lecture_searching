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
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as file:
        data = json.load(file)
    return data[field]

def linear_search(sequential_data, searching_number):
    list = []
    for index, number in enumerate(sequential_data):
        if number == searching_number:
            list.append(index)
    count = len(list)
    return {'positions':list,'count': len(list)}





def main():
    sequential_data = read_data('sequential.json', 'unordered_numbers')
    print(sequential_data)
    print(linear_search(sequential_data,searching_number=5))



if __name__ == '__main__':
    main()