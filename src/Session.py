# coding=utf-8
from DB import DB
#reference: how to create session id
#http://stackoverflow.com/questions/817882/unique-session-id-in-python
#import base64, M2Crypto#doesn't work 
import os, base64 # to generate session_id
import datetime #to get the current system time when inserting an element to the sesstion table.

"""
Table: ID, user, session, date
- each user can comment a single post many times
"""

class Session(DB):
    table = ('ID','user','sessionid','date')
    #table_name = 'session'
    table_name = 'sessions'
    def __init__(self):
        DB.__init__(self)
        try:
            self.raw_query('''create table sessions (%s integer primary key, %s text, %s text, %s text)''' % self.table)
        except:
            pass
        
    def is_valid(self, sessionid):
        return self.get("select * from sessions where sessionid=?", (sessionid,))
    
    def get_sessionid(self, user):
        return self.get("select sessionid from sessions where user=?", (user,))    
    
    def get_user(self, sessionid):
        return self.get("select user from sessions where sessionid=?", (sessionid,))
    
    #SHUO, add code here. 
    def create_session(self, user):
        now = datetime.datetime.now()
        expires = datetime.datetime.now() + datetime.timedelta(days=1)
        #current_time = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'  '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
        session_id = self.generate_session_id()
        #needs to be like this: """INSERT INTO sessions VALUES (NULL, ?,?,?)"""
        #and use database.execute(query, parameters)
        myquery = """INSERT INTO sessions VALUES (NULL, '"""+user+"""','"""+session_id+"""','"""+str(expires)+"""')"""
        message = ''
        try:
            DB().raw_query(myquery)
        except Exception, e:
            print 'failed to create session: ' + str(e)  
            return message     
    
        #message +='<p>[TESTING]Successfully add '+user+', '+session_id+', '+current_time+' to sessions table.</p>'
        return session_id
        
        #pass
        
    def delete_session(self, sessionid):
        myquery = """DELETE FROM sessions WHERE sessionid = '"""+sessionid+"""'"""
        try:
            DB().raw_query(myquery)
        except:
            pass
        return 'logged out'
        
    #def generate_session_id(self, num_bytes = 16):#this funciton doesn't work
        #return base64.b64encode(M2Crypto.m2.rand_bytes(num_bytes))
        
    #maybe it is not safe now
    def generate_session_id(self,num_bytes = 16):
        return base64.b64encode(os.urandom(num_bytes))