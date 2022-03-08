#realizzare un sito web che permetta la registrazione degli utenti
#l'utente inserisce il nome, username, una password
#la conferma della password e il sesso.se le informazioni sono corrette, il sito salva le informazioni in una struttura dati 
#PARTE 2
#prevedere la possibilità di fare il login inserendo username e password, se sono corrette, fornire un messaggio di benvenuto diverso a seconda del sesso.

from flask import Flask, render_template, request
app = Flask(__name__)
data = []
@app.route('/logup', methods=['GET', 'POST'])
def log1():
    return render_template("register.html" )


@app.route('/login', methods=['GET'])
def log2():
    nm = request.args['name']
    us = request.args['username']
    pw = request.args['Password']
    confpw = request.args['ConfPassword']
    data.append({name: nm, username : us, password : pw, conferma_password : confpw})
    return render_template("register.html", nm= nm, us = us, pw = pw , confpw=confpw)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)