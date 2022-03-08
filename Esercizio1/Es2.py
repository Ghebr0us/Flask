#realizzare un sito web che permetta la registrazione degli utenti
#l'utente inserisce il nome, username, una password, la conferma della password e il sesso.
#se le informazioni sono corrette, il sito salva le informazioni in una struttura dati 
#PARTE 2
#prevedere la possibilità di fare il login inserendo username e password, se sono corrette, fornire un messaggio di benvenuto diverso a seconda del sesso.

from flask import Flask, render_template, request
app = Flask(__name__)
data = []

@app.route('/', methods=['GET','POST'])
def log0():
    return render_template("register.html")

@app.route('/register', methods=['GET'])
def log1():
    nm = request.args['name']
    us = request.args['username']
    pw = request.args['Password']
    confpw = request.args['ConfPassword']
    sex = request.form.get('Sex')
    if confpw == pw:
        data.append({'name': nm, 'username' : us, 'password' : pw, 'conferma_password' : confpw, 'sesso': sex})
        print(data)
        return render_template("log.html", nm= nm, us = us, pw = pw , confpw=confpw,data= data)
    else:
        return '<h1>Errore</h1>'
    

@app.route('/login', methods=['GET','POST'])
def log2():
    for i in range(len(data)):
        if username == data[i]["us"]:
            return 'a'
    else: 
        return 'b'
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)