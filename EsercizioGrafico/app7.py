# Realizzare un sito web che permetta di visualizzare i quartieri di Milano e alcune informaizoni. La homepage deve contenere i link alle seguenti pagine

# /visualizza 
# visualizza la mappa di Milano divisa in quartieri

# /ricerca
# permette all'utente di inserire il nome di un quartiere e di avere la mappa del quartiere inserito. Dare un opportuno messaggio di errore se il quartiere non dovesse esistere

# /scelta
# permette all'utente di scegliere il nome del quartiere da un menù a tendina contenente i nomi di tutti i quartieri e di visualizzarlo

# /fontanelle
# permette all'utente di scegliere il nome del quartiere da un menù a tendina contenente i nomi di tutti i quartieri e di visualizzare le fontanelle presenti in quel quartiere. Visualizzare anche l'elenco delle fontanelle con l'indirizzo di ognuna

# Ogni link deve restituire una pagina html contenente un messagigo opportuno e le informazioni richieste.

from flask import Flask, render_template, request,send_file, make_response, url_for, Response
app = Flask(__name__)
import io
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

quartieri = gpd.read_file('/workspace/Flask/EsercizioGrafico/static/ds964_nil_wm (8)')

@app.route('/', methods = ['GET'])
def home():
    
    return render_template('region.html')

#-------------------------------------------------




@app.route('/plot.png', methods=['GET'])
def plot_png():

    fig, ax = plt.subplots(figsize = (12,8))

    quartieri.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor = 'k')
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/visualizza', methods=("POST", "GET"))
def mpl1():
    return render_template('plot.html',
                           PageTitle = "Matplotlib")
#----------------------------------------------------------------------









#---------------------------------------------------------------
@app.route('/texthome', methods = ['GET'])
def home2():
    
    return render_template('home2.html')



@app.route('/plot2.png', methods=['GET'])
def plot2_png():

    fig, ax = plt.subplots(figsize = (12,8))

    imgutente.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/ricerca', methods=("POST", "GET"))
def plot25():
    global imgutente
    quartiere_input = request.args['Quartiere']
    imgutente = quartieri[quartieri['NIL'] == quartiere_input]
    return render_template('plot2.html', PageTitle = "Matplotlib")
#------------------------------------------------------------------





#-----------------------------------------------------------------
@app.route('/texthome2', methods = ['GET'])
def home3():
    
    return render_template('home3.html', quartieri = quartieri['NIL'])



@app.route('/plot3.png', methods=['GET'])
def plot3_png():

    fig, ax = plt.subplots(figsize = (12,8))

    imgutente.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/scelta', methods=("POST", "GET"))
def plot35():   
    global imgutente
    quart_scelto = request.args['quartendina']
    imgutente = quartieri[quartieri['NIL'] == quart_scelto]
    return render_template('plot3.html', PageTitle = "Matplotlib")








#---------------------------------------------------------------------------

@app.route('/fontanelle', methods=("POST", "GET"))
def mpl4():
    quartieri_fontane = 
    return render_template('plot.html',
                           PageTitle = "Matplotlib")








if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)