import random
import os
import shutil
import stat
import time

def main():
    file_name = 'complex.txt'

    write_to_file(file_name)
    print('____')

    read_from_file(file_name)
    print('____')

    read_single_line(file_name)
    print('____')

    read_all_lines(file_name)
    print('____')

    write_list_to_file(file_name)
    print('____')

    move_file_pointer(file_name)
    print('____')

    flush_file_buffer(file_name)
    print('____')

    close_file_explicitly(file_name)
    print('____')

    new_file_name = 'renamed_file.txt'
    rename_file('to_rename.txt', new_file_name)
    print('____')

    # delete_file(new_file_name)

    change_file_permissions(file_name)
    print('____')

    get_file_metadata(file_name)
    print('____')


def write_to_file(file_name):
    with open(file_name, 'w') as f:
        data_to_write = 'This is a sample file.\nAdding second line.\n'
        f.write(data_to_write)

def read_from_file(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
        print('Reading the entire file:')
        print(content)

def read_single_line(file_name):
    with open(file_name, 'r') as file:
        line = file.readline()
        print('Reading a single line:')
        print(line)

def read_all_lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print('Reading all the lines:')
        print(lines)

def write_list_to_file(file_name):
    lines = ['This is another line.\n', 'Add one more line.\n']
    with open(file_name, 'a') as file:
        file.writelines(lines)

def move_file_pointer(file_name):
    with open(file_name, 'r') as file:
        print('Current position of pointer:', file.tell())
        file.seek(15)
        print('Moved the file pointer to position 15.')
        print('Current position of file:', file.tell())
        content = file.read()
        print('Reading the file after seeking 15 places:')
        print(content)

def flush_file_buffer(file_name):
    with open(file_name, 'r') as file:
        print('\nReading data before flush')
        print(file.read())
        file.flush()
        print('Reading the file after flush()')
        print(file.read())
        print('File buffer flushed')

def close_file_explicitly(file_name):
    file = open(file_name, 'r')
    print('File is open')
    file.close()
    print('File is closed explicitly')

def rename_file(file_name, new_file_name):
    try:
        os.rename(file_name, new_file_name)
        print('File', file_name, 'renamed to', new_file_name)
    except FileNotFoundError:
        print('File name', file_name, 'does not exist')
    except FileExistsError:
        print('A file', new_file_name, 'already exists')

def delete_file(file_name):
    pass

def change_file_permissions(file_name):
    file_permissions = os.stat(file_name).st_mode  # st_mode: represents file type and file mode bits
    print('File permissions (in octal):', oct(file_permissions))
    os.chmod(file_name, stat.S_IRWXG)
    print('New File permissions (in octal):', oct(file_permissions))

def get_file_metadata(file_name):
    file_stat = os.stat(file_name)
    print('File size:', file_stat.st_size, 'bytes')
    print('File name:', os.path.basename(file_name))
    print('File type:', 'Directory:' if os.path.isdir(file_name) else 'File')
    print('Creation time:', time.ctime(file_stat.st_ctime))
    print('Last access time:', time.ctime(file_stat.st_atime))
    print('Last modification time:', time.ctime(file_stat.st_mtime))
    print('Disk usage in bytes for ~/Playground:', shutil.disk_usage('/home/kunalkumarsahoo/Playground'))


if __name__ == '__main__':
    main()