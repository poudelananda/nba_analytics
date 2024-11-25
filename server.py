from flask import Flask, render_template, url_for, request, jsonify
import json
import pandas as pd
import player_position_scraper

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def homePage():
    df = player_position_scraper.player_pos_extracts()
    names = df['PLAYER_NAME']
    return render_template('homepage.html', names = names)

@app.route('/player-performance', methods = ['POST', 'GET'])
def player_performance():
    return render_template('player-performance.html')

if __name__ == '__main__':
    app.run(debug=True)

