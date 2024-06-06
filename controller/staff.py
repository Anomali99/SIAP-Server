from flask import request, current_app, jsonify
from model.asatidz import Asatidz, Job
from model.santri import Santri, Takziran
from model.lembaga import Lembaga, Class, SantriClass, Mengajar, MengajarClass, Subjects
from model.spp import Spp
from werkzeug.utils import secure_filename
from werkzeug.exceptions import BadRequest
from model import db
import os

def _saveIMage(file, dir:str, name:str, entry_year:str) -> str:
        photoname = secure_filename(file.filename)
        filename = f"{name} - {entry_year}.{photoname.rsplit('.', 1)[-1]}"
        file.save(os.path.join(current_app.config.get(dir), filename))
        return filename


def addAsatidz():
    try:
        name = request.form.get("name")
        gender = request.form.get("gender")
        entry_year = request.form.get("entry_year")
        telephone_number = request.form.get("telephone_number")
        password = request.form.get("password")
        email = request.form.get("email")
        pas_photo = request.files.get("pas_photo")

        if not all([name, gender, entry_year, telephone_number, password, email, pas_photo]):
            raise BadRequest("Missing required fields")

        filename = _saveIMage(pas_photo, "ASATIDZ_FOLDER", name, entry_year)

        asatidz = Asatidz(
            name = name,
            gender = gender,
            entry_year = entry_year,
            telephone_number = telephone_number,
            email = email,
            pas_photo = filename
        )
        asatidz.setPass(password=password)

        db.session.add(asatidz)
        db.session.commit()
        
        return jsonify({"message": "success"}), 200
    except BadRequest as e:
        return jsonify({"message": "error", "details": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "error", "details": str(e)}), 500
    finally:
        db.session.close()
    
def addSantri():
    try:
        name = request.form.get("name")
        address = request.form.get("address")
        place_of_birth = request.form.get("place_of_birth")
        date_of_birth = request.form.get("date_of_birth")
        entry_year = request.form.get("entry_year")
        gender = request.form.get("gender")
        parent_name = request.form.get("parent_name")
        telephone_number = request.form.get("telephone_number")
        password = request.form.get("password")
        email = request.form.get("email")
        pas_photo = request.files.get("pas_photo")

        if not all([name, gender, entry_year, telephone_number, password, email, pas_photo, address, place_of_birth, date_of_birth, parent_name]):
            raise BadRequest("Missing required fields")

        filename = _saveIMage(pas_photo, "SANTRI_FOLDER", name, entry_year)

        santri = Santri(
            name = name,
            address = address,
            place_of_birth = place_of_birth,
            date_of_birth = date_of_birth,
            entry_year = entry_year,
            gender = gender,
            parent_name = parent_name,
            telephone_number = telephone_number,
            email = email,
            pas_photo = filename,
        )
        santri.setPass(password=password)

        db.session.add(santri)
        db.session.commit()
        
        return jsonify({"message": "success"}), 200
    except BadRequest as e:
        return jsonify({"message": "error", "details": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "error", "details": str(e)}), 500
    finally:
        db.session.close()

def addSpp():
    try:
        year = request.json.get("year")
        month = request.json.get("month")
        nominal = request.json.get("nominal")

        if not all([year, month, nominal]):
            raise BadRequest("Missing required fields")

        spp = Spp(year=year, month=month, nominal=nominal)
        db.session.add(spp)
        db.session.commit()
        
        return jsonify({"message": "success"}), 200
    except BadRequest as e:
        return jsonify({"message": "error", "details": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "error", "details": str(e)}), 500
    finally:
        db.session.close()

def addTakziran():
    try:
        pelanggaran = request.json.get("pelanggaran")
        nominal = request.json.get("nominal")
        date = request.json.get("date")
        santri_id = request.json.get("santri_id")

        if not all([pelanggaran, nominal, date, santri_id]):
            raise BadRequest("Missing required fields")

        takziran = Takziran(pelanggaran=pelanggaran, nominal=nominal, date=date, santri_id=santri_id)
        db.session.add(takziran)
        db.session.commit()
        
        return jsonify({"message": "success"}), 200
    except BadRequest as e:
        return jsonify({"message": "error", "details": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "error", "details": str(e)}), 500
    finally:
        db.session.close()

def addJob():
    try:
        asatidz_id = request.json.get("asatidz_id")
        job_id = request.json.get("job_id")
        year = request.json.get("year")

        if not all([year, asatidz_id, job_id]):
            raise BadRequest("Missing required fields")

        job = Job(year=year, asatidz_id=asatidz_id, job_id=job_id)
        db.session.add(job)
        db.session.commit()
        
        return jsonify({"message": "success"}), 200
    except BadRequest as e:
        return jsonify({"message": "error", "details": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "error", "details": str(e)}), 500
    finally:
        db.session.close()

def addLembaga():
    try:
        name = request.json.get("name")
        alias = request.json.get("alias")

        if not all([name, alias]):
            raise BadRequest("Missing required fields")

        lembaga = Lembaga(name=name, alias=alias)
        db.session.add(lembaga)
        db.session.commit()
        
        return jsonify({"message": "success"}), 200
    except BadRequest as e:
        return jsonify({"message": "error", "details": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "error", "details": str(e)}), 500
    finally:
        db.session.close()

def addClass():
    try:
        name = request.json.get("name")
        year = request.json.get("year")
        lembaga_id = request.json.get("lembaga_id")
        santri = request.json.get("santri_id")

        if not all([name, year, lembaga_id, santri]):
            raise BadRequest("Missing required fields")

        newClass = Class(name=name, year=year, lembaga_id=lembaga_id)
        db.session.add(newClass)
        db.session.commit()

        for santri_id in santri:
            santri_class = SantriClass(santri_id=santri_id, class_id=newClass.class_id)
            db.session.add(santri_class)
        db.session.commit()
        
        return jsonify({"message": "success"}), 200
    except BadRequest as e:
        return jsonify({"message": "error", "details": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "error", "details": str(e)}), 500
    finally:
        db.session.close()

def addClassMengajar():
    try:
        mengajar_id = request.json.get("mengajar_id")
        class_id = request.json.get("class_id")

        if not all([mengajar_id, class_id]):
            raise BadRequest("Missing required fields")

        mengajarClass = MengajarClass(mengajar_id=mengajar_id, class_id=class_id)
        db.session.add(mengajarClass)
        db.session.commit()
        
        return jsonify({"message": "success"}), 200
    except BadRequest as e:
        return jsonify({"message": "error", "details": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "error", "details": str(e)}), 500
    finally:
        db.session.close()

def addMengajar():
    try:
        asatidz_id = request.json.get("asatidz_id")
        subjects = request.json.get("subjects")

        if not all([asatidz_id, subjects]):
            raise BadRequest("Missing required fields")
        
        subj = db.session.query(Subjects).filter(Subjects.name.in_([val.lower() for val in subjects])).all()
        for sub in subj:
            mengajar = Mengajar(asatidz_id=asatidz_id, subjects_id=sub.subjects_id)
            db.session.add(mengajar)
        db.session.commit()
        
        return jsonify({"message": "success"}), 200
    except BadRequest as e:
        return jsonify({"message": "error", "details": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "error", "details": str(e)}), 500
    finally:
        db.session.close()

def addSubject():
    try:
        name = request.json.get("name")
        lembaga_id = request.json.get("lembaga_id")

        if not all([name, lembaga_id]):
            raise BadRequest("Missing required fields")
        
        mengajar = Subjects(name=name, lembaga_id=lembaga_id)
        db.session.add(mengajar)
        db.session.commit()
        
        return jsonify({"message": "success"}), 200
    except BadRequest as e:
        return jsonify({"message": "error", "details": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "error", "details": str(e)}), 500
    finally:
        db.session.close()
