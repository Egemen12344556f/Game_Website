from flask import Flask, request
import os

app = Flask(__name__)

# Define the directory where you want to save the files
SAVE_DIR = 'saved_forms'

# Check if the directory exists, if not create it
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

@app.route('/')
def index():
    return open('templates/contact.html').read()

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Save data to a file in the specified directory
    file_path = os.path.join(SAVE_DIR, f'{name}.txt')
    with open(file_path, 'w') as file:
        file.write(f'Name: {name}\n')
        file.write(f'Email: {email}\n')
        file.write(f'Message: {message}')

    return open('templates/contactalert.html')

if __name__ == '__main__':
    app.run(debug=True)
