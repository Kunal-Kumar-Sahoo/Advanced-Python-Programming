def r_plus1():
    with open('file.txt', 'r+') as f:
        f.write("new line \n") 

def r_plus2():
    with open('file.txt', 'r+') as f:
        f.read()                # move file position to the end of the file.
        f.write("new line \n")

def w_plus1():
    with open('file.txt', 'w+') as f:   # create a new file or truncates it
        f.write("test 1\n")
        f.write("test 2\n")
        f.write("test 3\n")             

def w_plus2():
    with open('file.txt', 'w+') as f:   # create a new file or truncates it
        f.write("test \n")
        f.write("test \n")
        f.write("test \n")             # now the file pointer is at the end
        f.seek(0)                       # move the file pointer to the beginning
        lines = f.read()                # read it, now we can read!
        print(lines) 




if __name__ == '__main__':
    w_plus2()
