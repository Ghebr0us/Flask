#esercizio: realizzare un server web che visualizzi l'ora,e colori lo sfondo in base all'orario: un colore per la mattina, uno per il pomeriggio, uno per la sera e una per la notte.
from flask import Flask, render_template
app = Flask(__name__)

from datetime import datetime

now = datetime.now()
 
@app.route('/', methods=['GET'])
def time():
    return render_template(now.strftime("%H:%M:%S"))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
