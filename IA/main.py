import numpy as np
import pandas as pd
import logging
import subprocess
import schedule
import time
from datetime import datetime


logging.basicConfig(
    filename='log.txt', 
    level=logging.DEBUG,
)

def main(file_name='students_scores_test.csv'):
    logging.info(f'{datetime.now()}: Running the process')

    ls = str(subprocess.run(['ls'], capture_output=True).stdout)

    if file_name in ls:
        try:
            logging.info(f'{datetime.now()}: CSV file found')
            df = pd.read_csv(file_name)
            logging.info(f'{datetime.now()}: Dataset read successfully')
            df_trimmed = df.iloc[2:8, :]
            df_trimmed.to_csv('updated_data.csv')
            logging.info(f'{datetime.now()}: Saving the updated dataset to \'updated_data.csv\'')

            scores = df['Score'].to_numpy()

            highest_score = np.max(scores)
            lowest_score = np.min(scores)

            print(f'Highest score: {highest_score}\nLowest score: {lowest_score}')
            logging.info(f'{datetime.now()}: Highest score: {highest_score}')
            logging.info(f'{datetime.now()}: Lowest score: {lowest_score}')

            df_filtered = df.loc[df['Group'] == 'A']
            df_filtered = df_filtered[df['Score'] > 70]
            print(df_filtered)
        
        except Exception as e:
            logging.error(f'{datetime.now()}: {e}')
        
        finally:
            del df, df_trimmed, scores, df_filtered
            logging.info(f'{datetime.now()}: Terminating the program')

    else:
        logging.error(f'{datetime.now()}: CSV file not found')


if __name__ == '__main__':
    print('Starting program\n\n')
    
    schedule.every(30).days.at('00:00').do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
    # main()