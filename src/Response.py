# coding=utf-8
import bottle
from Session import Session

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

@bottle.get('/login')
def login_form():
    return '''<form method="POST">
                <input name="name" type="text" />
                <input name="password" type="password" />
                <input type=submit>
              </form>'''

@bottle.post('/login')
def login_submit():
    name     = bottle.request.forms.get('name')
    password = bottle.request.forms.get('password')
    bottle.response.set_cookie('sessionid', name, 'asdf')
    return "<p>"+name + ':'+ password +"</p>"

@bottle.route('/')
def hello():
    count = int( bottle.request.cookies.get('counter', '0') )
    count += 1
    bottle.response.set_cookie('counter', str(count))
    return 'You visited this page %d times' % count