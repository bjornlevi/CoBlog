# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, post, grade, date
- each user grade each post once
"""

class UserGrade(DB):
    table = ('ID','user','post','grade','date')
    table_name = 'user_grade'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table user_grade (%s integer primary key, %s text, %s text, %s text, %s text)''' % self.table)
        except:
            pass
    
    def get_grade(self, user, post):
        return self.get("where user='"+user+"' and post='"+post+"'")
