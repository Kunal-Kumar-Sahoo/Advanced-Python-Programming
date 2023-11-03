# Display the frequency of top 'n' frequent characters present in the string

def find_frequency(string: str) -> dict:
    '''
    Params: string(str)
    Returns: dict(str, int)
    Description: This function inputs a string and returns a dictionary
    containing each unique character present in the string along with their
    frequency of occurrence
    '''
    frequencies = dict()
    for i in string:
        if i.isalpha():
            if i in frequencies:
                frequencies[i] += 1
            else:
                frequencies[i] = 1
    return frequencies

def display_top(dictionary: dict, top: int = 2) -> None:
    '''
    Params: dictionary(dict), top(int)
    Returns: None
    Description: This function inputs any dictionary, sorts them based on their
    values and displays top 'n' entries.
    '''
    dictionary = dict(sorted(dictionary.items(), key=lambda x:x[1], reverse=True))
    print('Character\t Frequency')
    i = 0
    for key in dictionary:
        if i < top:
            print(f'{key}\t\t {dictionary[key]}')
            i += 1
        else:
            break

if __name__ == '__main__':
    string = input('Enter a string: ')
    display_top(
        dictionary=find_frequency(string=string), 
    )