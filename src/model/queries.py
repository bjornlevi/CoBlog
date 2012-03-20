# coding=utf-8
#This file defines the schema of tables

#######################LOCAL TABLE####################################
#posttable: (id, date, title, post, user, status)
create_post_table = """"CREATE TABLE posts (id integer primary key, date text, title text, post text, user text, status text)"""

#Shuo, comment_table, in each group dataase
create_comment_table = """ CREATE TABLE comments (id integer PRIMARY KEY, date text, content text, post text, user text)"""

###########################  GLOBAL TABLE  #############################################
#Shuo, user_table, global #what information do we need to store, in addition to username and password?
q_create_user_table = """ CREATE TABLE users (id integer PRIMARY KEY, user text, pwd text, email text )"""

# ???why do we put image in user_settings_table?~instead of user_table
q_create_user_settings_table = """CREATE TABLE user_settings (id integer primary key, user text, image text, group text, about text)"""

# ???table groups other attribute? How do the system link to a single group's database? 
q_create_group_table = """ CREATE TABLE groups (id integer PRIMARY KEY, group_name text, db_name text)"""

q_create_access_table = """CREATE TABLE access (id integer primary key, user text, group text, role text)"""
#for example user in group global with role 'admin' can create new groups
#user with group 'internet and society' and role 'admin' can't create new groups
#he can however accept group applications and assign roles for people in that group
#group creator automatically becomes group admin as well

##############################  USE FOR Login/Logout   ####################
q_create_session_table = """CREATE TABLE sessions (id integer primary key, user text, sessionid text, date text)"""


################################# DROP TABLES, just for test  ###########################
drop_user_table =""" DROP TABLE users"""
drop_user_setting_table = """"DROP TABLE user_settings"""
drop_group_table ="""" DROP TABLE groups"""
drop_access_table = """"DROP TABLE accesses"""
drop_post_table = """DROP TABLE posts"""
drop_comment_table = """DROP TABLE comments"""

################################INSERT INTO TABLES



###############################  ALL QUERIES OVER TABLES#################q##
q_get_all_users = """SELECT * FROM users"""
q_get_all_groups = """SELECT * FROM groups"""