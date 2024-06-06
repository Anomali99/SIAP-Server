from model import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Santri(db.Model):
    __tablename__ = 'santri'
    santri_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(225), nullable=False)
    place_of_birth = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date(), nullable=False)
    entry_year = db.Column(db.String(5), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    parent_name = db.Column(db.String(50), nullable=False)
    telephone_number = db.Column(db.String(13), nullable=False)
    password = db.Column(db.String(162), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    pas_photo = db.Column(db.String(50), nullable=True)
    is_active = db.Column(db.Boolean(), nullable=False, default=True)

    def setPass(self, password:str) -> None:
        self.password = generate_password_hash(password)
    
    def checkPass(self, password:str) -> bool:
        return check_password_hash(self.password, password)


class Takziran(db.Model):
    __tablename__ = 'takziran'
    takziran_id = db.Column(db.Integer(), primary_key=True)
    pelanggaran = db.Column(db.String(30), nullable=False)
    nominal = db.Column(db.Integer(), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    is_lunas = db.Column(db.Boolean(), nullable=False, default=False)
    payment_date = db.Column(db.Date())
    santri_id = db.Column(db.Integer(), db.ForeignKey('santri.santri_id'), nullable=False)