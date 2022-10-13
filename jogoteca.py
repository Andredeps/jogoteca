from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return render_template('lista.html')

app.run()