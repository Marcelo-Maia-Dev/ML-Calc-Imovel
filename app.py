# importando pacotes 
import flask
from flask import Flask

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return flask.render_template("home.html")

if __name__ == "__main__":
    app.run()

