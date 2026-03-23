from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from werkzeug.security import check_password_hash
from app import app, db
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired(), Length(min=3, max=45)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Hasło', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Potwierdź hasło', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Zarejestruj się')

    def validate_username(self, username):
        existing_user = User.query.filter_by(    
        username = username.data).first()
        if existing_user:
            raise ValidationError(
                "That username already exists. Please choose a different one."
            )

    def validate_email(self, email):
        existing_user = User.query.filter_by(    
        email = email.data).first()
        if existing_user:
            raise ValidationError(
                "That Email already exists. Please choose a different one."
            )


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Hasło', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Zaloguj się')

    

    def validate_email(self, email):
        existing_user = User.query.filter_by(    
        email = email.data).first()
        if existing_user is None:
            raise ValidationError(
                "Nie istnieje użytkownik o takim Emailu"
            )
        

    def validate_password(self, password):
        user = User.query.filter_by(email=self.email.data).first()
        
        if user and not check_password_hash(user.password, password.data):
            raise ValidationError("Podano nieprawidłowe hasło")
