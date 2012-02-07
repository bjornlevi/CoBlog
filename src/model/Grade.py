# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, post, date, grade, comment
- TA grading
"""

class Grade(DB):
    table = ('ID','user','post','date','grade','comment')
    table_name = 'grade'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table grade (%s integer primary key, %s text, %s text, %s text, %s text, %s text)''' % self.table)
        except:
            pass

    