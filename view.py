from flask import Flask, render_template, request, redirect
import os
#from login import authentication

app = Flask(__name__)


@app.route('/')

@app.route('/login')
def login():
    if request.method == 'POST':
        username = request.form.get('UserName')
        password = request.form.get('Password')
        #ans = authentication(username, password)
    return render_template('login.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4000))
    app.run(debug=True, host='0.0.0.0', port=port)