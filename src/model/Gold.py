# coding=utf-8
from modules.DB import DB

class Gold(DB):
    table = ('ID','grader','post','date')
    table_name = 'gold'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table gold (%s integer primary key, %s text, %s text, %s text)''' % self.table)
        except:
            pass
    