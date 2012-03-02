# coding=utf-8
#Shuo, exercise 2012-02-15

from Settings import Settings # from file import class
import sqlite3
from DB import DB

def helloShuo():
    return 'Hello Shuo'            
    
def get_groups():
    #make table if not exists
    #query create table ...
    #select * from groups
    #execute sql query and return fetchall
    try:DB().create_table()
    except: pass
    #DB().insert_user(1, 'shuo', '123', 'sdiao@brandeis.edu')
    #DB().query("""INSERT INTO users VALUES (1, 'shuo', '123','sdiao@brandeis.edu')""")
    #DB().query("""INSERT INTO users VALUES (NULL, 'bjorn', '123','bjorn@brandeis.edu')""")
    return DB().query('SELECT * FROM users')

#SHUO
def add_user(user, pwd, email):
    myquery = """INSERT INTO users VALUES (NULL, '"""+user+"""','"""+pwd+"""','"""+email+"""')"""
    DB().query(myquery)
    return DB().query('SELECT COUNT(*) AS total_user FROM users')
    #return DB().row_count('SELECT * FROM users')# in sqlite3, the row is set to -1 for SELECT clause. 
    #MODIFY the return value later
    
    
#SHUO
def get_users():
    return DB().query('SELECT * FROM users')

#SHUO. check whether a user and its password exist in the database
def check_login(user, pwd):
    myquery = """SELECT COUNT(*) AS found FROM users WHERE user='"""+user+"""' AND password='"""+pwd+"""'"""
    return DB().query(myquery)
#SHUO. check whether a user exists
def check_user(user):
    myquery = """SELECT COUNT(*) AS find_user FROM users WHERE user='"""+user+"""'"""
    return DB().query(myquery)

#Shuo. check whether the user name and password matches.#don't need this function
def check_user_pwd_match(user, pwd):
    myquery = """SELECT COUNT(*) FROM users WHERE user='"""+user+"""' AND password !='"""+pwd+"""'"""
    return DB().query(myquery)

