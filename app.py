from flask import Flask, render_template

from thesis import get_thesis_topic

app = Flask(__name__)

@app.route('/')
def thesis():
    return render_template('index.html', thesis=get_thesis_topic())
