import schedule
import time

def task1():
    print('Task 1 executed')

def task2():
    print('Task 2 executed')

def task3():
    print('Task 3 executed')


if __name__ == '__main__':
    schedule.every(2).seconds.do(task1)
    schedule.every(5).seconds.do(task2)

    while True:
        schedule.run_pending()
        time.sleep(1)