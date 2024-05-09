from flask import Flask
from flask import request, redirect, url_for, render_template
#from flask_login import login_required
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

#create app
app = Flask(__name__, template_folder='templates')
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./testproject5.db"
db.init_app(app)
#db = SQLAlchemy(app)

#define the routes
import routes

# See important note below
from models import Profile, User

with app.app_context():
    db.create_all()
    db.session.add(User('admin', 'admin@example.com'))
    db.session.add(User('guest', 'guest@example.com'))
    db.session.commit()
    
    users = User.query.all()
    print(users)
    userss = db.session.execute(db.select(User).order_by(User.username))
    print(userss)
  


if __name__ == '__main__':
    app.run()


