# coding=utf-8
import bottle
from Session import Session
import model
from DB import DB

bottle.debug(True)

def application():
    return bottle.app()

def get_sessionid():
    return bottle.request.cookies.get('sessionid', '0')

#SHUO. assume the session table we have is "CREATE TABLE sessions (id integer primary key, user text, sessionid text, date text)"
def session():
    sessionid = bottle.request.cookies.get('sessionid', '0')
    if Session().is_valid(bottle.request.cookies.get('sessionid', '0')):
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

@bottle.get('/user/<user>')
def user_page(user):
    return user + ':' + Session().get_sessionid(user)[0]['sessionid']

@bottle.get('/login')
def login_form():
    user = Session().get_user(get_sessionid())
    if user:
        return "you are already logged in"
    else:
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
        #add session
        #add redirect
        message += '<p>FOUND '+str(result)+' matched users in database.</p>'
        bottle.response.set_cookie('sessionid', Session().create_session(user))
        #add redirect to a user specify page.
        #for now, test logout
        message +="""<p> Please click Log Out to exit</p>
                    <a href = "logout/<user>">Log Out</a>"""
        
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
            bottle.redirect('/user/'+user)
        #[MODIFY]should jump to different pages.     
    #set cookie
    #bottle.response.set_cookie('sessionid', user, 'asdf')
    #[MODIFY] ADD TO SESSION TABLES
    return message

#just test log out. must odify later.put the             
@bottle.route('/logout')
def logout():
    #pass the user, and delete entries in sessions table
    message = ''
    message ='<p>[TESTING] Log Out</p><hr/>'
    message +=Session().delete_session(get_sessionid())
    message ='Log Out sucessfully.:)'   
    
    return message

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
        <p><label for="database">Database: </label><input type="text" name="dbname" id = "database"/></p>
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
    dbname = bottle.request.forms.get('dbname')
    message +=model.add_group(groupname, dbname)
    
    message +="<hr/><p>[TESTING] list all the groups in the database</p>"
    
    for row in model.get_groups():
        message +='<p>'+row['group_name']+','+row['db_name']+'</p>'
        
   
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

@bottle.get('/')
def hello():
    return 'list of groups + link to create a group if admin'

@bottle.get('/groups/create')
def create_group():
    return 'form for creating the group'

@bottle.post('/groups/create')
def add_group():
    #name restriction: ONE WORD - CAN'T START WITH A NUMBER
    #and name is lower cased before processing
    return 'the actual "adding" of the group --- creating the DB'


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
    dbname = 'DB-'+groupname
    message = '<p>[TEST] Add a group</p></hr>'
    message +=model.add_group(groupname, dbname)
    
    message +=model.add_group('GroupB','DB-B')
    message +=model.add_group('GroupC','DB-C')
    
    for row in model.get_groups():
        message += '<p>'+row['group_name']+','+row['db_name']+'</p>'
    
    return message

@bottle.get('/test4')
def shuotest4():
    message =''
    message +='<p> current time:'+model.get_time()+'</p>'
    return message

#test generat unique and secure session id
@bottle.get('/test5')
def shuotest5():
    message = '<p>[TESTING] generate session id</p>'
    message +='<p> session id is: '+ str(Session().generate_session_id())+'</p>';
    return message

#test select * from session table
@bottle.get('/test6')
def shuotest6():
    message = ''
    message +='<p>[TESTING] list contents from the session table</p>'
    
    for row in DB().query('SELECT * FROM sessions'):
        message +='<p>' + row['user']+','+row['sessionid']+','+row['date'] + '</p>'        
    return message

#test the funation of deleteing a session
@bottle.get('/test7')
def shuotest7():
    message =''
    user = 'bjorn'
    message +='<p>[TESTING] DELETE sessions</p><hr/>'
    message +=Session().delete_session(user)
    return message

#test the function of joining a group
@bottle.get('/test8')
def shuotest8():
    message =''
    user = 'bjorn'
    groupname = 'HCI'
    role = 'admin'
    
    message +=model.join_group(user,groupname,role)
    message +=model.join_group('Shuo','HCI')
    return message

#test quiting a group. doesn't work. need to check.
@bottle.get('/test9')
def shuotest9():
    message = ''
    message +=model.quit_group('Shuo','HCI','student')
    return message
    
    