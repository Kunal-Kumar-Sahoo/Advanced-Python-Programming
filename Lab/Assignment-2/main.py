import os
import subprocess
import platform

def load_content(file_path):
    # Load and read the contents of the specified file
    with open(file_path, 'r') as file:
        contents = file.readlines()
        contents = [content.strip() for content in contents]
    return contents

def get_requirements(contents):
    # Parse the contents to extract requirements and their values
    requirements = {}
    for content in contents:
        if ':' in content:
            content = content.split(':')
            requirements[content[0]] = content[1]
        elif '==' in content:
            if 'Libs' not in requirements:
                requirements['Libs'] = [content]
            else:
                requirements['Libs'].append(content)
    return requirements

class OSNotFound(Exception):
    # Custom exception class for when the OS is not found
    def __init__(self):
        pass

    def __str__(self):
        return 'OS Not Found!'

class OSNotSupported(Exception):
    # Custom exception class for when the OS is not supported
    def __init__(self):
        pass

    def __str__(self):
        return 'OS Not Supported!'

class OSVersionNotSupported(Exception):
    # Custom exception class for when the OS version is not supported
    def __init__(self):
        pass

    def __str__(self):
        return 'OS Version Not Supported'
    
class PythonVersionNotFound(Exception):
    # Custom exception class for when the Python version is not found
    def __init__(self):
        pass

    def __str__(self):
        return 'Python Version Not Found'

class LibsNotFound(Exception):
    # Custom exception class for when the libraries are not found
    def __init__(self):
        pass

    def __str__(self):
        return 'Libraries Not Found!'
    
class LibsVersionNotFound(Exception):
    # Custom exception class for when the library versions are not found
    def __init__(self):
        pass

    def __str__(self):
        return 'Library versions Not Found!'
    
def validate_configuration(requirements):
    '''Actual way to check system configuration
    os_name = str(subprocess.check_output('lsb_release -i', shell=True))
    os_name = os_name.split(':')[-1][2:-3]
    os_version = str(subprocess.check_output('lsb_release -r', shell=True))
    os_version = os_version.split(':')[-1][2:-3]
    
    python_version = platform.python_version()
    '''

    os_name = 'Ubuntu'
    os_version = '18.02'
    
    try:
        # Validate the configuration based on provided requirements
        if 'OS' not in requirements:
            raise OSNotFound
        if os_name != requirements['OS']:
            raise OSNotSupported
            if os_version != requirements['OS_VERSION']:
                raise OSVersionNotSupported
        if 'Python' not in requirements:
            raise PythonVersionNotFound
        if 'Libs' not in requirements:
            raise LibsNotFound
        if 'Libs' in requirements:
            for lib in requirements['Libs']:
                if '==' not in lib:
                    raise LibsVersionNotFound
    
    except Exception as e:
        print(e)

def create_docker_file(requirements):
    # Create a Dockerfile based on the provided requirements
    with open('output.txt', 'w') as file:
        file.writelines([f'FROM {requirements["OS"]}:{requirements["OS_VERSION"].lower()}\n\n'])
        if 'Python' in requirements:
            file.writelines([f'RUN apt-install python{requirements["Python"]}\n\n'])
            for lib in requirements['Libs']:
                file.writelines([f'RUN python3 -m pip install {lib}\n'])
        file.writelines(['\nRUN echo "Compilation successful"'])

if __name__ == '__main__':
    # Define the path to the requirements file and process the requirements
    file_path = './req.txt'
    requirements = get_requirements(load_content(file_path))
    validate_configuration(requirements)
    create_docker_file(requirements)
