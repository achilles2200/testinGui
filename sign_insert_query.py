import mysql.connector

cnx = mysql.connector.connect(user='bankapp', passwd='Tsumpass',database='BankApp')

my_cursor = cnx.cursor()

##execute command to show databases
my_cursor.execute("SHOW DATABASES")

#fetchall method does what it name states
result = my_cursor.fetchall()
print(result)


my_cursor.execute("SHOW TABLES")
tables = my_cursor.fetchall()
print(tables)


#create a table name, age, gender, password
# def create_table (name='',age=0,gender='',password=''):
#     name = input("Print full name: ")
#     age = int(input("What is your age?: "))
#     gender = input("gender please: ")
#     password = input("Type password: ")
#
#     my_cursor.execute("CREATE TABLE user (id INT NOT NULL AUTO_INCREMENT,"
#                       "name VARCHAR(100) NOT NUll,"
#                       "age INT NOT NULL,password VARCHAR(100) PRIMARY KEY[id))")



#show tables
my_cursor.execute("DESC user")
print(desc_table = my_cursor.fetchall())



cnx.close()
#Project not finished upload to git for saftey