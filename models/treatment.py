from odoo import api, fields, models, _
from odoo.exceptions import UserError


class Treatment(models.Model):
    _name = "treatment"
    _description = "Treatment"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name', required=True, tracking=True)
    code = fields.Char('Code', required=True, tracking=True)
    partner_id = fields.Many2one('res.partner', string='Doctor', required=True, tracking=True)
    patient_id = fields.Many2one('patient', string='Patient')

    def _get_default_restriction(self):
        result = self.env.ref('vertical_hospital.first_restriction').id
        if result:
            return [(6, 0, [result])]

    restriction_ids = fields.Many2many('treatment.restriction', string='Restrictions', tracking=True,
                                       default=_get_default_restriction)

    @api.constrains('code')
    def _validate_restrictions(self):
        for record in self:
            for restriction in record.restriction_ids:
                if restriction.name in record.code:
                    raise UserError(_("The code %s cannot contain any restriction, such as the restriction %s." % (
                        record.code, restriction.name)))


class TreatmentRestriction(models.Model):
    _name = "treatment.restriction"
    _description = "Treatment Restriction"

    name = fields.Char('Name', required=True)
