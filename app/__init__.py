from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'tajny_klucz'  # do formularzy/logowania
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///footballers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Można wyłączyć, jeśli nie chcesz śledzić zmian w bazie danych

db = SQLAlchemy(app)
login_manager = LoginManager(app)


from app import routes
