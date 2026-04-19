from maple_app.data import *
from maple_app import app
from flask import render_template, request

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        api_key = request.form.get('api_key')
        api_key_check(api_key)
        pass
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
