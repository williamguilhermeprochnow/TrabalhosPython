from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicia():
    return rendes_template('inicio.html')
app.run

