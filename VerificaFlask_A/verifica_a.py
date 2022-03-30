from flask import Flask, render_template, request,send_file, make_response, url_for, Response
app = Flask(__name__)
import io
import geopandas as gpd
import pandas as pd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

newradio = pd.read_csv("/workspace/Flask/VerificaFlask_A/static/coordfix_ripetitori_radiofonici_milano_160120_loc_final (1).csv")
quartieri = pd.read_csv('/workspace/Flask/VerificaFlask_A/static/ds964_nil_wm (8)/NIL_WM.dbf')


@app.route('/', methods = ['GET'])
def home():
    
    return render_template('home.html')

#-------------------------------------------------

@app.route('/numero', methods = ['GET'])
def home():
        # numero stazioni per ogni municipio

    risultato = newradio.groupby('MUNICIPIO')['OPERATORE'].count().reset_index()
    return render_template('elenco.html' ,tables = risultato.to_html())
#-------------------------------------------------





#-------------------------------------------------

@app.route('/numero', methods = ['GET'])
def home():


    return render_template('home.html')


#-------------------------------------------------




#-------------------------------------------------

    
@app.route('/numero', methods = ['GET'])
def home():
    
    return render_template('home.html')



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)