# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, email, password
user & email are unique!
"""

class User(DB):
    table = ('ID','user','email','password','status')
    table_name = 'user'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table user (%s integer primary key, %s text, %s text, %s text, %s text)''' % self.table)
        except:
            pass
        
    def set_email(self, user, email):
        u = self.get_user_info(user)
        try:
            self.edit({'ID':u['ID']}, ['email',email])
        except:
            pass
    
    def set_status(self, user, status):
        u = self.get_user_info(user)
        try:
            self.edit({'ID':u['ID']}, ['status',status])
        except:
            pass
    
    def set_password(self, user, password):
        u = self.get_user_info(user)
        try:
            self.edit({'ID':u['ID']}, ['password',password])
        except:
            pass
