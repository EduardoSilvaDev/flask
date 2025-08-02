from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

from estudo import db
from estudo.models import Contato

class ContatoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    assunto = StringField('Assunto', validators=[DataRequired()])
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    
    btnSubmit = SubmitField('Enviar')
    
    def save(self):
        contato = Contato(
            name = self.nome.data,
            email = self.email.data,
            subject = self.assunto.data,
            message = self.mensagem.data
        )
        
        db.session.add(contato)
        db.session.commit()
        
    