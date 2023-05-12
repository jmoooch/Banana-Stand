#Imports applicable modules used in the application
from flask import Flask, render_template, request

#Creates a Flask application object named 'app'
app = Flask(__name__)

#Assocaites the 'index' function to the URL '/' - (root URL)
@app.route('/', methods=['GET', 'POST'])
def index():
    #Checks if the request method is 'POST' request
    if request.method == 'POST':
        #Retrieves the value entered in the text box
        user_input = request.form['user_input']
        #Returns captured data from text box back to user
        return f"You entered: {user_input}"
    return render_template('index.html')

if __name__ == '__main__':
    #Starts Flask application dev server
    app.run()