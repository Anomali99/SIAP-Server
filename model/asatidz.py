from model import db
from werkzeug.security import generate_password_hash, check_password_hash

class Asatidz(db.Model):
    __tablename__ = 'asatidz'
    asatidz_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    entry_year = db.Column(db.String(5), nullable=False)
    telephone_number = db.Column(db.String(13), nullable=False)
    password = db.Column(db.String(162), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    pas_photo = db.Column(db.String(50), nullable=True)
    is_active = db.Column(db.Boolean(), nullable=False, default=True)

    def setPass(self, password:str) -> None:
        self.password = generate_password_hash(password)
    
    def checkPass(self, password:str) -> bool:
        return check_password_hash(self.password, password)


class Job(db.Model):
    __tablename__ = 'job'
    job_id = db.Column(db.Integer(), primary_key=True)
    job = db.Column(db.String(10), nullable=False)


class JobAsatid(db.Model):
    __tablename__ = 'job_asatiz'
    jobaz_id = db.Column(db.Integer(), primary_key=True)
    year = db.Column(db.String(10), nullable=False)
    asatidz_id = db.Column(db.Integer(), db.ForeignKey('asatidz.asatidz_id'), nullable=False)
    job_id = db.Column(db.Integer(), db.ForeignKey('job.job_id'), nullable=False)