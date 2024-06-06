from . import handle_options, api
from controller import santri

api.route('/santri/get', methods=['GET'])(santri.getSantri)


api.route('/santri/get', methods=['GET'])(handle_options)