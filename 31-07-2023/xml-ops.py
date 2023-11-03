# Create an XML file named "employees.xml" with information about two employees. 
# Use the ElementTree module to build an XML tree, define elements, set attributes, and write the XML content to a file.

import xml.etree.ElementTree as ET

def get_employee_details(num_employees):
    '''
    Params: num_employees (int)
    Returns: employee_details (list)
    Description: This function takes the details of
    `num_employees` employees from the user and return
    it in the form of a list
    '''
    employee_details = []
    for i in range(1, num_employees + 1):
        print(f'\nEnter details for Employee {i}:')
        name = input('Name: ')
        age = input('Age: ')
        employee_details.append((name, age))
    return employee_details

def generate_xml_content(employee_details):
    '''
    Params: employee_details (list)
    Returns: tree (ET.ElementTree)
    Description: This function creates the XML tree
    for the list of employees present in the `employee_details`
    list
    '''
    employees = ET.Element('Employees')
    for i, (name, age) in enumerate(employee_details, start=1):
        employee = ET.SubElement(employees, 'Employee', id=str(i))
        name_element = ET.SubElement(employee, 'Name')
        name_element.text = name
        age_element = ET.SubElement(employee, 'Age')
        age_element.text = age
    tree = ET.ElementTree(employees)
    return tree

def write_xml(file_name, tree):
    '''
    Params: file_name (str), tree (ET.ElementTree)
    Returns: None
    Description: This function generates the XML file 
    based on the contents stored in the `tree`
    '''
    with open(file_name, 'wb') as file:
        tree.write(file)

if __name__ == '__main__':
    num_employees = int(input('Enter the number of employees: '))
    write_xml(
        file_name='employees.xml',
        tree=generate_xml_content(
            employee_details=get_employee_details(
                num_employees=num_employees
            )
        )
    )
