from odoo import http
from odoo.http import request
from odoo.tools import float_round
import datetime

class HrAttendance(http.Controller):

    @staticmethod
    def _get_employee_info_response(employee, course_id=0):
        response = {}
        if employee:
            response = {
                'id': employee.id,
                'employee_name': employee.name,
                'slide_channel_id': request.env['slide.channel'].browse(course_id) if course_id > 0 else None,
                'employee_avatar': employee.image_1920,
                'hours_today': float_round(employee.hours_today, precision_digits=2),
                'total_overtime': float_round(employee.total_overtime, precision_digits=2),
                'last_attendance_worked_hours': float_round(employee.last_attendance_worked_hours, precision_digits=2),
                'last_check_in': employee.last_check_in,
                'attendance_state': employee.attendance_state,
                'hours_previously_today': float_round(employee.hours_previously_today, precision_digits=2),
                'kiosk_delay': employee.company_id.attendance_kiosk_delay * 1000,
                'attendance': {'check_in': employee.last_attendance_id.check_in,
                               'check_out': employee.last_attendance_id.check_out},
                'overtime_today': request.env['hr.attendance.overtime'].sudo().search([
                    ('employee_id', '=', employee.id), ('date', '=', datetime.date.today()),
                    ('adjustment', '=', False)]).duration or 0,
                'use_pin': employee.company_id.attendance_kiosk_use_pin,
                'display_systray': employee.company_id.attendance_from_systray,
                'display_overtime': employee.company_id.hr_attendance_display_overtime
            }
        return response

    @http.route('/hr_attendance/attendance_barcode_scanned', type="json", auth="public")
    def scan_barcode(self, token, barcode):
        eeeeeeeee
        company = self._get_company(token)
        course_id = 0
        if '_' in barcode:
            barcode, course_id = barcode.split('_')[0], barcode.split('_')[1]
        if company:
            employee = request.env['hr.employee'].sudo().search([('barcode', '=', barcode), ('company_id', '=', company.id)], limit=1)
            if employee:
                employee._attendance_action_change(self._get_geoip_response('kiosk'))
                return self._get_employee_info_response(employee, course_id)
        return {}
