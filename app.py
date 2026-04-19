from maple_app.data import *
from maple_app import app
from flask import render_template

@app.route('/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
