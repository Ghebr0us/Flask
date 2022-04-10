
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


@app.route('/linee', methods=('POST','GET'))
def p():
    Min = min(float(request.args["Val1"]), float(request.args["Val2"]))
    Max = max(float(request.args["Val1"]), float(request.args["Val2"]))
    print(Min)
    print(Max)
     #range_percorsi = percorsi['lung_km'] in (inputmin,inputmax)

    range_percorsi = percorsi[(percorsi["lung_km"] >= Min) & (percorsi["lung_km"] <= Max)].sort_values("lung_km")
    return  render_template("tabella.html", tabella = range_percorsi.to_html() )

#________________________________________________________________________

# 2. Avere un elenco di tutte le linee (tram e bus) che passano in un certo quartiere. L’utente inserisce il nome del
# quartiere (anche solo una parte del nome) e il sito risponde con l’elenco ordinato in ordine crescente delle linee
# che passano in quel quartiere

#________________________________________________________________________
@app.route('/quartiere_input', methods=['GET'])
def q_input():
    return render_template("quartiere_input.html")




@app.route('/quartiere', methods=['GET'])
def elenco():
    global quartiere,stazioniQuartiere
    quartieri_req = request.args['quart_input']
    quartiere = quartieri[quartieri.NIL.str.contains(quartieri_req)]
    percorsi_quartiere = percorsi[percorsi.intersects(quartiere.geometry.squeeze())].sort_values(by = 'linea', ascending = True)
    return render_template("tabella.html", tabella = percorsi_quartiere.to_html())

#________________________________________________________________________

# 3. Avere la mappa della città con il percorso di una linea scelta dall’utente. L’utente sceglie il numero della linea da
# un menù a tendina (le linee devono essere ordinati in ordine crescente), clicca su un bottone e ottiene la mappa
# di Milano con il percorso della linea prescelta

#________________________________________________________________________
@app.route('/map_input', methods=['GET'])
def m_input():
    return render_template("dropdown_linee.html", linee = percorsi["linea"].drop_duplicates().sort_values(ascending=True))
    



@app.route("/linea", methods=["GET"])
def linea():
    global lineeUtente
    linea = int(request.args["linea_drop"])
    lineeUtente = percorsi[percorsi["linea"] == linea]
    return render_template("mappa.html", linea = linea)

@app.route("/mappa.png", methods=["GET"])
def mappapng():
    fig, ax = plt.subplots(figsize = (12,8))

    lineeUtente.to_crs(epsg=3857).plot(ax=ax, edgecolor="k")
    quartieri.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor="k")
    contextily.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)