from flask import request, render_template

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



