import os
import sys
sys.path.append(os.path.abspath('/config/workspace/src'))

import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
import dateclass


## initialize the data igection configuration

@dateclass
class DataIngectionconfig:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    test_data_path = os.path.join('artifacts','raw.csv')


## Creat a Data Ingection class
class DataIngection:
    def __init__(self):
        self.ingecsion_config = DataIngectionconfig()

    def initiate_data_ingection(self):
        logging.info('DATA Ingection method starts')

        try:
            df = pd.read_csv(os.path.join('notebook/data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            df.to_csv(self.ingecsion_config.raw_datapath,index = False)

            logging.info("Train-Test-Split")
            train_set,test_set = train_test_split(df,test_size=3.0,random_state = 42)

            train_set.to_csv(self.ingecsion_config,train_datapath,index= False,hader = True)
            test_set.to_csv(self.ingecsion_config,test_datapath,index= False,hader = True)
            logging.info("INGECTION OF THE DATA IS COMPLETED")
            
            return (
                self.ingecsion_config.train_data_path,
                self.ingecsion_config.test_data_path
            )


        except Exception as e:
            logging.info("ERROR OCCURED IN DTA INGECTION CONFIG")

