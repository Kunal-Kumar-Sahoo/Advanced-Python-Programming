# Create a text file named "quiz.txt" that contains multiple-choice questions and their options. 
# Each question and its options are separated by newlines. 
# Implement a program to read the file in read mode ('r') and display the questions along with their options to the students

def display_quiz(file_path):
    with open(file_path, 'r') as file:
        contents = file.readlines()
        for line in contents:
            print(line, end='')
    print()


if __name__ == '__main__':
    display_quiz('./31-07-2023/quiz.txt')