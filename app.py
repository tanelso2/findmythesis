from flask import Flask, redirect, render_template, url_for
import werkzeug.exceptions

from thesis import get_thesis_topic

app = Flask(__name__)


@app.route('/')
def thesis():
    return render_template('index.html', thesis=get_thesis_topic())


@app.route('/test')
def test():
    return render_template('index.html',
                           thesis='Testing: A survey of secret access & simplicity in an age of containers')


@app.errorhandler(werkzeug.exceptions.NotFound)
def redirect_to_main(_):
    return redirect(url_for('thesis'))
