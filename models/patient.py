from odoo import api, fields, models, _


class Patient(models.Model):
    _name = "patient"
    _description = "Patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    sequence = fields.Char(string="Sequence", readonly=True, store=True)
    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    complete_name = fields.Char(string='Complete Name', compute='_compute_complete_name', recursive=True, store=True,
                                tracking=True)
    dni = fields.Integer(string='DNI', required=True, tracking=True)
    treatment_ids = fields.One2many('treatment', 'patient_id', string='Treatments Performed')
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('discharged', 'Discharged'),
            ('release', 'release'),
        ], string='State', tracking=True, default='draft')
    company_id = fields.Many2one('res.company', required=True, readonly=True, default=lambda self: self.env.company)

    @api.depends('name', 'last_name')
    def _compute_complete_name(self) -> str:
        for patient in self:
            if patient.name and patient.last_name:
                patient.complete_name = '%s %s' % (patient.name.strip(), patient.last_name.strip())

    @api.model_create_multi
    def create(self, vals_list):
        patients = super(Patient, self).create(vals_list)
        for patient in patients:
            patient['sequence'] = patient.env['ir.sequence'].next_by_code('seq.patient') or '/'
        return patients

    def print_report(self):
        return self.env.ref('vertical_hospital.report_patient').report_action(self)
