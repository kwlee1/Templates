from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def process():
    name = request.form['name']
    return render_template('result.html',name = name)
app.run(debug=True)