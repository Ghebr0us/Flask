#realizzare un server Web che permetta di conoscere capoluoghi di regione
#l'utente inserisce il nome della regione e il programma restituisce il nome del capoluogo della regione.
#caricare i capoluoghi e le regioni in una opportuna struttura dati

#PARTE 2

# modificare poi l'esercizio soprastante per permettere all'utente di inserire un capoluogo e di avere la regioni in cui si trova.
#l'utente sceglie se avere la regione o il capoluogo selezionando un radio button
from flask import Flask, render_template, request
app = Flask(__name__)
lista = []
lista.append({'Valle Aosta' : "Aosta", "Piemonte" : "Torino", "Liguria" : "Genova", "Lombardia" : "Milano", "Trentino-Alto Adige" : "Trento", "Veneto" : "Venezia", "Friuli-Venezia Giulia" : "Trieste", "Emilia-Romagna" : "Bologna","Toscana" : "Firenze","Marche" : "Ancona","Lazio" : "Roma","Umbria" : "Perugia","Abruzzo" : "L'Aquila","Molise" : "Campobasso","Campania" : "Napoli","Puglia" : "Bari","Basilicata" : "Potenza","Calabria" : "Catanzaro","Sicilia" :"Palermo","Sardegna" : "Cagliari"})
@app.route('/', methods=['GET'])
def hello_world():
    return render_template("regione.html")


@app.route('/data', methods=['GET'])
def Data():
    print(request.args)
    name = request.args['name']
    regCap = request.args['regCap']
    

@app.route("/Risposta", methods=["GET"])
def Risposta():
    ris = request.args['ris']
    for utente in lista:
        if utente[]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)