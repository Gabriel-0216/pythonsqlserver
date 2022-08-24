import pandas as pd
import pyodbc

server = 'localhost,1433'
database = 'python'
username = 'sa'
password = '1q2w3e4r@#$'

connectionString = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = connectionString.cursor()
query = "SELECT * FROM SALES_DATA"

data = pd.read_sql(query, connectionString)


print(data.loc[(data['Month'] == 'January')]['Product'].head(100))
