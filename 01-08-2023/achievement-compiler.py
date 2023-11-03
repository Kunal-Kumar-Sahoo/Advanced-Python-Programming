# There exists four different files, each contains Individual Student's  name, id_no, branch and achievement. 
# Combine the data of these 4 students into the Achievement.txt file

from os import listdir, path, getcwd
from json import dump

def list_files(folder_path):
    files = listdir(folder_path)
    return [
        path.join(getcwd(), folder_path, i) 
        for i in files
    ]

def read_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.readlines()
        contents = [i.split(':') for i in contents]
        student = dict()
        for content in contents:
            try:
                student[content[0]] =  eval(content[1].strip())
            except Exception as e:
                student[content[0]] = content[1].strip()
    return student

def compile_records(folder_path):
    return list(map(read_file, list_files(folder_path)))

def write_records(file_name, compiled_list):
    content = {'students_list': compiled_list}
    with open(file_name, 'w') as file:
        file.seek(0)
        dump(content, file, indent=4)
    print('File written successfully')
    

if __name__ == '__main__':
    records = compile_records('achievements')
    write_records('achievements.json', records)
