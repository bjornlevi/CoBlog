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
    
    def new_session(self, user_name):
        #create a sessionid to save and return
        char_set = string.ascii_uppercase + string.ascii_lowercase + string.digits
        sessionid = ''.join(random.sample(char_set,24))

        #set hard limit on cookie lifetime = 1 day
        expires = datetime.datetime.now() + datetime.timedelta(days=1)

        #delete any sessions this user already has
        try:
            self.database.raw_query('delete from sessions where user_name = ?', [user_name])
        except:
            pass

        # Insert a row of data
        try:
            self.database.add_data('sessions', [sessionid, expires, user_name])
            return sessionid
        except Exception, e:
            return ()    
