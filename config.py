import os

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

HOST = "0.0.0.0"

PORT = 5127

SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{os.environ.get('DB_PASS')}@{os.environ.get('DB_HOST')}/db_siap"
# SQLALCHEMY_DATABASE_URI = "sqlite:///siap.db"

SQLALCHEMY_TRACK_MODIFICATIONS = False

ASATIDZ_FOLDER = "static/asatidz"
SANTRI_FOLDER = "static/santri"