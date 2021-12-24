from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/go')
def go():
    return render_template('bible-study.html')

@app.route('/market')
def market():
    return render_template('market.html', item_name='Phone')