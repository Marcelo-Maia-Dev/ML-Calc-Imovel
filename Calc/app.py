# importando pacotes 
import flask
from flask import Flask

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
    return flask.render_template('home.html')

if flask.request.method == 'POST':
        # ver o que digitaram
        print(flask.request.form)
        return flask.render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
