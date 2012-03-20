# coding=utf-8
#Shuo, exercise 2012-02-15

from model.Settings import Settings # from file import class
import sqlite3
from model.DB import DB
import datetime #to get the current system time when inserting an element to the sesstion table.

def helloShuo():
    return 'Hello Shuo' 

#SHUO. when a user login, add the user name, session id, current time to the table sessions      
def add_session(user, sessionid):
    #get the current time
    now = datetime.datetime.now()
    current_time = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'  '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
    myquery = """INSERT INTO sessions VALUES (NULL, '"""+user+"""','"""+sessionid+"""','"""+current_time+"""')"""
    message = ''
    try:
        DB().raw_query(myquery)
    except:
        message += '<p>[TESTING]ERROR in Session().add_session</p>'   
        return message     
    
    message +='<p>[TESTING]Successfully add '+user+', '+sessionid+', '+current_time+' to sessions table.</p>'
    return message

def delete_session(user):
    myquery = """DELETE FROM sessions WHERE user = '"""+user+"""'"""
    message =''
    try:
        DB().raw_query(myquery)
    except:
       message +='<p>[TESTING]ERROR in Session().delete_session.</p>'
       return message
   
    message +='<p> [NOTICE]Successfully delete user '+user+' from the sessions tabnle.</p>'
    return message
    
def get_time():
    now = datetime.datetime.now()
    return str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'  '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
         
#SHUO. works. returns all the groups' name and database'name in the table groups    
def get_groups():
    #make table if not exists
    #query create table ...
    #select * from groups
    #execute sql query and return fetchall
    
    #try:DB().create_table()
    #except: pass
    
    return DB().query('SELECT * FROM groups')

#shuo
def add_group(groupname, dbname):
    #change schema to group, date, creator
    message = ''
    myquery = """INSERT INTO groups VALUES (NULL, '"""+groupname+"""','"""+dbname+"""')"""
    try:
        DB().raw_query(myquery)
    except:
        message +='<p>ERROR in model.add_group</p>'
        return message
    return '<p>Successfully add a group:'+groupname+','+dbname+'</p>'
    

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

#SHUO. joining a group means adding an entry to  the accesses table
#Questions; who assigns the role? What is the default value?
#What is the interface for joining a group
#get grouo from a list?
def join_group(user, groupname, role='student'):
    message = ''
    message +='<p>[TESTING] Join a group</p>'
    myquery = """INSERT INTO accesses VALUES (NULL,'"""+user+"""','"""+groupname+"""','"""+role+"""')"""
    try:
        DB().raw_query(myquery)
    except:
        message +='<p>[ERROR] cannot join a group</p>'
        return message
    message +='<p>[NOTICE]'+user+' joins group '+groupname +' as '+role+'. </p>'
    return message

#doesn't work write now.
def quit_group(user, groupname, role):
    message = ''
    message += '<p>[Testing] Quit a group as a certain role</p>'
    mequery = """ DELETE FROM accesses WHERE user = '"""+user+"""' AND group_name = '"""+groupname+"""' AND role = '"""+role+"""'"""
    try:
        DB().raw_query(myquery)
    except:
        message +='<p>[ERROR] cannot quit a group</p>'
        return message
    message += '<p> [NOTICE]Remove '+user+'('+role+') from group '+groupname
    return message