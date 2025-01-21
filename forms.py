from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Name', 
        validators=[
            DataRequired(message="Име је обавезно"),
            Length(min=2, max=50, message="Име мора имати између 2 и 50 карактера")
        ])
    email = StringField('Email', 
        validators=[
            DataRequired(message="Имејл је обавезан"),
            Email(message="Невалидан имејл формат")
        ])
    phone = StringField('Phone', 
        validators=[
            Length(min=9, max=15, message="Телефонски број мора имати између 9 и 15 цифара")
        ])
    message = TextAreaField('Message', 
        validators=[
            DataRequired(message="Порука је обавезна"),
            Length(min=10, max=500, message="Порука мора имати између 10 и 500 карактера")
        ])
    submit = SubmitField('Пошаљи')
