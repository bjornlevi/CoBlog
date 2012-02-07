# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, session, date
- each user can comment a single post many times
"""

class Comment(DB):
    table = ('ID','user','session','date')
    table_name = 'comment'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table comment (%s integer primary key, %s text, %s text, %s text)''' % self.table)
        except:
            pass
        
    def is_valid(self, session):
        return self.get("where session='"+session+"'")