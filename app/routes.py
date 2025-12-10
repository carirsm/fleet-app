from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Truck

main = Blueprint('main', __name__)

# main route
@main.route('/')
def index():
    return '<h1>Welcome!</h1><p>This is the Main Index page</p>'

# truck list
@main.route('/trucks')
def trucks():
    all_trucks = Truck.query.all()
    return render_template('trucks.html', trucks=all_trucks)

# create trucks
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

# edit trucks
@main.route('/trucks/<int:id>/edit')
def edit_truck(id):
    truck = Truck.query.get_or_404(id)
    return render_template('edit_truck.html', truck=truck)

@ main.route('/trucks/<int:id>/update', methods=['POST'])
def update_truck(id):
    truck = Truck.query.get_or_404(id)

    truck.truck_number = request.form.get('truck_number')
    truck.model = request.form.get('model')
    truck.license_plate = request.form.get('license_plate')
    truck.vin = request.form.get('vin')
    truck.status = request.form.get('status')

    db.session.commit()
    
    return redirect(url_for('main.trucks')) 

# delete trucks
@main.route('/trucks/<int:id>/delete', methods=['POST'])
def delete_truck():
    truck = Truck.query.get_or_404(id)

    db.session.delete(truck)
    db.session.commit()

    return redirect(url_for('main.trucks'))