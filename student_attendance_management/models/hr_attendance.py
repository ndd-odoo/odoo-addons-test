from odoo import models, fields


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'
    _description = 'Hr Attendance'

    slide_channel_id = fields.Many2one('slide.channel', 'Course')
