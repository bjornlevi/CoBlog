# coding=utf-8
from DB import DB
"""
Table: ID, user, session, date
- each user can comment a single post many times
"""

class Session(DB):
    table = ('ID','user','sessionid','date')
    table_name = 'session'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table session (%s integer primary key, %s text, %s text, %s text)''' % self.table)
        except:
            pass
        
    def is_valid(self, sessionid):
        return self.get("select * from session where sessionid=?", (sessionid,))
    
    def get_user(self, sessionid):
        return self.get("select user from session where sessionid=?", (sessionid,))

    def create_session(self, user):
        pass