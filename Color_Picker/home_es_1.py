# Esercizio 1 - Color Picker

#Creare un sito web che:
#- Permetta all'utente di inserire un colore in esadecimae (HEX)
#- Ritorni all'utente il colore in HSL
#- Ritorni all'utente il colore in RGB
#- Compaia un riquadro con il colore indicato
from flask import Flask, render_template , request
app = Flask(__name__)
@app.route('/', methods=['GET']) 
def hex():
    return render_template("home_style1.html",hex = hex) #questa è la prima fase, mandiamo nella pagina la form con l'input  e bottone.

@app.route('/RGB', methods = ['GET','POST'])
def hex_rgb():
  if request.method == "POST":
    # getting input with name = fname in HTML form
    hexa = request.form.get("hexa").lstrip('#')
    rgb = tuple(int(hexa[i:i+2], 16) for i in (0, 2, 4))
    
#--------------------------------------------------------------
  def rgb_to_hsl(r, g, b):
    r = float(r)
    g = float(g)
    b = float(b)
    high = max(r, g, b)
    low = min(r, g, b)
    h, s, v = ((high + low) / 2,)*3

    if high == low:
      h = 0.0
      s = 0.0
    else:
      d = high - low
      s = d / (2 - high - low) if low > 0.5 else d / (high + low)
      h = {
          r: (g - b) / d + (6 if g < b else 0),
          g: (b - r) / d + 2,
          b: (r - g) / d + 4,
      }[high]
      h /= 6
    return h, s, v
  hsl = rgb_to_hsl(rgb[0],rgb[1],rgb[2])
#----------------------------------------------------

  return render_template('rgb_hsl.html',hex_= hexa, rgb =  rgb, hsl = hsl)# a questo punto siamo riusciti ad inviare a flask un valore inserito tramite html.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)