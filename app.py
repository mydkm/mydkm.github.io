from flask import Flask, render_template, jsonify
import csv

app = Flask(__name__)

def read_trinkets_csv():
    """
    Reads the CSV file for remaining trinkets.
    Expected format: a header "remaining" and one row with the count.
    """
    try:
        with open('data/trinkets.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                return int(row['remaining'])
    except Exception as e:
        print("Error reading trinkets.csv:", e)
        return 0

def read_leaderboard_csv():
    """
    Reads the leaderboard CSV file.
    Expected columns: name,trinkets_found.
    Returns a sorted list of dictionaries in descending order of trinkets_found.
    """
    leaderboard = []
    try:
        with open('data/leaderboard.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                leaderboard.append({
                    'name': row['name'],
                    'trinkets_found': int(row['trinkets_found'])
                })
        leaderboard.sort(key=lambda x: x['trinkets_found'], reverse=True)
    except Exception as e:
        print("Error reading leaderboard.csv:", e)
    return leaderboard

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    remaining = read_trinkets_csv()
    leaderboard = read_leaderboard_csv()
    return jsonify({'remaining': remaining, 'leaderboard': leaderboard})

if __name__ == '__main__':
    app.run(debug=True)

