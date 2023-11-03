# Reading a Gradebook File
    # You have a CSV file named "grades.csv" that contains student names and their corresponding grades. 
    # Each line in the file consists of a student name followed by a comma and their grade. 
    # Implement a program to read the file in read mode ('r') and calculate the average grade for the students.

from csv import reader

def read_csv(file_path):
    '''
    Params: file_path (str)
    Returns: csv_content (list)
    Description: This function reads a CSV file
    and returns the contents of the CSV file in 
    the form of a list
    '''
    with open(file_path, 'r') as file:
        csv_content = reader(file, delimiter=',')
        return list(csv_content)

def list2dict(reader):
    '''
    Params: reader (list)
    Returns: dictionary (dict)
    Description: This function accepts a list of CSV contents
    and returns a dictionary for easier manipulation.
    '''
    dictionary = dict()
    for line in reader:
        dictionary[line[0]] = list(map(int, line[1:]))
    return dictionary

def mean(list):
    '''
    Params: list (list)
    Returns: mean (float)
    Description: This function returns the statistical
    mean of all the numbers of the list
    '''
    return sum(list) / len(list)

def display_average(dictionary):
    '''
    Params: dictionary (dict)
    Returns: None
    Description: This function displays the contents
    of the argument dictionary in a tabular manner
    '''
    print('Student\t\t\t Average grade')
    for key in dictionary:
        print(f'{key}\t\t\t {mean(dictionary[key])}')


if __name__ == '__main__':
    file_path = './31-07-2023/grades.csv'
    display_average(
        dictionary=list2dict(
            reader=read_csv(
                file_path=file_path
            )
        )
    )