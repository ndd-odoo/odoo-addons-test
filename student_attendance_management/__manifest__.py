{
    "name": "Student Attendance Management",
    "version": "1.0",
    'website': "https://altaif.com.sg/",
    'author': "Altaif Singapore PTE. LTD.",
    "Category": "HR",
    "Summary": "Manages Attendance for students using the HR Attendance Module",
    "depends": ['base', 'hr', 'hr_attendance', 'website_slides'],
    "data": [
        'security/ir.model.access.csv',
        'wizards/print_student_badge_views.xml',
        'reports/res_partner_badge.xml',
        'views/hr_attendance_views.xml',
        'views/hr_employee_views.xml',
        'views/res_partner_views.xml'
    ],
    'assets': {
        # 'web.assets_backend': [
        #     'student_attendance_management/static/src/**/*',
        # ],
        # 'web.assets_frontend': [
        #     'student_attendance_management/static/src/**/*',
        # ],
        'hr_attendance.assets_public_attendance': [
            'student_attendance_management/static/src/public_kiosk/**/*',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3'
}
