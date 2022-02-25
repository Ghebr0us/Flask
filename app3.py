from flask import Flask, render_template 
app = Flask(__name__)
from datetime import datetime
import random

@app.route('/', methods=['GET'])   # / è l'indirizzo
def home():
    return render_template("index3.html")
@app.route('/quantomanca', methods=['GET'])
def calendario():
    fine_scuola = datetime(2022,6,8) - datetime.now()
    return render_template("calendar.html", countdown = fine_scuola.days)

@app.route('/frasicelebri', methods=['GET'])
def libro():
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
    Random = random.randint(0,8)
    if Random <= 2:
        immagine = 'bi bi-brightness-high'
        bg_color = '#fbc531'
    elif Random <= 4:
        immagine = 'bi bi-cloud-drizzle'
        bg_color = '#7f8fa6'
    elif Random <= 6:
        immagine = 'bi bi-snow2'
        bg_color = '#dcdde1'
    else:
        immagine ='bi bi-cloud-fog2'
        bg_color = '#353b48'
    return render_template("meteo.html" , icon=immagine, bg_color=bg_color)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)