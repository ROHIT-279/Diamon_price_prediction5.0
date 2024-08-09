import os
import sys
import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingection import DataIngection


if __name__=='__main__':
    obj = DataIngection()
    train_data_path,test_data_path= obj.initiate_data_ingection()
    print(train_data_path,test_data_path)