from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class SmashCharacter(db.Model):
    __tablename__="smash_characters"
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50), nullable=False,unique=True)
    tier = db.Column(db.String(1),nullable=False,default="F")
    dash_speed = db.Column(db.String(20))
    air_speed = db.Column(db.String(20))
    final_smash=db.Column(db.String(50))
    image=db.Column(db.String(3000))
