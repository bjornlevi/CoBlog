# coding=utf-8
from modules.DB import DB
"""
Table: ID, user, title, post, date, status, group
"""
class Post(DB):
	table = ('ID', 'user', 'title', 'post', 'date', 'status', 'group_name')
	table_name = 'post'
	
	def __init__(self):
		DB.__init__(self)	
		try:
			self.raw_query('''create table post (%s integer primary key, %s text, %s text, %s text, %s text, %s text, %s text)''' % self.table)
		except:
			pass
		
	def get_post(self, post):
		return self.get("where ID = '" + post + "'")
	
	def get_group_posts(self, group):
		return self.get("where group_name ='"+group+"'")
