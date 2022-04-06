import mysql.connector as myconn
import pandas as pd
import re
data = pd.read_csv('aq.csv')
print(data.head())   #.head() prints the first 5 rows, useful for checking data
date = input('date: ')
creationdatelist = data['datacreationdate'].tolist()
r = re.compile(f'.*{date}') # '.'Any character except newline , '*' 0 or more  
newlist = list(filter(r.match, creationdatelist))


data.set_index("datacreationdate", inplace=True)
count=0
geez =[]
for i in range(len(newlist)):
    if count ==5:
        break
    print(f'{data.loc[newlist[i]]}\n\n')
    count+=1
print(f'.......\n......\nlisted 5 rows on the date {date}')
