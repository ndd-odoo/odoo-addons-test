from odoo import models, api


class ResPartnerBadge(models.AbstractModel):
    _name = 'report.student_attendance_management.print_partner_badge'

    @api.model
    def _get_report_values(self, docids, data=None):
        partner = self.env['res.partner'].browse(data['partner'])
        return {
            'docs': partner,
            'badge_course_id': partner.badge_id + '_' + str(data['course_id']) if data['course_id'] else partner.badge_id,
            'course_name': data['course_name']
        }
