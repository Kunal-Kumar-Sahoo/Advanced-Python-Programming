# Program to calculate sum of all values in a column of a CSV file. Display suitable error messages if
# the column name doesn't exist or the column doesn't have numeric values.

import csv

def get_content(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        content = [row for row in reader]
    return content

def get_data(content):
    dictionary = {}
    for column_name in content[0]:
        dictionary[column_name] = []
    
    for record in content[1:]:
        for idx, key in enumerate(dictionary):
            try:
                dictionary[key].append(eval(record[idx]))
            except Exception as e:
                dictionary[key].append(record[idx])
    
    return dictionary

def calculate_sum(dictionary, column):
    try:
        if column not in dictionary.keys():
            print('Column not found')
        return sum(dictionary[column])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    data = get_data(get_content('data.csv'))
    print(data)
    col = input('Enter column: ')
    print(calculate_sum(data, col))