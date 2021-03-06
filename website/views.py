from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Cuisine, Store
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        cuisine = request.form.get('cuisine')
        store = request.form.get('store')
        cuisine_type = request.form.get('cuisine_type')
        if cuisine_type == 0:
            cuisine_type = 'None'
        print(db.session.query())
        if len(cuisine) < 1:
            pass 
        else:
            new_cuisine = Cuisine(data=cuisine, user_id=current_user.id)
            db.session.add(new_cuisine)
            db.session.commit()
            flash('Cuisine added!', category='success')

        if len(store) < 1:
            pass 
        else:
            new_store = Store(data=store, user_id=current_user.id, cuisine_type=cuisine_type)
            db.session.add(new_store)
            db.session.commit()
            flash('Store added!', category='success')

    return render_template("home.html", user=current_user)
