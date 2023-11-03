import schedule
import time
import os
from datetime import datetime

def commit_files(source_dir):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    try:
        os.system('git add .')
        os.system(f'git commit -m {timestamp}')
        print(f'Version saved')
    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    source_dir = '/home/kunalkumarsahoo/Documents'
    schedule.every(2).hours().do(commit_files, source_dir=source_dir)

    while True:
        schedule.run_pending()
        time.sleep(1)
