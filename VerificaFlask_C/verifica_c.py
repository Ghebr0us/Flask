
# Si vuole realizzare un server web che permetta di avere informazioni sulle stazioni radio a Milano. In particolare,
# l’utente deve poter:

# Per richiamare i vari servizi del sito web, l’utente deve selezionare nella homepage il radiobutton corrispondente al
# servizio richiesto e cliccare su un bottone.

# Scrivere nella prima facciata del foglio protocollo il server Flask, nella seconda i file html relativi alla home page e al
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

percorsi = gpd.read_file('/workspace/Flask/VerificaFlask_C/static/tpl_percorsi.geojson')
quartieri = gpd.read_file('/workspace/Flask/VerificaFlask_C/static/ds964_nil_wm (8)/NIL_WM.dbf')



percorsi["lung_km"] = percorsi["lung_km"].astype(float)
percorsi["linea"] = percorsi["linea"].astype(int)


#___________________________________________________________________________________________________________________________

# 1. Avere l’elenco delle linee tranviarie e di bus che hanno un percorso la cui lunghezza è compresa tra due valori
# inseriti dall’utente. Ordinare le linee in ordine crescente sul numero della linea.

#___________________________________________________________________________________________________________________________
@app.route('/', methods=['GET'])
def Home():
    return render_template("home.html")

@app.route('/selection', methods=['GET'])
def selection():
    scelta = request.args['scelta']
    if scelta == 'es1':
         return redirect('/percorso_input')
    elif scelta == 'es2':
        return  redirect('/quartiere_input')
    else:
        return redirect('/map_input')


@app.route('/percorso_input', methods=['GET'])
def p_input():
    return render_template("percorso_input.html")


@app.route('/linee', methods=['GET'])
def p():
    inputmin = request.args["min"]
    inputmax = request.args["max"]
    
    range_percorsi = percorsi['lung_km'] in (inputmin,inputmax)
    return  render_template("range_percorsi.html", tabella = range_percorsi.to_html() )







    
#________________________________________________________________________

# 2. Avere un elenco di tutte le linee (tram e bus) che passano in un certo quartiere. L’utente inserisce il nome del
# quartiere (anche solo una parte del nome) e il sito risponde con l’elenco ordinato in ordine crescente delle linee
# che passano in quel quartiere

#________________________________________________________________________
@app.route('/quartiere_input', methods=['GET'])
def q_input():
    return render_template("home.html")
















#________________________________________________________________________

# 3. Avere la mappa della città con il percorso di una linea scelta dall’utente. L’utente sceglie il numero della linea da
# un menù a tendina (le linee devono essere ordinati in ordine crescente), clicca su un bottone e ottiene la mappa
# di Milano con il percorso della linea prescelta

#________________________________________________________________________
@app.route('/map_input', methods=['GET'])
def m_input():
    return render_template("home.html")
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)