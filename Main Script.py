#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pyodbc
import logging


# In[2]:


# Set up logging
logging.basicConfig(filename='error.log', level=logging.ERROR)


# In[3]:


# File path to the CSV file
csv_file_path = r"C:\Users\Manna\OneDrive\Documents\ec_utbildning\ptyhon\csv_viewer (1)\csv_viewer_without_data_and_filter 1\test_data.csv"


# In[4]:


# Function to read and process data
def process_data():
    try:
        # Read CSV file
        data = pd.read_csv(csv_file_path)
        print("Data loaded successfully")

        # Process data (example: convert 'date' column to datetime)
        data['date'] = pd.to_datetime(data['date'], errors='coerce')  # Handle parsing errors
        print("Data processing complete")
        
        return data
    except Exception as e:
        logging.error(f"Error reading or processing data: {str(e)}")
        raise


# In[5]:


# Function to update SQL table
def update_sql_table(data):
    try:
        # Establish connection to SQL database
        conn = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=server_name;DATABASE=db_name;UID=user;PWD=password'
        )
        cursor = conn.cursor()

        # Iterate over the data rows and update the SQL table
        for index, row in data.iterrows():
            cursor.execute(
                """
                UPDATE table_name 
                SET column_name = ? 
                WHERE condition_column = ?
                """, 
                row['column_name'], row['condition_column']
            )
        conn.commit()
        cursor.close()
        conn.close()
        print("SQL table updated successfully")
    except Exception as e:
        logging.error(f"Error updating SQL table: {str(e)}")
        raise


# In[7]:


# Main execution
if __name__ == '__main__':
    try:
        # Process the data
        data = process_data()

        # Update SQL table with the processed data
        update_sql_table(data)
    except Exception as e:
        logging.error(f"Failed to complete task: {str(e)}")
        print(f"An error occurred. Check 'error.log' for more details.")


# In[ ]:




