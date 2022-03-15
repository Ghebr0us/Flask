#realizzare un sito web per memorizzare le squadre di uno sport a scelta.
#L'utente deve poter inserire: il nome della squadra, la data di fondazione e la città.
#deve inoltre poter effettuare delle ricerche inserendo uno dei valori delle colonne e ottenendo i dati prensenti. 
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

dati = []

@app.route('/', methods=['GET'])
def home():
    return render_template("homepage.html")


@app.route('/create', methods=['GET'])
def create():
    return render_template("newteam.html")

@app.route('/create2', methods=['GET'])
def create2():
    team = request.args['team']
    year = request.args['year']
    city = request.args['city']
    dati.append({'squadra': [team], 'anno': [year],'città' : [city]})
    df = pd.DataFrame(data=dati)
    print(df)
    return render_template("search_home.html",team = team, year = year,city = city,df=df)


@app.route('/search', methods=['GET'])
def search():

    scelta = request.argsget(dati, type=list())
    if scelta == "squadra":
        team = request.args['team']
        for key, value in df.items():
            if scelta == key:
                df[team] = value
                return render_template("search.html", risposta = [team])
    elif scelta == "città":
        city = request.args['city']
    for key, value in df.items():
            if scelta == value:
                df[city] = key
            return render_template("search.html", risposta = [city])
    else:
        year = request.args['year']
    for key, value in df.items():
            if scelta == value:
                df[year] = key
            return render_template("search.html", risposta = [year])
    return render_template("search.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
