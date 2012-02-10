import sys

# Path of the directory where scripts directory is located.
#sys.path.insert(0, '/home/bjornlevi/coblog/bin')
sys.path.insert(0, 'c:\\Users\\bjorn\Documents\\Programming\\CoBlog\\src')

import Response
# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi
application = Response.application()