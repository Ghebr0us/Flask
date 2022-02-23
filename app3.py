from flask import Flask, render_template 
app = Flask(__name__)
from datetime import datetime

mese = datetime.now().month
anno = datetime.now().year
@app.route('/', methods=['GET'])   # / è l'indirizzo
def home():
    return render_template("index3.html")
@app.route('/calendar', methods=['GET'])   # / è l'indirizzo
def calendario():

    return render_template("index3.html")

@app.route('/book', methods=['GET'])   # / è l'indirizzo
def libro():

    return render_template("index3.html")

@app.route('/meteo', methods=['GET'])   # / è l'indirizzo
def meteorologia():
    from random import random
    from random import randint
    Random = random.randint(0,8)
    return render_template("index3.html" ,meteo = Random)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)