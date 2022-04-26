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


comuni = gpd.read_file('/workspace/Flask/VERIFICA_2/VerificaFlask_A_2.1/static/Com01012021_g')
provincie = gpd.read_file('/workspace/Flask/VERIFICA_2/VerificaFlask_A_2.1/static/ProvCM01012021_g')
regioni = gpd.read_file('/workspace/Flask/VERIFICA_2/VerificaFlask_A_2.1/static/Reg01012021_g')
ripartizioni = gpd.read_file('VERIFICA_2/VerificaFlask_A_2.1/static/RipGeo01012021_g-20220426T170822Z-001')


#______________________________________________________________________________________________________________________________


# 1. inserire il nome di una provincia, cliccare su un bottone ed ottenere le seguenti informazioni:

# a. mappa geografica con i confini della provincia (confini neri) con l’indicazione al suo interno dei comuni
# che la compongono (confini rossi)

# b. area della provincia (espressa in km 2 )


#______________________________________________________________________________________________________________________________

@app.route('/', methods=['GET'])
def Home():
    return render_template("home.html")

@app.route('/h1', methods=['GET'])
def h1():
    return render_template("home1.html")


@app.route('/es1', methods=['GET'])
def es1():
    
    global com_prov, prov,prov_input,area
    prov_input = request.args['provincia']

    prov = provincie[provincie['DEN_PROV'] == prov_input]
    com_prov = comuni[comuni.within(prov.geometry.squeeze())]
    area = prov.geometry.area/10**6
    print(prov)
    print(com_prov)
    print(provincie)
    print(comuni)
    print(regioni)
    print(ripartizioni)
    print(area)
    return render_template("risultato.html",area=area)

@app.route('/mappa', methods=['GET'])
def mappa():

    fig, ax = plt.subplots(figsize = (12,8))

    prov.to_crs(epsg=3857).plot(ax=ax, edgecolor="k",linewidth=1)
    com_prov.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor="r")
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

    return render_template("home1.html")

#______________________________________________________________________________________________________________________________

# 2. scegliere il nome della provincia da una serie di menù a tendina ed avere le stesse informazioni dell’esercizio
# precedente. Per scegliere la provincia, l’utente sceglie prima la regione (in cui si trova la provincia) da un menù a
# tendina, la seleziona, clicca su un bottone e ottiene l’elenco delle province di quella regione, sempre in un menù
# a tendina.

#  A questo punto sceglie la provincia dal menù a tendina, clicca su un bottone e ottiene le informazioni.
# Tutti gli elenchi devono essere ordinati in ordine alfabetico. Ottimizzare il lavoro in modo da poter riutilizzare il
# codice dell’esercizio 1



#______________________________________________________________________________________________________________________________
@app.route('/h2', methods=['GET'])
def h2():
    return render_template("home2.html",regioni = regioni.DEN_REG.sort_values(ascending=True))

@app.route('/h2.5', methods=['GET'])
def h2_5():
    global reg_input, prov_reg,area
    reg_input = request.args['dropreg']
    print(reg_input)
    reg = regioni[regioni['DEN_REG'] == reg_input]
    prov_reg =provincie[provincie.within(reg.geometry.squeeze())]
    return render_template("home2_5.html", prov_reg = prov_reg, regioni = reg, provincie = prov_reg.DEN_PROV.sort_values(ascending=True))


#______________________________________________________________________________________________________________________________

# 3. come l’esercizio precedente ma l’utente sceglie a partire dalla ripartizione geografica (che contiene la regione
# che contiene a sua volta la provincia). Usare sempre menù a tendina e ordinare sempre gli elenchi in ordine
# alfabetico. 

# Ottimizzare il lavoro in modo da poter riutilizzare il codice dell’esercizio 2


#______________________________________________________________________________________________________________________________

@app.route('/h3', methods=['GET'])
def h3():
    return render_template("home3.html",ripartizioni = ripartizioni.Ripartizione_geografica.sort_values(ascending=True))

@app.route('/h2.5', methods=['GET'])
def h3_5():
    global reg_input, prov_reg,area
    reg_input = request.args['dropreg']
    print(reg_input)
    reg = regioni[regioni['DEN_REG'] == reg_input]
    prov_reg =provincie[provincie.within(reg.geometry.squeeze())]
    return render_template("home2_5.html", prov_reg = prov_reg, regioni = reg, provincie = prov_reg.DEN_PROV.sort_values(ascending=True))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)