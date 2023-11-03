'''
Write a program to print the following pattern:
                3 3 3
                 2 2
                  1
'''

# Method 1
def pattern(rows):
    '''
    Params: rows(int)
    Returns: None
    Description: Prints the required pattern by implementing
    nested for loops
    '''
    for i in range(rows):  # outer for loop is used to access the ith row
        for _ in range(i):  # the first inner for loop determines the gap to maintained in the beginning of the pattern
            print(' ', end='')
        for _ in range(rows-i):  # The second for loop determines the numbers to be printed
            print(rows-i, end=' ')
        print()

# Method 2
def pattern2(rows):
    '''
    Params: rows(int)
    Returns: None
    Description: Prints the required pattern by using
    the concept of string multiplication in Python3
    '''
    for i in range(rows+1):
        print(' ' * i, end='')
        print(f'{rows-i} ' * (rows-i), end='')
        print()


# Ensures the below code is not executed when this program is used as a library
if __name__ == '__main__':
    rows = int(input('Enter number of rows: '))
    print('Pattern using Nested for loop')
    pattern(rows)
    print('Same pattern using String multiplication')
    pattern2(rows)