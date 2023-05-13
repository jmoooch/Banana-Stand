# Imports applicable modules used in application
from flask import Flask, render_template, request

# Creates a Flask application object named 'app'
app = Flask(__name__)

# Assocaites the 'index' function to URL '/' - (root URL)
@app.route('/', methods=['GET', 'POST'])
def index():
    # Checks if the request method is 'POST' request
    if request.method == 'POST':
        # Retrieves the value entered in text box
        user_input = request.form['user_input']
        # Checks user input and determines if they included $ in their response
        if '$' in user_input or 'money' in user_input: 
            return render_template('reward.html')
        else:
        # Returns failure message to user
            return f"You've made a huge mistake."
    return render_template('index.html')

# Starts dev server for Flask app
if __name__ == '__main__':
    app.run()