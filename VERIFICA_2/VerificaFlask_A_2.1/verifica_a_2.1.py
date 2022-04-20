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
ripartizioni = pd.read_csv('/workspace/Flask/VERIFICA_2/VerificaFlask_A_2.1/static/georef-italy-ripartizione-geografica.csv', sep=";")

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
    prov['area'] = prov.geometry.area
    print(prov)
    print(com_prov)
    print(provincie)
    return render_template("risultato.html")

@app.route('/mappa', methods=['GET'])
def mappa():

    fig, ax = plt.subplots(figsize = (12,8))

    prov.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    com_prov.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

    return render_template("home1.html")



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)