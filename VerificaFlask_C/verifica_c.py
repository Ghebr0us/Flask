
# Si vuole realizzare un server web che permetta di avere informazioni sulle stazioni radio a Milano. In particolare,
# l’utente deve poter:

# 2. Avere un elenco di tutte le linee (tram e bus) che passano in un certo quartiere. L’utente inserisce il nome del
# quartiere (anche solo una parte del nome) e il sito risponde con l’elenco ordinato in ordine crescente delle linee
# che passano in quel quartiere
# 3. Avere la mappa della città con il percorso di una linea scelta dall’utente. L’utente sceglie il numero della linea da
# un menù a tendina (le linee devono essere ordinati in ordine crescente), clicca su un bottone e ottiene la mappa
# di Milano con il percorso della linea prescelta
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

# 1. Avere l’elenco delle linee tranviarie e di bus che hanno un percorso la cui lunghezza è compresa tra due valori
# inseriti dall’utente. Ordinare le linee in ordine crescente sul numero della linea.

@app.route('/', methods=['GET'])
def HomeP():
    return render_template("home.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)