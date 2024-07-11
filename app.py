from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Ran Saadon, Man, 33'

