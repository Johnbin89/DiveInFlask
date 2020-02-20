from . import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' %self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' %self.username

class Divespot(db.Model):
    __tablename__ = 'divespots'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    depth = db.Column(db.Integer)
    type = db.Column(db.String(30))
    posLat = db.Column(db.String(30))
    posLng = db.Column(db.String(30))


    def __repr__(self):
        return '<Divespot %r>' %self.name