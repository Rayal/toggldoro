from flask import Flask, make_response, request, Response, abort
from flask.helpers import NotFound

import timers

app = Flask(__name__)


# TODO: User identification & HTTPS


@app.route('/')
def hello_world():
    return 'Hello World!'


# TODO: Redirect to timer page??
@app.route('/start', methods=['POST'])
def start_timer():
    req = request.json
    uid = timers.start_timer(req['title'])
    return {'uuid': uid}


# TODO: Add log. Redirect to logs page??
@app.route('/stop', methods=['PUT'])
def stop_timer():
    req = request.json
    try:
        title, elapsed = timers.stop_timer(req['uuid'])
        return {
            'title': title,
            'elapsed': elapsed
        }
    except KeyError:
        abort(400)


# TODO: Add log. Redirect?
@app.route('/log', methods=['POST'])
def add_log():
    pass


@app.route('/timer/<uid>')
def get_timer(uid):
    try:
        title, elapsed = timers.get_time(uid)
        return {
            'title': title,
            'elapsed': elapsed
        }
    except KeyError:
        abort(400)


# TODO
@app.route('/logs')
def get_logs():
    pass


if __name__ == '__main__':
    app.run()
