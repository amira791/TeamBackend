from market import db, ma, app 



class Annonce(db.Model) :
    id_annonce = db.Column(db.Integer(), primary_key = True)
    categorie = db.Column(db.String(30), nullable = False)
    type_annonce = db.Column(db.String(300), nullable = False, secondary_key = True )
    surface = db.Column(db.Float(), nullable = False)
    description = db.Column(db.String(300), nullable = False)
    prix = db.Column(db.Integer(), nullable = False)
    wilaya = db.Column(db.String(30), nullable = False)
    commune = db.Column(db.String(30), nullable = False)
    adresse = db.Column(db.String(100), nullable = False)
    photo = db.Column(db.String(30), nullable = False)
    #owner_id = db.Column(db.Integer, db.ForeignKey('account.id'),nullable=False)
    #likes = db.relationship('Like', backref='likes_owned_post')
    categorie
    def __init__(self, id_annonce, categorie, type_annonce, surface, description, prix, wilaya, commune, adresse, photo) : 
        self.id_annonce = id_annonce
        self.categorie = categorie
        self.type_annonce = type_annonce
        self.surface = surface
        self.description = description
        self.prix = prix
        self.wilaya = wilaya
        self.commune = commune
        self.adresse = adresse
        self.photo = photo

class AnnonceSchema(ma.Schema) :
    class Meta : 
        fields = ('id_annonce','categorie', 'type_annonce', 'surface', 'description', 'prix', 'wilaya', 'commune', 'adresse')


#with app.app_context() : 
    #  db.drop_all()
    #  db.create_all()
