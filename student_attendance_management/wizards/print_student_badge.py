from odoo import fields, models, api


class PrintStudentBadge(models.Model):
    _name = "print.student.badge"
    _description = 'Print Student Badge'

    slide_channel_ids = fields.Many2many('slide.channel')
    slide_channel_id = fields.Many2one('slide.channel', 'Course', domain="[('id', 'in', slide_channel_ids)]")

    @api.model
    def default_get(self, fields):
        """
        Get the default value for catalogue_store_ids
        """

        res = super(PrintStudentBadge, self).default_get(fields)

        partner_id = self.env['res.partner'].browse(self._context.get('active_id'))
        slide_channel = []
        for slide_channel_partner in self.env['slide.channel.partner'].search([('partner_id', '=', partner_id.id), ('member_status', 'in', ['joined', 'ongoing'])]):
            slide_channel.append(slide_channel_partner.channel_id.id)
        if slide_channel:
            res['slide_channel_ids'] = [(6, 0, slide_channel)]

        return res

    def print_badge(self):
        data = {
            'partner': self.env['res.partner'].search([('id', '=', self._context.get('active_id'))]).id,
            'course_id': self.slide_channel_id.id,
            'course_name': self.slide_channel_id.name,
        }
        return self.env.ref('student_attendance_management.res_partner_print_badge').report_action(self, data=data)
