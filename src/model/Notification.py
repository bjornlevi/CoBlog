# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, post, date, read
"""

class Notification(DB):
    table = ('ID','user','post','date','read','notifier')
    table_name = 'notification'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table notification (%s integer primary key, %s text, %s text, %s text, %s text, %s text)''' % self.table)
        except:
            pass
    