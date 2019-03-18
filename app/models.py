from . import db
from werkzeug.security import generate_password_hash
from datetime import date

class ProfilesDB(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    #__tablename__ = 'profilesDB'

    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50))
    location = db.Column(db.String(255))
    gender = db.Column(db.String(6))
    biography = db.Column(db.String(100))
    created_on = db.Column(db.Date, nullable=False)
    picture = db.Column(db.String(255))
    
    def __init__(self, first_name, last_name, email, location, gender,biography):#, picture):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email#generate_password_hash(password, method='pbkdf2:sha256')
        self.location = location
        self.gender=gender
        self.biography = biography
        self.created_on = date.today()
        #self.picture = picture
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.userid)  # python 2 support
        except NameError:
            return str(self.userid)  # python 3 support

    def __repr__(self):
        return '<ProfilesDB %r>' % (self.first_name)


