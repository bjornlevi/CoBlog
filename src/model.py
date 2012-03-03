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
    
    #try:DB().create_table()
    #except: pass
    
    return DB().query('SELECT * FROM groups')

#shuo
def add_group(groupname, database):
    message = ''
    myquery = """INSERT INTO groups VALUES (NULL, '"""+groupname+""",'"""+database+"""')"""
    try:
        DB().raw_query(myquery)
    except:
        message +='<p>ERROR in model.add_group</p>'
        return message
    return '<p>Successfully add a group:'+groupname+','+database+'</p>'
    

#SHUO
def add_user(user, pwd, email):
    myquery = """INSERT INTO users VALUES (NULL, '"""+user+"""','"""+pwd+"""','"""+email+"""')"""
    try:DB().raw_query(myquery)
    except:
        return 'ERROR!'
    return '<p>Successful!:)</p><p>'+user+','+pwd+','+email+'</p>'
    #return DB().query('SELECT COUNT(*) AS total_user FROM users')

    #return DB().row_count('SELECT * FROM users')# in sqlite3, the row is set to -1 for SELECT clause. 
    #[MODIFY] the return value later. Now, just use test messages
    
    
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

def create_user_settings():
    message =' '
    try:
        DB().raw_query(q_create_user_settings_table)
    except:
        message +="<p>[ERROR] create user settings</p>"
    return message

def create_tables():
    message ='<p>TESTING CREATE GLOBAL TABLES:)</p><hr/>'
    try: 
        DB().raw_query(queries.q_create_user_settings_table)
    except:
        message +='<p>[ERROR] cannot create table user_settings</p>'
    #message += '<p>[NOTICE] successfully created table user_settings</p>' 

    try:
        DB().raw_query(queries.q_create_access_table)
    except:
        message +='<p>[ERROR] cannot create table access</p>'
    #message +='<p>[NOTICE] successfully created table access</p>'
    
    try:
        DB().raw_query(queries.q_create_session_table)
    except:
        message += '<p>[ERROR] cannot create table sessions</p>'
    #message +='<p>[NOTICE]successfully created table sessions</p>'
    
    return message


