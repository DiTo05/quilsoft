from odoo import http
from odoo.http import request
import json


class PatientController(http.Controller):

    @http.route('/pacientes/consulta/<string:seq>', type='http', auth='public', methods=['GET'])
    def consult_patient(self, seq, **kwargs):
        patient = request.env['patient'].search([('sequence', '=', seq)])
        if patient:
            patient_dict = {
                'seq': patient.sequence,
                'name': patient.name + ' ' + patient.last_name,
                'dni': str(patient.dni),
                'state': patient.state,
            }
            return request.make_response(json.dumps(patient_dict), headers=[('Content-Type', 'application/json')])
        else:
            return request.make_response(
                json.dumps({'error': 'No se encontró ningún patient con la secuencia especificada.'}),
                headers=[('Content-Type', 'application/json')])

