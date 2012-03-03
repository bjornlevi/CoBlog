# coding=utf-8
import bottle
from Session import Session
import model
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
    #return 'registration page'
    return """<p>[TESTING] registration page </p><hr/>
            <form method="post">
            <p><label for="user">User name: </label><input type="text" name="user" id="name" /></p>
            <p><label for="user">Password: </label><input type="password" name="password" /></p>
            <p><label for="email">Email: </label><input type="text" name="email" /></p>
            <p><input type="submit" value="Register"></p>
            </form>"""
            
@bottle.post('/register')
def add_user():
    #SHUO: should get name, pwd, and emial from the registration page. 
    #name = 'Jeanne'
    #pwd = '222'
    #email = name +'@brandeis.edu' 
    name = bottle.request.forms.get('user')
    pwd = bottle.request.forms.get('password')
    email = bottle.request.forms.get('email')
    
    results = ''
    results +=model.add_user(name, pwd, email)
    return results
    #return 'register new user if user name does not exist'

@bottle.get('/login')
def login_form():
    return """<form method="post">
        <p><label for="user">User name: </label><input type="text" name="user" id="name" /></p>
        <p><label for="user">Password: </label><input type="password" name="password" /></p>
        <p><input type="submit" value="Log in"></p>
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
            #bottle.redirect('/relogin')#not correct.
            bottle.redirect("relogin")
            #[MODIFY] link to login page
        else:
            message +="""<p> Welcome new user. Please Register first. :)</p>"""
            bottle.redirect("register")
        #[MODIFY]should jump to different pages.     
    
    bottle.response.set_cookie('sessionid', user, 'asdf')
    #[MODIFY] ADD TO SESSION TABLES
    return message

@bottle.get('/relogin')
def relogin():

    #bottle.redirect('login')
    return """<p>Please check your password and click re-login. </p>
            <a href="login">Re-Login</a>"""

@bottle.get('/groups')
def get_groups():
    results = ''
    #results +='<p>[TEST] show groups</p>'
    #for row in model.get_groups():
        #results += '<p>'+row['group_name']+row['database']+'</p>'
    #for row in model.get_groups():
        #results += '<p>'+str(row['total_user'])+'</p><hr/>'
        
    #list the form
    results +='<p>[TEST]Create a new group here</p><hr/>'
    results += """<form method="post">
        <p><label for="groupname">Group Name: </label><input type="text" name="groupname" id="groupname" /></p>
        <p><label for="database">Database: </label><input type="text" name="database" id = "database"/></p>
        <p><input type="submit" value="Create a group"></p>
        </form>
        """
    return results
    
    #return 'list of groups <form method="post" action=""><input type="text" name="test"><input type="submit"></form>'

@bottle.post('/groups')
def add_group():
    #get information from form. then call model.addgroup
    message = ''
    groupname = bottle.request.forms.get('groupname')
    database = bottle.request.forms.get('database')
    message +=model.add_group(groupname, database)
   
    return message

@bottle.post('/groups/:group')
def edit_group():
    return 'edit group'

@bottle.post('/user')
#[MODIFY]should delete later

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
@bottle.get('/test1')
def shuotest1():  
    results = ''
    results += '<p>[TEST] ADD a user, list the number of users, and all users name and email</p>'
    name = 'Lucy'
    pwd = 'llll'
    email = name +'@brandeis.edu' 
    
    #test
    #model.add_user(name,pwd,email)
    
    #for count in  model.add_user('Alex','1','alex@brandeis.edu'):
        #results += '<p>add a new user</p><br/><p>current total number of users: ' + str(count['total_user']) + '</p><hr/>'

    #results +='<p>TOTAL USERS: '+str(model.add_user('Kiki','000','kiki@brandeis.edu'))+'</p>'
    #test
    for total in DB().query('SELECT COUNT(*) AS total_user FROM users'):
        results +='<p>total users:'+str(total['total_user'])+'</p>'
        
    #test, add a user
    results +='<p>[TEST] Add a user:'+model.add_user(name,pwd,email)+'</p>'
    
    
    for row in model.get_users():
        results += '<p>'+row['user']+' '+ row ['email']+'</p>'
    
    return results

###test for creating tables
#[MODIFY]. it doesn't work now.
@bottle.get('/test2')
def shuotest2():
    return model.create_user_settings()

@bottle.get('/test3')
def shuotest3():
    groupname='Design'
    database = 'DB-'+groupname
    message = '<p>[TEST] Add a group</p></hr>'
    message +=model.add_group(groupname, database)
    
    message +=model.add_group('GroupB','DB-B')
    message +=model.add_group('GroupC','DB-C')
    
    for row in model.get_groups():
        message += '<p>'+row['group_name']+','+row['database']+'</p>'
    
    return message
    