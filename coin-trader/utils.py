import os
import math
import logging

import pandas as pd
import numpy as np

import keras.backend as K


# Formats Position
format_position = lambda price: ('-$' if price < 0 else '+$') + '{0:.2f}'.format(abs(price))


# Formats Currency
format_currency = lambda price: '${0:.2f}'.format(abs(price))


def get_stock_data(stock_file):
    print('get_stock_data()')
    """Reads stock data from csv file
    """
    df = pd.read_csv(stock_file)
    # df['date'] = pd.to_datetime(df['date'], format="%Y-%m")
    
    return df
    
def get_economy_data(economy_file):
    print('get_economy_data')

    df = pd.read_csv(economy_file)

    df['Date'] = df['Date'].astype(str)
    df['Date'] = df['Date'].str.replace(". ", "-", regex=False)
    df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m")
    df = df.set_index('Date')
    return df

def get_date(stock_file):
    print('get_date()')

    df = pd.read_csv(stock_file)
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    return list(df['date'])

def switch_k_backend_device():
    if K.backend() == "tensorflow":
        logging.debug("switching to TensorFlow for CPU")
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"