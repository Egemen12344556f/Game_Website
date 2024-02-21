from flask import Flask, render_template, request

app = Flask(__name__)

def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Write form data to a file
    with open('form_data.txt', 'a') as file:
        file.write(f'Name: {name}\n')
        file.write(f'Email: {email}\n')
        file.write(f'Message: {message}\n')
        file.write('\n')  # Add a new line to separate entries
        
    # Return a response indicating successful form submission
    return render_template('contactalert.html')

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
