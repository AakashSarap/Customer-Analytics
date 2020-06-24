import numpy as np
import pandas as pd
import datetime as dt



# Removing the first row from a dataframe
def remove_n_Row(n, df):    
    """
    
    :param n: first n rows to be removed
    :param df: dataframe
    """
    df = df.iloc[n+1:]
    return df

# Create a function to assign the given column names to my df
def assign_col_names(df):
    """
    
    :param df: dataframe
    """
    cols = ['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country']
    df.columns = cols
    return df.columns
        
# changing the data 
def change_data_type(col,data_type):
    is_correct = None
    for i in col:
        if type(i) != data_type:
            is_correct = False
    if is_correct != False:
        print('True')
    elif is_correct == False:
        col = col.astype(data_type)        
        print('False')

# Create a function to make Revenue column
def Revenue(col_name1, col_name2):
    """


    :param col_name1: depicts the quantity
    :param col_name2: depicts the unit price of products
    :return: Revenue column as a product of quantity and unit price
    """
    return col_name1 * col_name2


# Create a function to change the data type to "int"
def to_int(x):
    """


    :param x: the column that needs to be operated
    :return: int format of column
    """
    try:
        x = int(x)
    except:
        x = np.nan
    return x

# create a function to fecth the month from respective dates
def to_month(date):
    """


    :param date: date to perform operation
    :return: returning the month
    """
    return dt.datetime(date.year, date.month, 1)

