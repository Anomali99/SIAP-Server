from model import db

class Lembaga(db.Model):
    __tablename__ = 'lembaga'
    lembaga_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    alias = db.Column(db.String(20), nullable=False)


class Subjects(db.Model):
    __tablename__ = 'subjects'
    subjects_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lembaga_id = db.Column(db.Integer(), db.ForeignKey('lembaga.lembaga_id'), nullable=False)


class Mengajar(db.Model):
    __tablename__ = 'mengajar'
    mengajar_id = db.Column(db.Integer(), primary_key=True)
    asatidz_id = db.Column(db.Integer(), db.ForeignKey('asatidz.asatidz_id'), nullable=False)
    subjects_id = db.Column(db.Integer(), db.ForeignKey('subjects.subjects_id'), nullable=False)


class Class(db.Model):
    __tablename__ = 'class'
    class_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(10), nullable=False)
    lembaga_id = db.Column(db.Integer(), db.ForeignKey('lembaga.lembaga_id'), nullable=False)


class MengajarClass(db.Model):
    __tablename__ = 'mengajar_class'
    mengajar_id = db.Column(db.Integer(), db.ForeignKey('mengajar.mengajar_id'), nullable=False, primary_key=True)
    class_id = db.Column(db.Integer(), db.ForeignKey('class.class_id'), nullable=False, primary_key=True)


class SantriClass(db.Model):
    __tablename__ = 'santri_class'
    santri_class_id = db.Column(db.Integer(), primary_key=True)
    santri_scores = db.Column(db.Integer())
    santri_id = db.Column(db.Integer(), db.ForeignKey('santri.santri_id'), nullable=False)
    class_id = db.Column(db.Integer(), db.ForeignKey('class.class_id'), nullable=False)


class Absensi(db.Model):
    __tablename__ = 'absensi'
    absensi_id = db.Column(db.Integer(), primary_key=True)
    is_present = db.Column(db.Boolean(), nullable=False)
    date = db.Column(db.Date())
    ket = db.Column(db.String(10))
    santri_class_id = db.Column(db.Integer(), db.ForeignKey('santri_class.santri_class_id'), nullable=False)