import mysql.connector as myconn
import pandas as pd

data = pd.read_csv('aq.csv')
print(data.head())   #.head() prints the first 5 rows, useful for checking data