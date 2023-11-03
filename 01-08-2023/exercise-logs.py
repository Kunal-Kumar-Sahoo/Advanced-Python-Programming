# Design a program that allows users to log their exercise activities and view their exercise logs. 
# The program should provide a user-friendly interface to input exercise details such as date, exercise type, duration, and calories burned. 
# The exercise logs should be stored in a file for future reference.

import csv

def input_log():
    date = input('Enter date in (dd/mm/yyyy): ')
    exercise = input('Enter exercise name: ')
    duration = float(input('Enter duration of exercise (in minutes): '))
    calories_burned = float(input('Enter calories burned: '))

    return [date, exercise, duration, calories_burned]

def log_exercise(activity):
    with open('logs.csv', 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(activity)
        print('Exercise logged successfully')

def fetch_logs():
    with open('logs.csv', 'r') as file:
        logs = csv.reader(file, delimiter=',')
        return list(logs)
    
def display_logs(logs):
    print('Date\t\t Exercise\t\t Duration\t\t Calories Burned')
    for log in logs:
        print(f'{log[0]}\t {log[1]}\t\t {log[2]}\t\t\t {log[3]}')
    
if __name__ == '__main__':
    flag = True
    while flag:
        print('Choices:\n1. Record an exercise\n2. Print logs\n3. Exit')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            log_exercise(
                activity=input_log()
            )
        
        elif choice == 2:
            display_logs(
                logs=fetch_logs()
            )
        elif choice == 3:
            flag = False
        else:
            print('Invalid choice!')
