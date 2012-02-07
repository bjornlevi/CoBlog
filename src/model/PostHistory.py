# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, title, post, date, status, group
"""
class PostHistory(DB):
    table = ('ID', 'user', 'title', 'post', 'date', 'original')
    table_name = 'post_history'    
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table post_history (%s integer primary key, %s text, %s text, %s text, %s text, %s text)''' % self.table)
        except Exception, e:
            print e