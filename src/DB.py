# coding=utf-8
from Settings import Settings
import sqlite3

class DB(object):
    
    table = None #[col1, col2, ...]
    table_name = None
    
    def __init__(self):
        object.__init__(self)
        self.database = Settings().appDB
        self.connect()
        self.close()
        
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database)
            self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()
        except Exception, e:
            print e

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def commit_and_close(self):
        self.commit()
        self.close()

    def raw_query(self, query):
        """
        take a raw sql query and execute it
        @query: the sql query
        """
        try:
            self.connect()
            self.cursor.execute(query)
        except Exception, e:
            print e
        finally:
            self.commit_and_close()

    def raw_query_return(self, query):
        """
        take a raw sql query and execute it
        @query: the sql query
        """
        try:
            self.connect()
            self.cursor.execute(query)
        except Exception, e:
            print e
        finally:
            results = self.cursor.fetchall()
            self.commit_and_close()
            return results
    
    def get(self, query, values=()):
        """
        get all data from table_name
        @query is the sql query
        Error and empty results return []
        otherwise returns [{row1},{row2},...] 
        dict for every row that matches query
        """
        results = []
        try:
            self.connect()
            self.cursor.execute(query, values)
            results = self.cursor.fetchall()
        except Exception, e:
            print e
        finally:
            self.commit_and_close()
            return results
        
    def post(self, data):
        """
        data = {key1:value, key2:value, ...}
        if self.table then try to add data
        when adding, all entries must be filled
        Raises KeyError if data (column) is missing
        Raises ValueError if DB table is missing
        Returns inserted ID if successful
        """
        query = 'insert into ' + self.table_name + ' values (NULL' + ',?'*len(data) + ')'
        query_data = []
        if self.table:
            for col in self.table[1:]: #skip leading ID
                try:
                    query_data.append(data[col])
                except Exception, e:
                    print e
                    raise KeyError
            self.connect()
            try:
                self.cursor.execute(query, query_data)
            except Exception, e:
                print e, query, query_data
                raise ValueError
            inserted_id = self.cursor.lastrowid
            self.commit_and_close()
            return inserted_id
        raise ValueError
    
    def edit(self, row_id, data):
        """
        updates data to provided table of database
        @data: dictionary of columns and values
        @row_id: dictionary of name of id column and the value {'id_col':'id_value}
        returns True or False depending on success
        """
        query = 'update ' + self.table_name + ' set '
        values_list = []
        for key, value in data.items():
            values_list.append(value)
            query += key +"=?,"
        #erase the last ','
        query = query[:-1]
        query += ' where ' + str(row_id.keys()[0]) + "='" + str(row_id[row_id.keys()[0]]) + "'"
        try:
            self.connect()
            self.cursor.execute(query, values_list)
            self.commit_and_close()
            return True
        except:
            self.close()
            return False
    
    def delete(self, row_id):
        """
        @row_id: dictionary of name of id column and the value {'id_col':'id_value}
        returns True or false depending on success
        """
        query = 'delete from ' + self.table_name
        query += ' where ' + str(row_id.keys()[0]) + "='" + str(row_id[row_id.keys()[0]]) + "'"
        try:
            self.connect()
            self.cursor.execute(query)
            self.commit_and_close()
            return True
        except:
            self.close()
            return False        