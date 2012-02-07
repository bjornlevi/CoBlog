# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, image, lastlogin
"""

class UserPreferences(DB):
    table = ('ID','user','image','lastlogin')
    table_name = 'user_preferences'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table user_preferences (%s integer primary key, %s text, %s text, %s text)''' % self.table)
        except:
            pass
    
    def add_image(self, user, image):
        """
        overrides existing image
        """
        try:
            row_id = self.get("where user='"+user+"'")
            self.edit({'ID':row_id['ID']}, ['image',image])
        except:
            pass
    
    def update_login(self, user, lastlogin):
        """
        updates lastlogin to NOW
        """
        try:
            row_id = self.get("where user='"+user+"'")
            self.edit({'ID':row_id['ID']}, ['lastlogin',lastlogin])
        except:
            pass