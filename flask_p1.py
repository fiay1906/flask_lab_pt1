from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    return render_template('template.html')

# @app.route('/Acronyms')
# def hello2():
#     print("Acronyms")
#     return '<p>Ayala-Arias F. : LASER</p>\n<p>Genevieve M. : AFAIK</p>'