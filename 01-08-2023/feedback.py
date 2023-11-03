# Develop a feedback collection program that allows users to submit their feedback.
# The program should prompt the user to enter their name (optional) and their feedback.
# The collected feedback should be stored in a file named "feedback.txt".
# The program should provide a menu with two options: "1. Submit feedback" and "2. Exit".
# If the user chooses option 1, the program should collect the feedback.
# If the user chooses option 2, the program should exit. Any other choice should result in an error message.

def input_feedback():
    name = input('Enter name (optional): ')
    feedback = input('Enter your feedback:\n')

    return [name, feedback]

def record_feedback(record):
    with open('feedback.txt', 'a') as file:
        if record[0] == '':
            record[0] = 'Anonymous'
        file.writelines(f'{record[0]}:{record[1]}\n')
        print('Record written')

def retrieve_feedbacks():
    with open('feedback.txt', 'r') as file:
        records = file.readlines()
        return records

def display_feedback(records):
    for record in records:
        record = record.split(':')
        print(f'{record[0]} says:')
        print(f'{record[1]}')

if __name__ == '__main__':
    while True:
        print('Choices:\n1. Submit feedback\n2. Read feedbacks\n')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            record_feedback(input_feedback())
        
        elif choice == 2:
            display_feedback(retrieve_feedbacks())

        else:
            print('Invalid choice')
            break