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
    df = pd.read_csv("/workspace/Flask/EsercizioSquadre/templates/dati.csv")
    df.append({'squadra': team, 'anno': year,'città' : city}, ignore_index=True)   
    df.to_csv("/workspace/Flask/EsercizioSquadre/templates/dati.csv")
    
    return render_template("search_home.html",team = team, year = year,city = city,df=df)


@app.route('/search', methods=['GET'])
def search():
    indice = request.args.get('ricerca')
    informazione = request.args.get("info")
    print(indice, informazione)
    scelta = dati[dati[informazione] == indice]
    return render_template('search.html', tables=[scelta.to_html()], titles=[''])

    return 'errore'
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
