from flask import Flask, request, render_template,  redirect, flash, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///employees_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():
    """Render home page with pets"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Send data when adding pet and adding to db"""
    form = AddPetForm()
    if form.validate_on_submit():
        pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data,
        )
        db.session.add(pet)
        db.session.commit()
        flash('New pet added!')
        return redirect(url_for('home_page'))
    return render_template('add.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_details(pet_id):
    # retrieve the pet record from the database
    pet = Pet.query.get_or_404(pet_id)

    # create a form object and populate it with the current pet data
    form = EditPetForm(obj=pet)

    # handle form submission
    if form.validate_on_submit():
        # update the pet record with the form data
        form.populate_obj(pet)
        db.session.commit()
        flash('Pet updated successfully!', 'success')
        return redirect(url_for('home_page'))

    # render the template with the pet data and form
    return render_template('pet_details.html', pet=pet, form=form)
