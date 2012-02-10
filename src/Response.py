# coding=utf-8
import bottle

bottle.debug(True)

def application():
    return bottle.default_app()

@bottle.route('/')
def hello():
    return "Hello World!"