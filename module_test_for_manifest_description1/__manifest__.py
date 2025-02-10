# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": """Indian - E-invoicing""",
    "version": "1.03.00",
    'countries': ['in'],
    "category": "Accounting/Localizations/EDI",
    "depends": [
        "account_edi",
        "l10n_in",
        "iap",
        "hr_attendance",
    ],
    "description": """
Key Features
============
#. Easy configuration just a few click to get serial and template from meInvoice and then finish setup

   * Filling some credentials information then get serial and template from meInvoice in a click

   .. image:: module_test_for_manifest_description1/static/description/meinvoice_service1_en.png
      :alt: Meinvoice Provider
      :width: 1100
      :height: 500

   * Finish setup by filling the serial taken from meInvoice into Invoice Journal

#. Issue system's invoice to meInvoice service.
#. Generate a Display Version of the issued invoice and store it in the system for later download.
#. Generate a Converted Version of the issued invoice and store it in the system for later download.
#. Cancel issued meInvoice.
#. Manage the system invoices based on the meInvoice status:

   - Original: the system invoices that have the respective meInvoice issued.
   - Deleted: the system invoices that have the respective meInvoice issued and has been cancel in either system or in meInvoice website.
   - Replaced: the system invoices that have the respective meInvoice replaced by another.
   - Adjusted: the system invoices that have the corresponding meInvoice issued and adjust for another invoice.

#. Customer Portal:

   - Customers can download the display version of the meInvoice in PDF format that also has an EU's Factur-X standard-compliant file attached to it so that they can import it into their own instance.
   - Customers can print the display version of the meInvoice.
   - Customers can download the  XML version of meInvoice so that they can import it to any software that supports meInvoice XML.

#. Support Sandbox mode for your testing before launching in production.
#. Multilingual support for meInvoice issuing to foreign customers according to the state rules: Invoice must be written in Vietnamese
   and may have another language additionally.

    """,
    "data": [
        "data/account_edi_data.xml",
        "views/res_config_settings_views.xml",
        "views/edi_pdf_report.xml",
        "views/account_move_views.xml",
    ],
    "demo": [
        "demo/demo_company.xml",
    ],
    'assets': {
        'hr_attendance.assets_public_attendance': [
            "module_test_for_manifest_description1/static/src/public_kiosk/**/*",
        ]
    },
    'author': "Duong Nguyen (daiduongnguyen2709@gmail.com)",
    "installable": True,
    "license": "LGPL-3",
}
