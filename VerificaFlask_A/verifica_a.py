
# 1. Avere il numero di stazioni per ogni municipio (in ordine crescente sul numero del municipio) e il grafico
# corrispondente

# 2. Avere un elenco di tutte le stazioni radio che si trovano in un certo quartiere. L’utente inserisce il nome del
# quartiere (anche solo una parte del nome) e il sito risponde con l’elenco ordinato in ordine alfabetico delle
# stazioni radio presenti in quel quartiere

# 3. Avere la posizione in città di una stazione radio. L’utente sceglie il nome della stazione da un menù a tendina (i
# nomi delle stazioni devono essere ordinati in ordine alfabetico), clicca su un bottone e ottiene la mappa del
# quartiere che contiene la stazione radio, con un pallino nero sulla posizione della stazione radio

# Per richiamare i vari servizi del sito web, l’utente deve selezionare nella homepage il radiobutton corrispondente al
# servizio richiesto e cliccare su un bottone.

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

stazioni = pd.read_csv("/workspace/Flask/VerificaFlask_A/static/coordfix_ripetitori_radiofonici_milano_160120_loc_final (1).csv" , sep=";")
stazionigeo = gpd.read_file('/workspace/Flask/VerificaFlask_A/static/ds710_coordfix_ripetitori_radiofonici_milano_160120_loc_final.geojson')
quartieri = gpd.read_file('/workspace/Flask/VerificaFlask_A/static/ds964_nil_wm (8)/NIL_WM.dbf')

@app.route('/', methods=['GET'])
def HomeP():
    return render_template("home1.html")



@app.route('/selection', methods=['GET'])
def Home2():
    scelta = request.args['scelta']
    if scelta == 'es1':
         return redirect('/numero')
    elif scelta == 'es2':
        return  redirect('/input')
    else:
        return redirect('/dropdown')




@app.route('/numero', methods=['GET'])
def numero():
    global risultato
    # numero di stazione per ogni municipio
    risultato = stazioni.groupby(stazioni.MUNICIPIO, as_index = False).count().filter(items=["MUNICIPIO", "BOUQUET"]).sort_values(by="BOUQUET", ascending = True)
    return render_template("elenco.html", tabella = risultato.to_html())


@app.route('/grafico', methods=['GET'])
def numero2():
    # costruzione del grafico; 
    fig, ax = plt.subplots(figsize = (6,4))

    x = risultato.MUNICIPIO
    y = risultato.BOUQUET

    ax.bar(x, y, color = "#304C89")

    plt.xticks(rotation = 30, size = 5)
    plt.ylabel("Expected Clean Sheets", size = 5)
    # visualizzazione del grafico; 
    output = io.BytesIO()
    #stampa l'immagine sul canale della comunicazione 
    FigureCanvas(fig).print_png(output)
    #,amda òa risposta quello che c'è nell'output
    return Response(output.getvalue(), mimetype='image/png')



@app.route('/numero', methods=['GET'])
def numero4():
    global risultato
    # numero di stazione per ogni municipio
    risultato = stazioni.groupby(stazioni.MUNICIPIO, as_index = False).count().filter(items=["MUNICIPIO", "BOUQUET"]).sort_values(by="BOUQUET", ascending = True)
    return render_template("elenco.html", tabella = risultato.to_html())


@app.route("/input", methods=["GET"])
def input():
    
    return render_template('input.html')

@app.route("/ricerca", methods=["GET"])
def ricerca():
    global quartiere, stazioniQuartiere
    nomeQuar = request.args['quartiere']
    quartiere = quartieri[quartieri.NIL.str.contains(nomeQuar)]
    stazioniQuartiere = stazionigeo[stazionigeo.intersects(quartiere.geometry.squeeze())]
    print(quartiere)
    print(stazionigeo)
    return render_template('elenco1.html',tabella = stazioniQuartiere.to_html())







@app.route('/mappa.png', methods=['GET'])
def plot4_png():

    fig, ax = plt.subplots(figsize = (12,8))
    quartiere.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor = 'r')
    stazioniQuartiere.to_crs(epsg=3857).plot(ax=ax, alpha=0.5 , color = 'r')
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


#_________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________


@app.route('/dropdown', methods = ['GET'])
def home4():
    #trasformare in una lista la colonna 'OPERATORE'
    nomi_stazioni = stazioni.OPERATORE.to_list()
    #eliminiamo i duplicati con set, dato che non prevede duplicati
    nomi_stazioni = list(set(nomi_stazioni))
    nomi_stazioni.sort()
    return render_template('dropdown.html', stazioni = nomi_stazioni)




@app.route('/mappa2.png', methods=['GET'])
def mappa2():

    fig, ax = plt.subplots(figsize = (12,8))

    stazione_utente.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    quartiere1.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')






@app.route('/scelta_stazione', methods = ['GET'])
def station():
    global quartiere1, stazione_utente
    scelta_stazione = request.args['stazione']
    stazione_utente = stazionigeo[stazionigeo.OPERATORE == scelta_stazione]
    quartiere1 = quartieri[quartieri.contains(stazione_utente.geometry.squeeze())]
    return render_template('lista_stazione.html',quartiere1 = quartiere1)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)