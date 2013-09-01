from gevent import monkey
monkey.patch_all()
from gevent.wsgi import WSGIServer
from env import ENV 
cli = ENV.parse_cli(['env=','port=']) 

from flask import Flask, abort, request, jsonify, make_response, url_for, g, redirect, Response,current_app

flask_app = Flask(__name__)

@flask_app.route('/tasks',methods=["GET"])
def route_get_tasks():
    pass

@flask_app.route('/tasks',methods=["PUT"])
def route_put_tasks():
    pass

@flask_app.route('/tasks',methods=["POST"])
def route_post_tasks():
    pass

@flask_app.route('/tasks',methods=["DELETE"])
def route_delete_tasks():
    pass

if __name__ == '__main__':
    http_server = WSGIServer(('', int(cli['--port'])), flask_app)
    print 'SERVING!'
    http_server.serve_forever()
