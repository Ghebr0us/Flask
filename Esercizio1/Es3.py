#realizzare un server Web che permetta di conoscere capoluoghi di regione
#l'utente inserisce il nome della regione e il programma restituisce il nome del capoluogo della regione.
#caricare i capoluoghi e le regioni in una opportuna struttura dati

#PARTE 2

# modificare poi l'esercizio soprastante per permettere all'utente di inserire un capoluogo e di avere la regioni in cui si trova.
#l'utente sceglie se avere la regione o il capoluogo selezionando un radio button
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def Reg_Cap():
    
    return render_template("regione.html")


@app.route('/Reg', methods=['GET'])
def Data():
    name = request.args['name']
    regCap = request.args['regCap']

capoluoghiRegione = {'Abruzzo':' L Aquila','Basilicata':'Potenza','Calabria':'Catanzaro','Campania':'Napoli','Emilia-Romagna':'Bologna','Friuli-Venezia Giulia':'Trieste','Lazio':'Roma','Liguria':'Genova','Lombardia':'Milano','Marche':'Ancona','Molise':'Campobasso','Piemonte':'	Torino','Puglia':'	Bari','Sardegna':'Cagliari','Sicilia':'	Palermo','Toscana':'Firenze','Trentino-Alto Adige':'Trento','Umbria':'Perugia','Valle d Aosta':'Aosta','Veneto':'Venezia',}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)