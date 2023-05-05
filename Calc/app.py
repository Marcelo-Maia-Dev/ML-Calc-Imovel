# importar os pacotes 
import flask 

app = flask.Flask(__name__, template_folder="Html")

@app.router("/")
def main():
    return flask.render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
