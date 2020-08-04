from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# TODO: Set POST. Start timer. Redirect to timer page.
@app.route('/start')
def start_timer():
    pass


# TODO: Set POST. End timer. Redirect to logs page.
@app.route('/stop')
def stop_timer():
    pass


# TODO: Set POST. Add log. Redirect?
@app.route('/log')
def add_log():
    pass


# TODO
@app.route('/timer')
def get_timer():
    pass


# TODO
@app.route('/logs')
def get_logs():
    pass


if __name__ == '__main__':
    app.run()
