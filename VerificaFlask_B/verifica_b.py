# Si vuole realizzare un server web che permetta di avere informazioni sulle stazioni radio a Milano. In particolare
# l’utente deve poter:

# 1. Avere un elenco di tutte le stazioni radio che si trovano in un certo quartiere. L’utente sceglie il nome del
# quartiere da un elenco di radiobutton (ordinato in ordine alfabetico) e clicca su un bottone. Il sito risponde con
# l’elenco ordinato in ordine alfabetico delle stazioni radio presenti in quel quartiere

# 2. Avere le stazioni radio presenti in un quartiere. L’utente inserisce il nome del quartiere (anche solo una parte di
# esso), clicca su un bottone e ottiene la mappa del quartiere con un pallino nero sulla posizione delle stazioni
# radio

# 3. Avere il numero di stazioni per ogni municipio (in ordine crescente sul numero del municipio) e il grafico
# corrispondente

# Per richiamare i vari servizi del sito web, l’utente deve selezionare nella homepage il link corrispondente al servizio
# richiesto.

# Scrivere nella prima facciata del foglio protocollo il server flask, nella seconda i file html relativi alla home page e al
# primo esercizio, nella terza facciata i file html relativi al secondo esercizio e nella quarta facciata i file html relativi al
# terzo esercizio.

from flask import Flask, render_template, send_file, make_response, url_for, Response, request, redirect
app = Flask(__name__)
import pandas as pd

import io
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

stazioni = pd.read_csv("/workspace/Flask/VerificaFlask_B/static/coordfix_ripetitori_radiofonici_milano_160120_loc_final (1).csv" , sep=";")
stazionigeo = gpd.read_file('/workspace/Flask/VerificaFlask_B/static/ds710_coordfix_ripetitori_radiofonici_milano_160120_loc_final.geojson')
quartieri = gpd.read_file('/workspace/Flask/VerificaFlask_B/static/ds964_nil_wm (8)/NIL_WM.dbf')

@app.route('/', methods=['GET'])
def Home():
    return render_template("home.html")

@app.route('/home_es1', methods=['GET'])
def Home1():
  
    return render_template("home_es1.html", quartieri = quartieri.NIL)

@app.route('/elenco', methods=['GET'])
def elenco():
    global quartiere,stazioniQuartiere
    quartieri_req = request.args['radiobutton']
    quartiere = quartieri[quartieri.NIL.str.contains(quartieri_req)]
    stazioniQuartiere = stazionigeo[stazionigeo.intersects(quartiere.geometry.squeeze())].sort_values(by = 'OPERATORE', ascending = True)
    
    return render_template("elenco.html", tabella = stazioniQuartiere.to_html())

#_________________________________________________________________________________________________________________________________________________


#_________________________________________________________________________________________________________________________________________________
    

@app.route('/home_es2', methods=['GET'])
def Home2():
  
    return render_template("home_es2.html", quartieri = quartieri.NIL)
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)



@app.route('/elenco', methods=['GET'])
def elenco():
    global quartiere,stazioniQuartiere
    quartieri_req = request.args['quartiere']
    quartiere = quartieri[quartieri.NIL.str.contains(quartieri_req)]
    stazioniQuartiere = stazionigeo[stazionigeo.intersects(quartiere.geometry.squeeze())].sort_values(by = 'OPERATORE', ascending = True)
    return render_template("in.html", quartieri = quartieri.NIL)
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)