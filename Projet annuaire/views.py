from flask import Flask, render_template, request
import sqlite3

conn = sqlite3.connect('baseDonnees.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS NUMEROS(id INT, nom TEXT, prenom TXT, numero INT)")
conn.commit()

cur.close()
conn.close()

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/ajout')
def ajout():
    return render_template("ajout.html")

@app.route('/resultat',methods = ['POST'])
def resultat():
  result = request.form
  n = result['nom']
  p = result['prenom']
  return render_template("resultat.html", nom=n, prenom=p)

app.run(port=5008)