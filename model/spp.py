from model import db

class Spp(db.Model):
    __tablename__ = 'spp'
    spp_id = db.Column(db.Integer(), primary_key=True)
    year = db.Column(db.String(10), nullable=False)
    month = db.Column(db.String(10), nullable=False)
    nominal = db.Column(db.Integer(), nullable=False)


class SppSantri(db.Model):
    __tablename__ = 'spp_santri'
    santri_id = db.Column(db.Integer(), db.ForeignKey('santri.santri_id'), nullable=False, primary_key=True)
    spp_id = db.Column(db.Integer(), db.ForeignKey('spp.spp_id'), nullable=False, primary_key=True)
    date = db.Column(db.Date())