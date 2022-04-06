import mysql.connector as myconn   
dbConn = myconn.connect(
                host = 'localhost',
                user = 'aquser',
                password = '!a000000',
                database = 'aqD1047316'
                    
        )
sql = '''CREATE TABLE `users` (id INTEGER AUTO_INCREMENT PRIMARY KEY,
                                    account VARCHAR(255) NOT NULL,
                                    name VARCHAR(255) NOT NULL,
                                    email VARCHAR(255) NOT NULL,
                                    password VARCHAR(255) NOT NULL
                                    )'''

my_cursor = dbConn.cursor()                                    
my_cursor.execute(sql)
my_cursor.execute('SHOW TABLES')

for table in my_cursor:
    print(table[0])
    print('fk you')
