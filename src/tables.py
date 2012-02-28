create_post_table = """"create table posts (id integer primary key, date text, title text, post text, user text, status text)"""
create_comment_table = """ """
create_user_table = """ """
create_user_settings_table = """create table user_settings (id integer primary key, user text, image text, group text, about text)"""
create_group_table = """ """
create_access_table = """create table access (id integer primary key, user text, group text, role text)"""
#for example user in group global with role 'admin' can create new groups
#user with group 'internet and society' and role 'admin' can't create new groups
#he can however accept group applications and assign roles for people in that group
#group creator automatically becomes group admin as well
create_session_table = """create table sessions (id integer primary key, user text, sessionid text, date text)"""