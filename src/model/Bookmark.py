# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, post
"""

class Bookmark(DB):
    table = ('ID', 'user', 'post', 'date')
    table_name = 'bookmark'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table bookmark (%s integer primary key, %s text, %s text, %s text)''' % self.table)
        except:
            pass
