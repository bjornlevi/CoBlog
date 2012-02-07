# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, post, comment, date
- each user can comment a single post many times
"""

class Comment(DB):
    table = ('ID','user','post','comment','date')
    table_name = 'comment'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table comment (%s integer primary key, %s text, %s text, %s text, %s text)''' % self.table)
        except:
            pass