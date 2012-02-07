# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, post, highlight, note, date
each user can have many notes for each post
"""

class UserNote(DB):
    table = ('ID','user','post','highlight','note','date')
    table_name = 'user_note'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table user_note (%s integer primary key, %s text, %s text, %s text, %s text, %s text)''' % self.table)
        except:
            pass
    