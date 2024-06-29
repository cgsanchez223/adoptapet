from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)
db.create_all()

debug = DebugToolbarExtension(app)

@app.route("/")
def pet_list():
    """Lists pets name, photo, availability"""

    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)



@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    """Form for adding pets."""

    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data
        )
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Added new pet: {new_pet.name}")
        return redirect("/")
    
    else:
        return render_template("pet_add_form.html", form=form)
    


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit the pet page"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated")
        return redirect(f"/{pet_id}")
    
    else:
        return render_template("pet_edit_form.html", form=form, pet=pet)
    

