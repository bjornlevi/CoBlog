# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, post, date
- each user can only like a post once
"""

class Like(DB):
    table = ('ID','user','post','date')
    table_name = 'like'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table like (%s integer primary key, %s text, %s text, %s text)''' % self.table)
        except:
            pass
    
    def get_user_likes_before(self, user, date):
        return self.get("where user='"+user+"' and date < '"+date+"'")