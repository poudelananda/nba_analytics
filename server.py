from flask import Flask, render_template, url_for, request, jsonify
import json
import pandas as pd
import player_position_scraper
import nba_analytics

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def homePage():
    df = player_position_scraper.player_pos_extracts()
    names = df['PLAYER_NAME']
    return render_template('homepage.html', names = names)

@app.route('/player-data', methods = ['POST', 'GET'])
def player_data():
    player_name = request.form.get("player-names")
    # inner_html = data.get('innerHTML')
    # player_name_json = jsonify(inner_html)
    # return render_template('player-performance.html', player_name = inner_html)
    player_df = nba_analytics.player_stats(player_name)
    player_df_json = player_df[['PTS', 'AST', 'REB']].describe().to_json()
    return player_df_json


@app.route('/player-performance', methods = ['POST', 'GET'])
def player_performance():
    player_data = player_data()
    return render_template('player-performance.html', data = player_data)

if __name__ == '__main__':
    app.run(debug=True)

