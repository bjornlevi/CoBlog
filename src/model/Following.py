# coding=utf-8
from modules.DB import DB
"""
Table: 'ID', 'user', 'following'
"""

class Following(DB):
    table = ('ID', 'user', 'following')
    table_name = 'following'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table following (%s integer primary key, %s text, %s text)''' % self.table)
        except:
            pass
        
    def get_followers(self, user):
        return self.get("where following='"+user+"'")
    