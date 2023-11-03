import subprocess
import os
import datetime
import logging
import schedule


class DataBackup:
    def __init__(self, src:str, dest:str) -> None:
        self.__src = src
        self.__dest = dest

    def backup(self) -> None:
        assert os.path.exists(self.__src), 'Source directory not found'
        if not os.path.exists(self.__dest):
            os.mkdir(self.__dest)

        __timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        __backup_folder = f'{self.__dest}/backup_{__timestamp}'
        os.mkdir(__backup_folder)

        for file in os.listdir(self.__src):
            file_path = os.path.join(self.__src, file)
            subprocess.call(['cp', file_path, __backup_folder])

        Logger.log_changes(f'Created backup of {self.__src} at {__backup_folder}')


class Cleaner:
    def __init__(self, src:str, days:int=7) -> None:
        self.__src = src
        self.__days = days

    def clean_up(self) -> None:
        assert os.path.exists(self.__src), 'Source directory not found'
        __current_date = datetime.datetime.now().date()
        __files = []
        for file in os.listdir(self.__src):
            file_path = os.path.join(self.__src, file)
            file_date = datetime.datetime.fromtimestamp(
                os.path.getmtime(file_path)
            )
            if (__current_date - file_date).days >= self.__days:
                __files.append(file_path)
                os.remove(file_path)
        
        Logger.log_changes(f'Removed files {__files} from {self.__src}')


class Logger:
    @staticmethod
    def log_changes(message:str):
        logging.basicConfig(level=logging.DEBUG)
        __logger = logging.getLogger('backup_cleanup')
        __file_handler = logging.FileHandler('./logs.log')
        __formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        __file_handler.setFormatter(__formatter)
        __logger.addHandler(__file_handler)
        __logger.info(message)


class Scheduler:
    @staticmethod
    def schedule_processes(src:str, dest:str, days:int=7) -> None:
        schedule.every().day().at('14:00').do(DataBackup(src, dest).backup)
        schedule.every().day().at('14:00').do(Cleaner(src, days).clean_up)


if __name__ == '__main__':
    src = '/home/kunalkumarsahoo/Playground/Python/Advanced Python/28-08'
    dest = '/home/kunalkumarsahoo/Playground/Python/Advanced Python/29-08-2023/backup'
    
    Scheduler.schedule_processes(src, dest)