#realizzare un server Web che permetta di conoscere capoluoghi di regione
#l'utente inserisce il nome della regione e il programma restituisce il nome del capoluogo della regione.
#caricare i capoluoghi e le regioni in una opportuna struttura dati

#PARTE 2

# modificare poi l'esercizio soprastante per permettere all'utente di inserire un capoluogo e di avere la regioni in cui si trova.
#l'utente sceglie se avere la regione o il capoluogo selezionando un radio button
from flask import Flask, render_template, request 
app = Flask(__name__)

dizionario = {'Abruzzo':'L\'Aquila', 'Basilicata':'Potenza', 'Calabria':'Catanzaro', 'Campania':'Napoli', 'Emilia-Romagna':'Bologna', 'Friuli-Venezia Giulia':'Trieste', 'Lazio':'Roma', 'Liguria':'Genova', 'Lombardia':'Milano', 'Marche':'Ancona', 'Molise':'Campobasso', 'Piemonte':'Torino', 'Puglia':'Bari', 'Sardegna':'Cagliari', 'Sicilia':'Palermo', 'Toscana':'Firenze', 'Trentino-Alto Adige':'Trento', 'Umbria':'Perugia', 'Valle dAosta':'Aosta', 'Veneto':'Venezia'}

@app.route("/", methods=["GET"])
def home():
    return render_template("regione.html")

@app.route("/data", methods=["GET"])
def data():
    scelta = request.args["Scelta"]
    if scelta == "R":
        regione = request.args["RegCap"]
        for key, value in dizionario.items():
            if regione == key:
                capoluogo = value
                return render_template("risp_reg_cap.html", risposta = capoluogo)
        return "<h1>Errore</h1>"              
    else:
        capoluogo = request.args["RegCap"]
        for key, value in dizionario.items():
            if capoluogo == value:
                regione = key
                return render_template("risp_reg_cap.html", risposta = regione)
        return "<h1>Errore</h1>"


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)