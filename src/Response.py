# coding=utf-8
import bottle
from Session import Session
import model

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
    return """<form method="post">
        <p><label for="user">User name</label><input type="text" name="user" id="name" /></p>
        <p><label for="user">Password</label><input type="password" name="password" /></p>
        <p><input type="submit" value="log in"></p>
        </form>
        """

@bottle.post('/login')
def login_submit():
    user     = bottle.request.forms.get('user')
    password = bottle.request.forms.get('password')
    
    message = ''
    #SHUO:check log in    
    message +='<p>[TEST] Login Module</p><hr/>'
    message += '<p>' + user+':' + password +'</p>'
    message += '<p> CHECK IN DATABASE, PLEASE WAIT...</p>'
   
    result = 0 
    for row in (model.check_login(user, password)):
        result = row['found']
    
    if(result >0):
        message += '<p>FOUND '+str(result)+' matched users in database.</p>'     
    else:
        find_user = 0
        for row in (model.check_user(user)):
            find_user = row['find_user']
        
        if (find_user):
            message +="""<p>Username and Password doesn't match. Please re-check and login.:)</p>"""
            #[MODIFY] link to login page
        else:
            message +="""<p> Welcome new user. Please Register first. :)</p>"""
        #[MODIFY]should jump to different pages.     
    
    bottle.response.set_cookie('sessionid', user, 'asdf')
    #[MODIFY]
    return message

@bottle.get('/groups')
def get_groups():
    results = ''
    results +='<p>[TEST] show groups</p>'
    for row in model.get_groups():
        results += '<p>'+row['user']+'</p>'
    #for row in model.get_groups():
        #results += '<p>'+str(row['total_user'])+'</p><hr/>'
    return results
    
    #return 'list of groups <form method="post" action=""><input type="text" name="test"><input type="submit"></form>'

@bottle.post('/groups')
def add_group():
    test     = bottle.request.forms.get('test')
    return 'create new group ' + test

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
    data = model.helloShuo()
    count = int( bottle.request.cookies.get('counter', '0') )
    count += 1
    bottle.response.set_cookie('counter', str(count))
    return 'You visited this page %d times' % count + data


#########    SHUO Test   ######
@bottle.get('/test')
def shuotest():  
    results = ''
    results += '<p>[TEST] ADD a user, list the number of users, and all users name and email</p>'
    name = 'Emma'
    pwd = '222'
    email = name +'@brandeis.edu' 
    
    for count in  model.add_user(name,pwd,email):
        results += '<p>add a new user</p><br/><p>current total number of users: ' + str(count['total_user']) + '</p><hr/>'
    #results +='<p>TOTAL USERS: '+str(model.add_user('Kiki','000','kiki@brandeis.edu'))+'</p>'
        
    for row in model.get_users():
        results += '<p>'+row['user']+' '+ row ['email']+'</p>'
    
    return results
    