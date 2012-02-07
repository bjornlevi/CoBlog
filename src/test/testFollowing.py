# coding=utf-8
from Following import Following
import testFunctions as tf
"""
Table: 'ID', 'user', 'following'
"""
f = Following()
data = {'user':'testuser', 'following':'testuser2'}
f.post(data)
data = {'user':'testuser', 'following':'testuser3'}
f.post(data)
print f.get()
print f.get_user_info('testuser')
print f.get_followers('testuser2')
print f.delete({'user':'testuser'})