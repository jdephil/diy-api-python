from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flasql'
db = SQLAlchemy(app)

class Jellybean(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  flavor = db.Column(db.String, unique=True, nullable=False)
  color = db.Column(db.String, nullable=False)
  description = db.Column(db.String)

  def __repr__(self):
    return f'Jellybean(id={self.id}, flavor="{self.flavor}", color="{self.color}", description="{self.description}")'