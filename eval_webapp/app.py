from flask import Flask, render_template, redirect, request
from inputform import InputForm
from evalclient import EvalClient
from os import environ

app = Flask(__name__)
app.config['SECRET_KEY'] = environ['FLASK_SECRETKEY']
eval = EvalClient()

@app.route('/input')
def __slash_input():
    lang = request.args.get('lang', 'py')
    inputform = InputForm()
    inputform.lang.data = lang
    return render_template('input.html', form=inputform)
    
@app.route('/output', methods=["POST"])
def __slash_output():
    inputform = InputForm()
    if inputform.validate_on_submit():
        lang = inputform.lang.data
        src = inputform.src.data
        res = eval(lang, src)
        return render_template('output.html', input=src, output=res, lang=lang)