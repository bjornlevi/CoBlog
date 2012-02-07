# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, post, date
"""

class Log(DB):
    table = ('ID', 'user', 'action', 'date')
    table_name = 'log'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table log (%s integer primary key, %s text, %s text, %s text)''' % self.table)
        except:
            pass
    