# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 19:19:02 2020

@author: aakas
"""

# Purpose of this file is to transfer data between AWS Postgres, Python and s3

# Importing Reuqired Modules
import psycopg2
import pandas as pd
import io
from io import StringIO
import boto3

# Connect to the PostgreSQL database
conn = psycopg2.connect(host="database-2.cqklbhslpxrg.us-east-2.rds.amazonaws.com",
                        database="", user="postgres", password="uEaI6UMFSyAvMPRwFDac")
# Create a new cursor
cur = conn.cursor()

# A function that takes in a PostgreSQL query and outputs a pandas database 
def create_pandas_table(sql_query, database = conn):
    table = pd.read_sql_query(sql_query, database)
    return table
  
# Utilize the create_pandas_table function to create a Pandas data frame
# Store the data as a variable
df = create_pandas_table("SELECT * FROM Retail")
df

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
conn.close()


# Creating a function to pass the data to Jupyter Notebook for further analysis
def get_data():
    """
    
    return: dataframe pulled from Postgres Database
    """
    return df


# Creating a function to push clean data to Amazon s3

# defining AWS s3 details
s3_bucket = 'sarap-a'
region = 'us-east-2'
access_key_id = 'AKIAUEO24LPUZLCJE5HB'
secret_access_key = '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'
file_key = 'data_transformed.csv'    


def push_to_s3(s3_bucket, data):
    bucket = s3_bucket# already created on S3
    csv_buffer = StringIO()
    data.to_csv(csv_buffer)
    s3_resource = boto3.resource('s3')
    push = s3_resource.Object(bucket, 'data_transformed.csv').put(Body=csv_buffer.getvalue())
    return push

# Creating a function to import cleaned data from Amazon s3
date_cols = ['InvoiceDate']
def pull_from_s3():    
    s3c = boto3.client(
            's3',
            region_name = region,
            aws_access_key_id = access_key_id,
            aws_secret_access_key = secret_access_key
        )
    Obj = s3c.get_object(Bucket= s3_bucket, Key = file_key)
    df_clean = pd.read_csv(io.BytesIO(Obj['Body'].read()), parse_dates=date_cols)
    df_clean = df_clean.iloc[:,1:]
    return df_clean
