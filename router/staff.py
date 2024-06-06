from . import handle_options, api
from controller import staff


api.route('/staff/add/asatidz', methods=['POST'])(staff.addAsatidz)
api.route('/staff/add/santri', methods=['POST'])(staff.addSantri)
api.route('/staff/add/spp', methods=['POST'])(staff.addSpp)
api.route('/staff/add/takziran', methods=['POST'])(staff.addTakziran)
api.route('/staff/add/job', methods=['POST'])(staff.addJob)
api.route('/staff/add/lembaga', methods=['POST'])(staff.addLembaga)
api.route('/staff/add/class', methods=['POST'])(staff.addClass)
api.route('/staff/add/lembaga', methods=['POST'])(staff.addLembaga)
api.route('/staff/add/classMengajar', methods=['POST'])(staff.addClassMengajar)
api.route('/staff/add/mengajar', methods=['POST'])(staff.addMengajar)
api.route('/staff/add/subject', methods=['POST'])(staff.addSubject)

api.route('/staff/add/asatidz', methods=['OPTIONS'])(handle_options)
api.route('/staff/add/santri', methods=['OPTIONS'])(handle_options)
api.route('/staff/add/spp', methods=['OPTIONS'])(handle_options)
api.route('/staff/add/takziran', methods=['OPTIONS'])(handle_options)
api.route('/staff/add/job', methods=['OPTIONS'])(handle_options)
api.route('/staff/add/lembaga', methods=['OPTIONS'])(handle_options)
api.route('/staff/add/class', methods=['OPTIONS'])(handle_options)
api.route('/staff/add/classMengajar', methods=['OPTIONS'])(handle_options)
api.route('/staff/add/mengajar', methods=['OPTIONS'])(handle_options)
api.route('/staff/add/subject', methods=['OPTIONS'])(handle_options)