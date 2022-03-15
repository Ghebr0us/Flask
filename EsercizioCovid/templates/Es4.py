#si vuole realizzare un sito web che permetta di visualizzare alcune informazioni sull'andamento dell'epidemia di Covid nel nostro paese, a partire da i dati presenti nel file
#l'utente sceglie la regione da un elenco(menù a tendina), clicca su un bottone e il sito deve visualizzare una tabella contente le informazioni relative a quella regione.
#i dati da inserire nel menù a tendina devono essere caricati automanticamente dalla pagina.
from flask import Flask, render_template, request 
app = Flask(__name__)
import pandas as pd  #installare prima pandas
daticovid = pd.read_csv('https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-dose-addizionale-booster.csv')
@app.route("/", methods=["GET"])
def home():
    return render_template("home19_automatic.html")


@app.route("/dati", methods=["GET"])
def data():
  nomeregione = request.args['regioni']
  risultato = daticovid[daticovid['nome_area'] == nomeregione]
  return render_template('covid.html', tables=[risultato.to_html()], titles=[''])
           

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)