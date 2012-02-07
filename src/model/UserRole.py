# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, group, role
each user can have many roles in one group
only has to have one entry of each role per group
User roles are:
- admin (group admin)
- grader (group grader)
- student (group member)
- applying (applying to the group)
"""

class UserRole(DB):
    table = ('ID','user','group_name','role')
    table_name = 'user_role'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table user_role (%s integer primary key, %s text, %s text, %s text)''' % self.table)
        except:
            pass
    
    def get_applications(self, group):
        return self.get("where group_name='"+group+"' and role='applying'")
    
    def is_system_admin(self, user):
        return self.get("where user ='"+user+"' and group='system' and role='admin'")
    
    def make_system_admin(self, user):
        if self.is_system_admin(user):
            pass
        else: #add
            self.post({'user':user,'group_name':'system','role':'admin'})
            
    def remove_system_admin(self, user):
        admin = self.is_system_admin(user)
        if admin:
            self.delete({'ID':admin['ID']})
    
    def is_group_admin(self, user, group):
        return self.get("where user ='"+user+"' and group='"+group+"' and role='admin'")
    
    def make_group_admin(self, user, group):
        if self.is_group_admin(user, group):
            pass
        else: #add
            self.post({'user':user,'group_name':group,'role':'admin'})

    def remove_group_admin(self, user, group):
        admin = self.is_group_admin(user, group)
        if admin:
            self.delete({'ID':admin['ID']})
    
    def is_group_grader(self, user, group):
        return self.get("where user ='"+user+"' and group='"+group+"' and role='grader'")
        
    def make_grader(self, user, group):
        if self.is_group_admin(user, group):
            pass
        else: #add
            self.post({'user':user,'group_name':group,'role':'grader'})
    
    def remove_grader(self, user, group):
        grader = self.is_group_admin(user, group)
        if grader:
            self.delete({'ID':grader['ID']})