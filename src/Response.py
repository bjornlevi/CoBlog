# coding=utf-8
import bottle
from Session import Session
from DB import DB

bottle.debug(True)

def application():
    return bottle.app()

def session():
    sessionid = bottle.request.cookies.get('sessionid', '0')
    if Session().is_valid(sessionid):
        bottle.response.set_cookie('sessionid', sessionid)
        return Session().get_user(sessionid)
    else:
        return None

@bottle.get('/register')
def register():
    return 'registration page'

@bottle.get('/login')
def login_form():
    DB().raw_query('create table users (id integer primary key, user text, email text, password text)')
    DB().raw_query("""insert into users values (NULL, 'bjorn', 'bjornlevi@gmail.com', 'pass')""")
    return 'login form' + str(DB().raw_query_return('select * from users'))

@bottle.post('/login')
def login_submit():
    name     = bottle.request.forms.get('name')
    password = bottle.request.forms.get('password')
    bottle.response.set_cookie('sessionid', name, 'asdf')
    return "<p>"+name + ':'+ password +"</p>"

@bottle.get('/groups')
def get_groups():
    return 'list of groups'

@bottle.post('/groups')
def add_group():
    return 'create new group'

@bottle.post('/groups/:group')
def edit_group():
    return 'edit group'

@bottle.post('/user')
def add_user():
    return 'register new user if user name does not exist'

@bottle.get('/user/:user')
def get_user():
    return 'user page'

@bottle.post('/user/:user')
def edit_user():
    return 'edit user'

@bottle.get('/posts')
def get_posts():
    return 'posts list'

@bottle.get('/posts/:post')
def get_post():
    return 'one post'

@bottle.post('/posts')
def add_post():
    return 'new post'

@bottle.post('/posts/:post')
def edit_post():
    return 'edit post'

@bottle.post('/posts/:post/comment')
def add_comment():
    return 'new comment'

@bottle.post('/posts/:post/comment/:commment')
def edit_comment():
    return 'edit comment'

@bottle.post('/posts/:post/like')
def add_like():
    """
    This method is activated by an ajax call and contains the type of like to add
    """
    return 'new like'

@bottle.route('/')
def hello():
    count = int( bottle.request.cookies.get('counter', '0') )
    count += 1
    bottle.response.set_cookie('counter', str(count))
    return 'You visited this page %d times' % count