
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
    
    return render_template('home.html')

@app.route('/plot.png', methods=['GET'])
def plot_png():

    fig, ax = plt.subplots(figsize = (12,8))

    imgutente.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/plot', methods=("POST", "GET"))
def mpl():
    global imgutente
    quartiere_input = request.args['Quartiere']
    imgutente = quartieri[quartieri['NIL'] == quartiere_input]
    return render_template('plot.html', PageTitle = "Matplotlib")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)