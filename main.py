import os
from flask import Flask, redirect, render_template, request, send_from_directory
import sys
from datetime import date
import json

app = Flask(__name__)

pesos = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("pesos.html")

@app.route("/datos/<float:id>")
def datos(id):
    
    pesos.pop(0)
    pesos.append(round(id, 2))
    #print(pesos)
    return ' '

@app.route("/data")
def data():
   # print(pesos)
    return json.dumps(pesos)

