# importando pacotes 
import flask
from flask import Flask
import pandas as pd
import pickle

# importando modelos e features 
with open('model/model.joblib', 'rb') as file:
    model = pickle.load(file)
with open('model/features.names', 'rb') as file:
    features = pickle.load(file)

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return flask.render_template('home.html')

    if flask.request.method == 'POST':
        # ver o que digitaram
        print(flask.request.form)

        # input para df
        df = pd.DataFrame(index=[0], columns=features)
        df.fillna(value=0, inplace=True)
        user_inputs = flask.request.form.items()
        for i in user_inputs:
            df[i[0]] = i[1]
        df = df.astype(float)

        # fazer a previsão
        Y_pred = model.predict(df)[0]
        print(Y_pred)

        return flask.render_template("home.html", valor=Y_pred)

if __name__ == "__main__":
    app.run(debug=True)
