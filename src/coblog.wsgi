import os, sys

# Path of the directory where scripts directory is located.
sys.path.insert(0, os.path.dirname(__file__))

import Response
# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi
application = Response.application()