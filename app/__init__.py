from flask import Flask, render_template, redirect
from flask_migrate import Migrate
from .config import Config
from .models import db, SmashCharacter
from .forms import SmashCharacterForm
import app.api_routes as api_routes


app= Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app,db)
app.register_blueprint(api_routes.bp)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/character-library")
def library():
    characters = SmashCharacter.query.all()
    return render_template("library.html", characters=characters)


@app.route("/create-character",methods=["GET", "POST"])
def new_character():
    form= SmashCharacterForm()
    data = form.data
    print(form.data)
    if form.validate_on_submit():
        # print(form.data.tier)
        new_character = SmashCharacter()
        form.populate_obj(new_character)
        db.session.add(new_character)
        db.session.commit()
        return redirect("/character-library")
    return render_template("create.html",form=form)

