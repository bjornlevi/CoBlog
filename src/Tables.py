# coding=utf-8
from Settings import Settings
import sqlite3
import bottle


get_all_posts = """select * from posts"""
get_all_user_posts = """select * from posts where user = ?"""
#cursor.execute(get_all_user_posts, ('bjorn'))
get_all_user_posts_after = """select * from posts where user = ? and date > ?"""
#cursor.execute(get_all_user_posts_after, ('bjorn','01-01-2012 00:00:00'))


#SHUO define all the SQL strings here
