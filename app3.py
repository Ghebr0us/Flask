from flask import Flask, render_template 
app = Flask(__name__)
from datetime import datetime

mese = datetime.now().month
anno = datetime.now().year
@app.route('/', methods=['GET'])   # / è l'indirizzo
def home():
    return render_template("index3.html")
@app.route('/calendar', methods=['GET'])
def calendario():

    return render_template("calendar.html")

@app.route('/book', methods=['GET'])
def libro():
    import random
    frasi = [{'autore':'Dietrich Bonhoeffer','Frase':'Contro la stupidità non abbiamo difese.'},
    {'autore':'Charlie Chaplin','Frase':'Un giorno senza un sorriso è un giorno perso.'},
    {'autore':'Francesco Bacone','Frase':'Sapere è potere.'},
    {'autore':'Italo Calvino','Frase':'Il divertimento è una cosa seria.'},
    {'autore':'Johann Wolfgang von Goethe','Frase':'Il dubbio cresce con la conoscenza.'},
    {'autore':'Luis Sepùlveda','Frase':'Vola solo chi osa farlo.'},
    {'autore':'Voltaire','Frase':'Chi non ha bisogno di niente non è mai povero.'},
    {'autore':'Ricky Nelson','Frase':'Le lacrime di oggi sono gli arcobaleni di domani.'},
    {'autore':'Steve Jobs','Frase':'Siate affamati, siate folli.'},
    {'autore':'Henry David Thoreau','Frase':'Le cose non cambiano; siamo noi che cambiamo.'},]
    FraseRnd = random.randint(0,8)
    return render_template("book.html", autore = frasi[FraseRnd]['autore'],frase = frasi[FraseRnd]['Frase'])

@app.route('/meteo', methods=['GET'])
def meteorologia():
    import random
    Random = random.randint(0,8)
    if Random <= 2:
        immagine = '/static/images/sole.jpg'
    elif Random <= 4:
        immagine = '/static/images/pioggia.jpg'
    elif Random <= 6:
        immagine = '/static/images/grandine.jpg'
    else:
        immagine ='/static/images/nebbia.jpg'
    return render_template("meteo.html" ,meteo = immagine)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)