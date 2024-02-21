from flask import Flask, render_template
from main import submit



app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/contact')
def contact():
    submit()
    return render_template('contactalert.html')



if __name__ == "__main__":
    app.run(debug=True)