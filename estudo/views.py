from estudo import app, db
from flask import render_template, url_for, request
from estudo.models import Contato

@app.route('/')
def homepage():
    context = {
        'name': 'Eduardo',
        'idade': 30,
        'cidade': 'Caruaru'
    }
    return render_template('index.html',context=context)


@app.route('/new/')
def newpage():
    return render_template('newpage.html')

@app.route('/contato/', methods=['GET','POST'])
def contato():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        print('GET',pesquisa)
        context.update({'pesquisa':pesquisa})
    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        assunto = request.form['subject']
        mensagem = request.form['message']
        
        contato = Contato(
            name=nome,
            email=email,
            subject=assunto,
            message=mensagem
        )
        db.session.add(contato)
        db.session.commit()
        
    return render_template('contato.html',context=context)