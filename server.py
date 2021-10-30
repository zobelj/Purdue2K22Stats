from flask import Flask, render_template, request, jsonify
from randomize import htmlRandomize, htmlUploadScores
from sqlalchemy import create_engine
from sqlalchemy.sql import text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')

@app.route('/data')
def data():
    with open('db_url.txt', 'r') as f:
        db_url = f.read()
        my_conn = create_engine(db_url)
    
    with my_conn.connect() as conn:
        file = open("./sql_scripts/create_html_table.sql")
        query = text(file.read())
        rows = conn.execute(query)
        data = rows.fetchall()
        print(data)
        
    return render_template('data.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/randomize", methods=['GET', 'POST'])
def randomize():
    if(request.method == "GET"):
        return jsonify(htmlRandomize())

    elif(request.method == "POST"):
        return "Bad request!", 400

@app.route("/upload", methods=['GET', 'POST'])
def uploadScores():
    if(request.method == "GET"):
        return "Bad request!", 400

    elif(request.method == "POST"):
        return htmlUploadScores(request.json)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    # local ip is 10.41.0.51:8080
