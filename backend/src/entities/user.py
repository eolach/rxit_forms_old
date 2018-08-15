from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from src import db, login
from src import ma


class PrivateUser (UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    authorization_level = db.Column(db.Integer)

    def __repr__(self):
        return '<PrivateUser {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return PrivateUser.query.get(int(id))


class PrivateUserSchema(ma.ModelSchema):
    # id = field_for(Prescriber, 'id', dump_only=True)

    class Meta:
        model = PrivateUser