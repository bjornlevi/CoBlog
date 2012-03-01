# coding=utf-8
#Shuo, exercise 2012-02-15

from Settings import Settings # from file import class
import sqlite3

def helloShuo():
    return 'Hello Shuo'

class DB(object):
    
    table = None #[col1, col2, ...]
    table_name = None
    
    #function, _init_(self)
    def __init__(self):
        object.__init__(self)
        self.database = Settings().appDB
        self.connect()
        self.commit_and_close()
        
    def connect(self):
        self.connection = sqlite3.connect(self.database)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def commit_and_close(self):
        self.commit()
        self.close()
        
    def login(self, post):
        #table check
        
        self.query(' create table users (id integer primary key, user text, password text, email text )')
        
    def query(self, query):
        try:
            self.connect()
            self.cursor.execute(query)
            results = self.cursor.fetchall()
        except Exception, e:
            print e
        finally:
            self.commit_and_close()
            return results
            
    #Shuo, test create a table,
    def create_table(self):
        #global table
        self.query('create table users (id integer primary key, user text, password text, email text)')
        self.query('create table groups (id integer primary key, group_name text, database text)')
       # self.query('')
    
    def insert_user(self, id, user, password, email):
        #self.query("""INSERT INTO users VALUES (id,user,password,email)""")
        pass
    
def get_groups():
    #make table if not exists
    #query create table ...
    #select * from groups
    #execute sql query and return fetchall
    try:DB().create_table()
    except: pass
    #DB().insert_user(1, 'shuo', '123', 'sdiao@brandeis.edu')
    #DB().query("""INSERT INTO users VALUES (1, 'shuo', '123','sdiao@brandeis.edu')""")
    DB().query("""INSERT INTO users VALUES (NULL, 'bjorn', '123','bjorn@brandeis.edu')""")
    return DB().query('select * from users')
            
            