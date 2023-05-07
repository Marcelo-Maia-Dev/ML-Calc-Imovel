# importar os pacotes 
import flask 
import pandas as pd 

app = flask.Flask(__name__, template_folder='templates')

@app.router("/")
def main():
    df = pd.read_csv("http://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2019-07-15/visualisations/listings.csv")


    return flask.render_template('index.html')
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
 