from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from flask_login import UserMixin
from app import db
from random import shuffle



class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    nationality = db.Column(db.String(45))
    position = db.Column(db.String(45))
    current_club = db.Column(db.String(100), nullable=True)
    previous_club = db.Column(db.String(100), nullable=True)
    goals = db.Column(db.Integer, nullable=True)
    assists = db.Column(db.Integer, nullable=True)
    appearances =db.Column(db.Integer)
    league_titles = db.Column(db.Integer, nullable=True)
    national_titles = db.Column(db.Integer, nullable=True)
    ucl_titles = db.Column(db.Integer, nullable=True)
    nickname = db.Column(db.String(100), nullable=True)

    def get_info_list(self):
        info = [
            f"Narodowość: {self.nationality}",
            f"Pozycja: {self.position}",
            f"Obecny klub: {self.current_club or 'Brak danych'}",
            f"Poprzedni klub: {self.previous_club or 'Brak danych'}",
            f"Bramki: {self.goals if self.goals is not None else 'Brak danych'}",
            f"Asysty: {self.assists if self.assists is not None else 'Brak danych'}",
            f"Występy: {self.appearances}",
            f"Tytuły ligowe: {self.league_titles if self.league_titles is not None else 'Brak danych'}",
            f"Tytuły krajowe: {self.national_titles if self.national_titles is not None else 'Brak danych'}",
            f"Trofea Ligi Mistrzów: {self.ucl_titles if self.ucl_titles is not None else 'Brak danych'}"
        ]
        return info




class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(45), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # zahashowane hasło

