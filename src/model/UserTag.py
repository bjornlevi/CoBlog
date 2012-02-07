# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, post, tag
- each user can tag a single post many times
"""

class UserTag(DB):
    table = ('ID','user','post','tag')
    table_name = 'user_tag'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table user_tag (%s integer primary key, %s text, %s text, %s text)''' % self.table)
        except:
            pass
