from app.models.User import User
from app import db

def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()

def get_all_user():
    users = User.query.all()
    return users


def save_user(user):

    db.session.add(user)
    db.session.commit()

def edit_user_details(user_id, name, email):
    user = User.query.filter_by(id=user_id).first()
    user.name = name
    user.email = email

    db.session.commit()

def delete_user_details(user_id):
    user = User.query.filter_by(id=user_id).first()

    db.session.delete(user)
    db.session.commit()

