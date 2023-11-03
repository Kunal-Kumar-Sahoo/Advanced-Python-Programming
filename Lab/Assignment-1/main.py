from os import listdir, path

def read_file(file_path, attributes, delimiter=':'):
    '''
    Params:
        - file_path (str): The path to the file to be read.
        - attributes (list): List of attribute names to be extracted from the file.

    Returns:
        - dictionary (dict): A dictionary containing the extracted attributes as keys and their corresponding values.

    Description:
        This function reads the specified file and extracts the values of the given attributes.
        It assumes that each line in the file contains an attribute and its value, separated by a delimiter (default is ':').
        The function returns a dictionary with the attribute names as keys and their corresponding values as values.
    '''
    with open(file_path, 'r') as file:
        text = file.readlines()
        dictionary = dict()
        for i in range(len(text)):
            text[i] = text[i].split(delimiter)
        
        for i in text:
            if i[0] in attributes and i[0] not in dictionary:
                dictionary[i[0]] = i[1].strip()
        
        return dictionary
    
def read_records(folder_path, attributes):
    '''
    Reads multiple files from a folder and extracts the specified attributes.

    Params:
        - folder_path (str): The path to the folder containing the files to be read.
        - attributes (list): List of attribute names to be extracted from each file.

    Returns:
        - records (list): A list of dictionaries, where each dictionary contains the extracted attributes from a file.

    Description:
        This function reads all the files in the specified folder and calls 'read_file' to extract the desired attributes.
        It returns a list of dictionaries, where each dictionary represents the attributes of a single file.
    '''
    files_list = listdir(folder_path)
    records = []
    for file in files_list:
        records.append(read_file(path.join(folder_path, file), attributes))
    return records

def create_product_db(records):
    '''
    Creates a database of products and their average ratings based on the records.

    Params:
        - records (list): A list of dictionaries representing records containing product information.

    Returns:
        - products (dict): A dictionary with product IDs as keys and their average ratings as values.

    Description:
        This function takes a list of records and calculates the average rating for each product based on their reviews.
        It returns a dictionary where the keys are the product IDs and the values are their corresponding average ratings.
    '''
    products = dict()
    for record in records:
        if check_validity(record):
            if record['Product ID'] in products:
                products[record['Product ID']].append(int(record['Review rating']))
            else:
                products[record['Product ID']] = [int(record['Review rating'])]
    
    for product in products:
        products[product] = sum(products[product]) / len(products[product])

    return products

def display_top(records, top=3):
    '''
    Displays the top-rated products and their average ratings.

    Params:
        - records (dict): A dictionary with product IDs as keys and their average ratings as values.
        - top (int, optional): The number of top-rated products to display. Default is 3.

    Returns:
        - disp (str): A formatted string representing the top-rated products and their average ratings.

    Description:
        This function takes the 'records' dictionary, sorts it based on average ratings in descending order, and displays
        the top-rated products along with their average ratings in a formatted string.
        The 'top' parameter determines how many top-rated products to display.
    '''
    records = dict(sorted(records.items(), key=lambda x: x[1], reverse=True))
    disp = 'Product ID\t Average Rating'
    i = 0
    for key in records:
        if i < top:
            disp += f'\n{key}\t {records[key]}'
            i += 1
        else:
            break
    return disp

def check_validity(record):
    '''
    Checks the validity of a record.

    Params:
        - record (dict): A dictionary representing a single record with different attributes.

    Returns:
        - validity (bool): True if the record is valid, False otherwise.

    Description:
        This function checks whether a record has valid attributes based on specific conditions.
        It verifies the 'Customer ID' and 'Product ID' have the correct length and consist only of alphanumeric characters.
        It also checks if the 'Review rating' is within the valid range of 1 to 5 and if the 'Review text' is not empty.
    '''
    if not (len(record['Customer ID']) == 6 and record['Customer ID'].isalnum()):
        return False
    if not (len(record['Product ID']) == 10 and record['Product ID'].isalnum()):
        return False
    if not (1 <= int(record['Review rating']) <= 5):
        return False
    if record['Review text'] == '':
        return False
    
    return True

def valid_records(records):
    '''
    Counts the number of valid and invalid records in a list.

    Params:
        - records (list): A list of dictionaries representing records with different attributes.

    Returns:
        - valid (int): The number of valid records.
        - invalid (int): The number of invalid records.

    Description:
        This function takes a list of records and checks the validity of each record using the 'check_validity' function.
        It returns the counts of valid and invalid records.
    '''
    valid, invalid = 0, 0
    for record in records:
        if check_validity(record):
            valid += 1
        else:
            invalid += 1
    return valid, invalid

def write_summary(file_path, records):
    '''
    Writes a summary file with valid and invalid review counts and top-rated products.

    Params:
        - file_path (str): The path to the file where the summary will be written.
        - records (list): A list of dictionaries representing records with different attributes.

    Returns:
        - None

    Description:
        This function takes a list of records and calls the 'valid_records' and 'display_top' functions to create
        a summary file. The summary file contains the counts of valid and invalid reviews and the top-rated products.
    '''
    with open(file_path, 'w') as file:
        valid, invalid = valid_records(records)
        file.writelines(f'Valid reviews: {valid}\nInvalid reviews: {invalid}')
        file.writelines(f'\n{display_top(create_product_db(records))}')
    print('File generated!')
        

if __name__ == '__main__':
    ATTRIBUTES = ['Customer ID', 'Product ID', 'Review date', 'Review rating', 'Review text']
    records = read_records('customers', ATTRIBUTES)
    db = create_product_db(records)
    write_summary('summary.txt', records)