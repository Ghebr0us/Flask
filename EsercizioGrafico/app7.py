# realizzare un sito web che restituisca la mappa dei quartieri di Milano.
#ci deve essere una home page con un link "quartieri di Milano": cliccando su questo link si deve visualizzare la mappa dei quartieri di Milano
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

quartieri = gpd.read_file('https://dati.comune.milano.it/dataset/e8e765fc-d882-40b8-95d8-16ff3d39eb7c/resource/f5a2ea4b-3d9e-458c-a11f-a3815553db18/download/ds964_nil_wm.zip')

@app.route('/', methods = ['GET'])
def search():

    return render_template('region.html')

@app.route('/geoplot', methods=['GET'])
def geoplot_data():

    fig, ax = plt.subplots(figsize = (12,8))

    quartieri.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)