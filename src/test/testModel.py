import random
import string
from Bookmark import Bookmark
from Comment import Comment
from Grade import Grade
from Group import Group
from Like import Like
from Notification import Notification
from Post import Post
from PostHistory import PostHistory
from Task import Task
from User import User
from UserGrade import UserGrade
from UserNote import UserNote
from UserPreferences import UserPreferences
from UserRole import UserRole
from UserTag import UserTag
from Log import Log
from Following import Following
from Gold import Gold

bookmark = Bookmark()
comment = Comment()
grade = Grade()
group = Group()
like = Like()
notification = Notification()
post = Post()
post_history = PostHistory()
task = Task()
user = User()
user_grade = UserGrade()
user_note = UserNote()
user_preferences = UserPreferences()
user_role = UserRole()
user_tag = UserTag()
log = Log()
following = Following()
gold = Gold()

tests = [bookmark, comment, grade, group,
         like, notification, post, post_history, task, user, user_grade,
         user_note, user_preferences, user_role, user_tag, like, following, gold]

def random_word():
    return ''.join(random.sample(string.ascii_lowercase, random.randint(1, 12))) + ' '

def random_data(keys):
    results = {}
    for key in keys:
        results[key] = random_word()
    return results

for test in tests:
    print test.__class__
    data = random_data(test.table[1:])
    row_id = test.post(data)
    print 'results', test.get()[-1]
    edit_data = random_data(test.table[1:])
    if test.edit({'ID':row_id}, edit_data):
        print 'edit', test.get()[-1]
    else:
        print 'edit failed'
    if test.delete({'ID':row_id}):
        print 'delete', test.get()
    else:
        print 'delete failed'
