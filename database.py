from dotenv import load_dotenv
load_dotenv()


from app import app, db
from app.models import SmashCharacter


with app.app_context():
    db.drop_all()
    db.create_all()

    # id = db.Column(db.Integer,primary_key=True)
    # name = db.Column(db.String(50), nullable=False,unique=True)
    # tier = db.Column(db.String(1),nullable=False,default="F")
    # dash_speed = db.Column(db.String(20))
    # air_speed = db.Column(db.String(20))
    # final_smash=db.Column(db.String(50))
    # image=db.Column(db.String(3000))

    character1 = SmashCharacter(name="Mario", tier="S", dash_speed="Average",air_speed="Average",final_smash="Coin Drop",image="")

    character2 = SmashCharacter(name="Charizard", tier="B", dash_speed="Average",air_speed="Average",final_smash="Triple Finish",image="https://img.rankedboost.com/wp-content/plugins/super-smash-bros-ultimate/assets/character-images-main/Charizard_SSBU.png") 

    character3 = SmashCharacter(name="Link", tier="M", dash_speed="medium", air_speed="slow", final_smash="Sword Spike", image="") 

    character4 = SmashCharacter(name="Pyra", tier="B", dash_speed="slow", air_speed="slow", final_smash="Chain Attack", image="https://ssb.wiki.gallery/images/thumb/e/ec/Pyra_SSBU.png/400px-Pyra_SSBU.png") 

    character5 = SmashCharacter(name="Pikachu", tier="A", dash_speed="fast", air_speed="fast", final_smash="Thunderbolt", image="") 

    character6 = SmashCharacter(name="Kirby", tier="C", dash_speed="average", air_speed="slow", final_smash="Ultra Sword", image="https://img.rankedboost.com/wp-content/plugins/super-smash-bros-ultimate/assets/character-images-main/Kirby_SSBU.png")
    character7 = SmashCharacter(name="Inkling", tier="A", dash_speed="fast",air_speed="fast",final_smash="Killer Wail",image="https://img.rankedboost.com/wp-content/plugins/super-smash-bros-ultimate/assets/character-images-main/Inkling_SSBU.png") 

    db.session.add(character1)
    db.session.add(character2)
    db.session.add(character3)
    db.session.add(character4)
    db.session.add(character5)
    db.session.add(character6)
    db.session.commit()
