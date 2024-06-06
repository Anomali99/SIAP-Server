from flask import request, jsonify
from werkzeug.exceptions import BadRequest
from model import db
from model.santri import Santri
from model.asatidz import Asatidz, Job, JobAsatid
from model.lembaga import SantriClass, Absensi, Lembaga, Subjects, Mengajar, MengajarClass, Class


def getAsatidz():
    asatidz: Asatidz = db.session.query(Asatidz).all()
    return jsonify({
        "message": "Status OK",
        "data": [{
                "name": ustadz.name,
                "gender": ustadz.gender,
                "entry_year": ustadz.entry_year,
                "telephone_number": ustadz.telephone_number,
                "pas_photo":ustadz.pas_photo,
                "email":ustadz.email} for ustadz in asatidz]
    })

def ustadzLogin():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        if not all([email, password]):
            raise BadRequest("Missing required fields")
    
        ustadz, job, _ = (db.session.query(Asatidz, Job, JobAsatid)
                        .join(JobAsatid, JobAsatid.asatidz_id == Asatidz.asatidz_id)
                        .join(Job, JobAsatid.job_id == Job.job_id)
                        .filter(Asatidz.email==email)
                        .first())
        if ustadz and ustadz.checkPass(password):
            return jsonify({
                "message": "Berhasil login",
                "data"   : {
                    "name": ustadz.name,
                    "gender": ustadz.gender,
                    "entry_year": ustadz.entry_year,
                    "telephone_number": ustadz.telephone_number,
                    "email": ustadz.email,
                    "pas_photo": ustadz.pas_photo,
                    "job": job.job
                }
            }), 200
        else:
            return jsonify({"message": "Gagal login"}), 200
        
    except BadRequest as e:
        return jsonify({"message": "error", "details": str(e)}), 400
    except Exception as e:
        return jsonify({"message": "error", "details": str(e)}), 500
    
def inputScore():
    try:
        santri = request.json.get('santri')
        
        if not all([santri]):
            raise BadRequest("Missing required fields")
        
        class_ids = list(dict.fromkeys(
            value.get("class_id") for value in santri if value.get("class_id") is not None
        ))
        santri_classes = db.session.query(SantriClass).filter(SantriClass.class_id.in_(class_ids)).all()

        for santri_class in santri_classes:
            scores = [value.get("scores") for value in santri if santri_class.class_id == value.get("class_id")][0]
            santri_class.santri_scores = scores
            db.session.merge(santri_class)
        db.session.commit()
        
        return jsonify({"message": "success"}), 200
    except BadRequest as e:
        return jsonify({"message": "error", "details": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "error", "details": str(e)}), 500
    finally:
        db.session.close()

def inputAbsens():
    try:
        santri = request.json.get('santri')
        
        if not all([santri]):
            raise BadRequest("Missing required fields")
        
        for value in santri:
            is_present = value.get("is_present")
            santri_class_id = value.get("santri_class_id")
            date = value.get("date")
            ket = value.get("ket")
            absensi = Absensi(
                is_present= is_present,
                date= date,
                ket= ket,
                santri_class_id= santri_class_id
            )
            db.session.add(absensi)
        db.session.commit()
        
        return jsonify({"message": "success"}), 200
    except BadRequest as e:
        return jsonify({"message": "error", "details": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "error", "details": str(e)}), 500
    finally:
        db.session.close()

def getClass(id):
    try:
        data = []
        results = (db.session
                  .query(Lembaga, Subjects, Mengajar, MengajarClass)
                  .outerjoin(Mengajar, Mengajar.subjects_id == Subjects.subjects_id)
                  .outerjoin(Mengajar, Subjects.lembaga_id == Lembaga.lembaga_id)
                  .outerjoin(Mengajar, Mengajar.mengajar_id == MengajarClass.mengajar_id)
                  .filter(Mengajar.asatidz_id == id).all())
        
        result = (db.session
                  .query(SantriClass, Santri, Class)
                  .outerjoin(SantriClass, SantriClass.santri_id == Santri.santri_id)
                  .outerjoin(SantriClass, SantriClass.class_id == Class.class_id)
                  .filter(SantriClass.class_id.in_([cls.MengajarClass.class_id for cls in results])).all())
        
        for lembaga, subjects, _, mengajarClass in results:
            for class_santri, santri, cls in result:
                if class_santri.class_id == mengajarClass.class_id:
                    data.append({
                        "lembaga_id":lembaga.lembaga_id,
                        "lembaga":lembaga.name,
                        "subjects":subjects.name,
                        "class":{
                            "class_santri_id":class_santri.class_santri_id,
                            "class_id":cls.class_id,
                            "name":cls.name,
                            "year":cls.year,
                            "santri":{
                                "santri_id":santri.santri_id,
                                "name":santri.name
                            }
                        }
                    })

        return jsonify({"message": "success", "data":data}), 200
    except Exception as e:
        return jsonify({"message": "error", "details": str(e)}), 500
