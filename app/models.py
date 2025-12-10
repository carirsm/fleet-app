from datetime import datetime, timezone
from app import db

class Truck(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    truck_number = db.Column(db.String(10), nullable=False)
    model = db.Column(db.String(100))
    license_plate = db.Column(db.String(7))
    vin = db.Column(db.String(17))
    status = db.Column(db.String(50), default='available')
    last_updated = db.Column(db.DateTime, 
                             default=lambda: datetime.now(timezone.utc),
                             onupdate=lambda: datetime.now(timezone.utc))