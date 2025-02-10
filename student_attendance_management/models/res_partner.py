from random import choice
from string import digits

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Partners'

    student = fields.Boolean('Is Contact a Student')
    # check_company=True can also be used, but need company_id field
    job_id = fields.Many2one('hr.job', tracking=True)
    function = fields.Char(string='Job Position', compute="_compute_function", store=True, readonly=False)
    badge_id = fields.Char(help="ID used for employee identification.", groups="hr.group_hr_user", copy=False)
    pin = fields.Char(string="PIN", groups="hr.group_hr_user", copy=False,
                      help="PIN used to Check In/Out in the Kiosk Mode of the Attendance application (if enabled in Configuration) and to change the cashier in the Point of Sale application.")

    _sql_constraints = [
        ('badge_id_uniq', 'unique (badge_id)', "The Badge ID must be unique, this one is already assigned to another employee."),
    ]

    @api.constrains('pin')
    def _verify_pin(self):
        for partner in self:
            if partner.pin and not partner.pin.isdigit():
                raise ValidationError(_("The PIN must be a sequence of digits."))

    def _prepare_employee_vals(self):
        """
        Prepare values for creating or updating `hr.employee` from `res.partner`.
        """
        return {
            'name': self.name,
            'job_title': self.function,
            'employee_type': 'student',
            'work_contact_id': self.id,
            'image_1920': self.image_1920,
            'job_id': self.job_id.id,
            'private_street': self.street,
            'private_street2': self.street2,
            'private_city': self.city,
            'private_state_id': self.state_id.id if self.state_id else None,
            'private_zip': self.zip,
            'private_country_id': self.country_id.id if self.country_id else None,
            'private_phone': self.phone,
            'work_phone': self.phone,  # Assuming work_phone is same as phone
            'private_email': self.email,
            'pin': self.pin,
            'barcode': self.badge_id
        }

    @api.model_create_multi
    def create(self, vals_list):
        """
        Link res.partner to hr.employee for students during creation.
        """
        res_partners = super(ResPartner, self).create(vals_list)
        for partner in res_partners:
            if partner.student:
                vals = partner._prepare_employee_vals()
                self.env['hr.employee'].sudo().create(vals)
        return res_partners

    def write(self, vals):
        """
        Link res.partner to hr.employee for students during updates.
        """
        result = super(ResPartner, self).write(vals)
        for partner in self:
            if partner.student:
                employee_vals = partner._prepare_employee_vals()
                if len(partner.employee_ids) == 0:
                    self.env['hr.employee'].sudo().create(employee_vals)
                elif len(partner.employee_ids) == 1:
                    partner.employee_ids.sudo().write(employee_vals)
        return result

    @api.depends('job_id')
    def _compute_function(self):
        for partner in self.filtered('job_id'):
            partner.function = partner.job_id.name

    def generate_random_badge_id(self):
        for partner in self:
            partner.badge_id = '041' + "".join(choice(digits) for i in range(9))
