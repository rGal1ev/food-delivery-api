from app import db
from werkzeug.security import check_password_hash, generate_password_hash

class Employees(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, unique=True)
    firstname = db.Column("firstname", db.String, nullable=False)
    lastname = db.Column("lastname", db.String, nullable=True)

    phone = db.Column("phone", db.String, nullable=False)
    email = db.Column("email", db.String, nullable=True)

    login = db.Column("login", db.String, nullable=False)
    password = db.Column("password", db.String, nullable=False)

    def __init__(self, firstname, phone, login, password, lastname=None, email=None):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.login = login
        self.password = generate_password_hash(password)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "phone": self.phone,
            "email": self.email,
            "login": self.login,
            "password": self.password
        }

    def check_password(self, password):
        return check_password_hash(self.password, password)