from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Truck

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return '<h1>Welcome!</h1><p>This is the Main Index page</p>'

@main.route('/trucks')
def trucks():
    all_trucks = Truck.query.all()
    return render_template('trucks.html', trucks=all_trucks)

@main.route('/trucks/new')
def new_truck():
    return render_template('new_truck.html')

@main.route('/trucks/create', methods=['POST'])
def create_truck():
    truck_number = request.form.get('truck_number')
    model = request.form.get('model')
    license_plate = request.form.get('license_plate')
    vin = request.form.get('vin')
    status = request.form.get('status')

    new_truck = Truck(
        truck_number=truck_number,
        model=model,
        license_plate=license_plate,
        vin=vin,
        status=status
    )

    db.session.add(new_truck)
    db.session.commit()

    return redirect(url_for('main.trucks'))