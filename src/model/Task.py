# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, post
Each post can be assigned many users but user only once to each post.
"""

class Task(DB):
    table = ('ID','user','post')
    table_name = 'task'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table task (%s integer primary key, %s text, %s text)''' % self.table)
        except:
            pass

    
