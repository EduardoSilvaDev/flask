from estudo import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    context = {
        'name': 'Eduardo',
        'idade': 30,
        'cidade': 'São Paulo'
    }
    return render_template('index.html',context=context)


@app.route('/new/')
def newpage():
    return render_template('newpage.html')