import pandas as pd
from sqlalchemy import create_engine

# MySQL Connection Details

username = 'root'
password = 'Qristin101'
hostname = '127.0.0.1' 
port = '3306'  
database_name = 'paintings'

# MySQL Connection URL
connection_url = f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database_name}'

db = create_engine(connection_url)

conn = db.connect()

# Testing connection
try:
    with db.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")


files = ['artist', 'canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']

for file in files:
    df = pd.read_csv('C:/Users/user/myProjects/famousPainitingsSqlAnalysis/paintingdatacsv/{}.csv'.format(file))

    df.to_sql(file, con=conn, if_exists='replace', index=False)



