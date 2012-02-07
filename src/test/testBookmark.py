# coding=utf-8
from Bookmark import Bookmark
import testFunctions as tf
"""
Table: ID, user, post, date
"""

b = Bookmark()
data = {'user':'testuser', 'post':'1', 'date':tf.now()}
#create some data
b.post(data)
print b.get()
print b.get_user_info('testuser')
print b.get_post_info('1')
print b.delete({'user':'testuser'})