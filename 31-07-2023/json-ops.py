# Read and write JSON data to/from a file. The code defines two functions, read_json(filename) and write_json(filename, data), 
# that handle reading and writing JSON data from/to a file, respectively. It provides an example usage where it creates a 
# sample JSON object, writes it to a file, reads it back from the file, modifies the JSON data, and then writes the updated 
# data back to the file.

import json

def read_json(file_path):
    '''
    Params: file_path (str)
    Returns: None
    Description: This function reads and displays the contents
    of a JSON file
    '''
    with open(file_path, 'r') as file:
        contents = json.load(file)
        print('Name\t\t\t E-mail\t\t\t\t\t Interest')
        for content in contents['student_details']:
            print(f'{content["name"]}\t\t {content["email"]}\t\t {content["interest"]}')

def write_json(file_path, record):
    '''
    Params: file_path (str), record (dict)
    Returns: None
    Description: This function appends the `record` to the
    existing contents of the `file_path` and again write the 
    contents to the same file
    '''
    with open(file_path, 'r+') as file:
        contents = json.load(file)
        contents['student_details'].append(record)
        file.seek(0)
        json.dump(contents, file, indent=4)

def input_record():
    '''
    Params: None
    Returns: dict object
    Description: This function takes input from the user and 
    return the data in form of a dictionary object
    '''
    name = input('Enter your name: ')
    email = input('Enter your e-mail ID: ')
    interest = input('Enter your area of interest: ')

    return {
        'name': name, 'email': email, 'interest': interest
    }


if __name__ == '__main__':
    file_path = 'students.json'
    while True:
        print('Choices:\n1. Read records\n2. Add record')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            read_json(file_path)
        
        elif choice == 2:
            write_json(file_path, input_record())

        else:
            print('Invalid choice! Exiting')
            break
