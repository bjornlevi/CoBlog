# coding=utf-8
from modules.DB import DB
"""
Table: ID, group
"""
class Group(DB):
    
    table = ('ID', 'group_name', 'creator', 'date')
    table_name = 'groups'
    
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table groups (%s integer primary key, %s text, %s text, %s text)''' % self.table)
        except:
            pass
        
    def get_group(self, group):
        return self.get("where group_name='"+group+"'")
