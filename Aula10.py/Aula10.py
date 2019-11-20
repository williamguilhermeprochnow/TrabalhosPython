# Aula 10 - 20-11-2019
# 
#--- Web - Calculadora

nome_pagina= 'Calculadora'
from flask import Flask, render_template, request
from operacoes import *


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',titulo=nome_pagina)
    
@app.route('/calcular')
def calcular():
    n1 = int(request.args['numero1'])
    n2 = int(request.args['numero2'])
    soma1 = soma(n1,n2)
    subtracao1 = subtracao(n1,n2)
    multiplicacao1 = multiplicacao(n1,n2)
    divisao1 = divisaoi(n1,n2)
    divisao_fracionada1 = divisaof(n1,n2)
    resto_divisao1 = restod(n1,n2)
    raiz1 = raiz(n1,n2)
    resultados1 = {'soma':soma1,
                   'subtracao':subtracao1, 
                   'multiplicacao': divisao1, 
                   'divisaoi': divisao1, 
                   'divisaof':divisao_fracionada1, 
                   'restod':resto_divisao1, 
                   'raiz':raiz1 }


    return render_template(
        'resultado.html',
        n1=n1, 
        n2=n2, 
        resultados = resultados1
        )

app.run()

