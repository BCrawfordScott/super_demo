from flask import Blueprint, request
from .models import SmashCharacter

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/characters")
def get_characters():
    characters = SmashCharacter.query.all()
    data = [{
        "id": char.id, 
        "name": char.name,
        "tier": char.tier,
        "dash_speed": char.dash_speed,
        "air_speed":char.air_speed,
        "final_smash": char.final_smash,
        "image": char.image
    } for char in characters]
    return { "data": data }

@bp.route("/characters", methods=["POST"])
def create_character():
    data = request.json
    new_character = SmashCharacter(**data)
    db.session(add(new_character))
    db.session.commit()
    return {
        "id": new_character.id, 
        "name": new_character.name,
        "tier": new_character.tier,
        "dash_speed": new_character.dash_speed,
        "air_speed":new_character.air_speed,
        "final_smash": new_character.final_smash,
        "image": new_character.image
    }
