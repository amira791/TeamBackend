from market import db, ma, app, login_manager
import sqlalchemy.types as types
import enum
from market import bcrypt
from flask_login import UserMixin
from sqlalchemy import Integer, Enum
from werkzeug.security import generate_password_hash, check_password_hash


class Annonce(db.Model) :
    __tablename__ = 'annonces'
    id_annonce = db.Column(db.Integer(), primary_key = True)
    categorie = db.Column(db.String(30), nullable = False)
    categories = db.Column(Enum('vente', 'echange', 'location', 'location pour vacance', name='categorie_annonce'))
    type =  db.Column(Enum('terrain', 'terrain agricole', 'appartement', 'maison', 'bungalow', name='type_annonce'))
    description = db.Column(db.String(300), nullable = False)
    prix = db.Column(db.Integer(), nullable = False)
    wilaya = db.Column(db.String(30), nullable = False)
    commune = db.Column(db.String(30), nullable = False)
    adresse = db.Column(db.String(100), nullable = False)
    photo = db.Column(db.String(30), nullable = False)
    #owner_id = db.Column(db.Integer, db.ForeignKey('account.id'),nullable=False)
    #likes = db.relationship('Like', backref='likes_owned_post')
    owner_id = db.Column(db.Integer(),db.ForeignKey('users.id')) 
    def __init__(self, id_annonce, categorie, type, surface, description, prix, wilaya, commune, adresse, photo) : 
        self.id_annonce = id_annonce
        self.categorie = categorie
        self.type = type
        self.surface = surface
        self.description = description
        self.prix = prix
        self.wilaya = wilaya
        self.commune = commune
        self.adresse = adresse
        self.photo = photo

class AnnonceSchema(ma.Schema) :
    class Meta : 
        fields = ('id_annonce','categorie', 'type', 'surface', 'description', 'prix', 'wilaya', 'commune', 'adresse')

class User(db.Model):
    __tablename__ = 'users'
    serialize_only=()
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True )
    fullname = db.Column(db.String, unique=True, nullable=False )
    email = db.Column(db.String,nullable=False,unique=True)
    address = db.Column(sb.String, nullable = False)
    password = db.Column(db.String)
    profile_pic = db.Column(db.String(30), nullable = False)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
    def __init__(self, id_, username, fullname, email, address, password, profile_pic):
        self.id = id_
        self.username = username
        self.fullname = fullname
        self.email = email
        self.address= address
        self.password = password
        self.profile_pic = profile_pic


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ('id', 'username', 'fullname', 'email', 'address', 'password', 'profile_pic')
        include_relationships = True

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    annonce_id = db.Column(db.Integer, db.ForeignKey('annonces.id'))

annonce_user = db.Table('annonce_user',
                    db.Column('annonce_id', db.Integer, db.ForeignKey('annonces.id')),
                    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
                    )
messages_user = db.Table('comments_user',
                    db.Column('annonce_id', db.Integer, db.ForeignKey('annonces.id')),
                    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                    db.Column('comment_id', db.Integer, db.ForeignKey('comments.id'))
                    )