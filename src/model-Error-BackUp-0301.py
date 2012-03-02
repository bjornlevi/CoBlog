# coding=utf-8
#Shuo, exercise 2012-02-15

#put controller's fucntions here
from Settings import Settings # from file import class
import sqlite3
#import DB
import queries

def helloShuo():
    return 'Hello Shuo'        
   

def get_groups():
    #make table if not exists
    #query create table ...
    #select * from groups
    #execute sql query and return fetchall
   
    #try:DB().create_table()
    #except: pass
    
    #DB().insert_user(1, 'shuo', '123', 'sdiao@brandeis.edu')
    #DB().query("""INSERT INTO users VALUES (1, 'shuo', '123','sdiao@brandeis.edu')""")
    DB().query("""INSERT INTO users VALUES (NULL, 'bjorn', '123','bjorn@brandeis.edu')""")
    return DB().query('select * from users')

def check_login(user, pwd):
    query = """SELECT id FROM users WHERE user = '"""+user+"""' AND password = '"""+pwd+"""'"""
    id = DB().query(query)
    return id

def add_user(user, pwd, email):
    query = """INSERT INTO users VALUES (NULL, '"""+user+"""','"""+pwd+"""','"""+email+"""')"""
    DB().raw_query(query)
    pass
    
#get all users from the users tablne. for testing.    
def get_users():
    myquery=queries.q_get_all_users
    return DB().query(myquery);

def get_user():#get only one user
    return 'test get user'
  
    
    
            
            