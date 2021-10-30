from flask import Flask, render_template, request, jsonify
from randomize import htmlRandomize

app = Flask(__name__)

PASSWORD = "test123"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/randomize")
def randomize():
    if(request.method == "GET"):
        return jsonify(htmlRandomize())

    else:
        return "Bad requst.", 400


if __name__ == "__main__":
    app.run()
