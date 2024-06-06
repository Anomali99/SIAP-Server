from flask import request, jsonify
from model.santri import Santri
from model import db
from werkzeug.exceptions import BadRequest

def getSantri():
    santri: Santri = db.session.query(Santri).all()
    return jsonify({
        "message": "Status OK",
        "data": [{
                "name":san.name,
                "address":san.address,
                "place_of_birth":san.place_of_birth,
                "date_of_birth":san.date_of_birth.strftime("%d-%m-%Y"),
                "entry_year":san.entry_year,
                "gender":san.gender,
                "parent_name":san.parent_name,
                "telephone_number":san.telephone_number,
                "pas_photo":san.pas_photo,
                "email":san.email} for san in santri]
    }), 200


def ustadzLogin():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        if not all([email, password]):
            raise BadRequest("Missing required fields")
    
        santri = (db.session.query(Santri)
                    .filter(Santri.email==email)
                    .first())
        if santri and santri.checkPass(password):
            return jsonify({
                "message": "Berhasil login",
                "data"   : {
                    "name":santri.name,
                    "address":santri.address,
                    "place_of_birth":santri.place_of_birth,
                    "date_of_birth":santri.date_of_birth.strftime("%d-%m-%Y"),
                    "entry_year":santri.entry_year,
                    "gender":santri.gender,
                    "parent_name":santri.parent_name,
                    "telephone_number":santri.telephone_number,
                    "password":santri.password,
                    "email":santri.email,
                    "pas_photo":santri.pas_photo
                }
            }), 200
        else:
            return jsonify({"message": "Gagal login"}), 200
        
    except BadRequest as e:
        return jsonify({"message": "error", "details": str(e)}), 400
    except Exception as e:
        return jsonify({"message": "error", "details": str(e)}), 500
