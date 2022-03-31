
from flask import Flask, render_template, send_file, make_response, url_for, Response, request
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


    


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)