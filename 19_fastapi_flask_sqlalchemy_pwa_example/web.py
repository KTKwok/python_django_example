from flask import Flask, render_template, request
from database import SessionLocal
from models import User

flask_app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static'
)
flask_app.config["TEMPLATES_AUTO_RELOAD"]=True

@flask_app.route('/')
def index():
    name = request.args.get('name', 'Visitor')
    db = SessionLocal()

    try:
        user_count = db.query(User).count()
        users = db.query(User).all()
    finally:
        db.close()

    return render_template('index.html', users=users, name=name, user_count=user_count)