from . import handle_options, api
from controller import asatidz

api.route('/asatidz/get', methods=['GET'])(asatidz.getAsatidz)
api.route('/asatidz/login', methods=['POST'])(asatidz.ustadzLogin)
api.route('/asatidz/class/<id>', methods=['GET'])(asatidz.getClass)
api.route('/asatidz/score/santri', methods=['POST'])(asatidz.inputScore)
api.route('/asatidz/absen/santri', methods=['POST'])(asatidz.inputAbsens)

api.route('/asatidz/get', methods=['OPTIONS'])(handle_options)
api.route('/asatidz/login', methods=['OPTIONS'])(handle_options)
api.route('/asatidz/class/<id>', methods=['OPTIONS'])(handle_options)
api.route('/asatidz/score/santri', methods=['OPTIONS'])(handle_options)
api.route('/asatidz/absen/santri', methods=['OPTIONS'])(handle_options)
