import schedule
import time
import shutil
from datetime import datetime

def backup_files(source_dir, backup_dir):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_folder = f'{backup_dir}/backup_{timestamp}'

    try:
        shutil.copytree(source_dir, backup_folder)
        print(f'Backup created at {backup_folder}')
    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    source_dir = '/home/kunalkumarsahoo/Documents'
    backup_dir = './backup'
    schedule.every().day.at('09:43').do(backup_files, source_dir=source_dir, backup_dir=backup_dir)

    while True:
        schedule.run_pending()
        time.sleep(1)
