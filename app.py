from flask import Flask, render_template, request, jsonify, redirect
from dotenv import load_dotenv

import os
import requests


load_dotenv()
PARK = os.getenv('PARK')

# config the app
app = Flask(__name__)

# ---- ROUTES ----
@app.route('/')
def hello_flask():
    return render_template('home.html')

@app.route('/list')
def list():
    stateCode = request.args.get('stateCode')
    park = PARK
    #print(park)
    r = requests.get(f'https://developer.nps.gov/api/v1/parks?stateCode={stateCode}&sort=&api_key={park}')
    #print(r.json())
    parkList = r.json()
    #return (parkList)
    return render_template('list.html', parkList = parkList)
    
    # return render_template('list.html', stateCode=request.args.get('stateCode', 'I think i missed something'))

@app.route('/park')
def park():
    return 'Details of selected park will be here'

# @app.route('/cats/<name>')
# def cat_name(name):
#     # render template with variable
#     return render_template('cats_name.html', name=name)

# fake_database = [
#     'frist the cat',
#     'snowball',
#     'sylvester'
# ]

# # GET/api -- show from fake db
# @app.route('/api/cats', methods=['GET', 'POST'])
# def cats_api():
#     global fake_database

#     if request.method == 'GET':
#         return jsonify({ 'cats': fake_database })
#     if request.method == 'POST':
#         #get request body, for html form
#         cat = request.form['name']
#         fake_database.append(cat)
#         return redirect('/api/cats')