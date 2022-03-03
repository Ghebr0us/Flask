# Esercizio 1 - Color Picker

#Creare un sito web che:
#- Permetta all'utente di inserire un colore in esadecimae (HEX)
#- Ritorni all'utente il colore in HSL
#- Ritorni all'utente il colore in RGB
#- Compaia un riquadro con il colore indicato
from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/', methods=['GET']) 
def hex():
    return render_template("home_style1.html",hex = hex)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)