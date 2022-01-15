import os
import logging

import pandas as pd

# 데이터 읽어오기
def get_data(file):
    df = pd.read_csv(file)
    
    return df