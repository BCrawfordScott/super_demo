from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField
from wtforms.validators import DataRequired


letter_grade= ["A","B","C","D","E"]
values = [(el, el+"-tier") for el in letter_grade]

class SmashCharacterForm(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    tier=SelectField("Tier", choices=values)
    dash_speed=StringField("Dash Speed")
    air_speed=StringField("Air Speed")
    final_smash=StringField("Final Smash")
    image=StringField("Image")
    submit=SubmitField("Submit")