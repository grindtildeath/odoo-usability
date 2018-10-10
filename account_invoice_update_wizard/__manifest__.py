# Copyright 2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# Copyright 2018 Camptocamp
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Account Invoice Update Wizard',
    'version': '11.0.1.0.0',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'summary': 'Wizard to update non-legal fields of an open/paid invoice',
    'description': """
Account Invoice Update Wizard
=============================

This module adds a button *Update Invoice* on Customer and Supplier invoices in Open or Paid state. This button starts a wizard which allows the user to update non-legal fields of the invoice:

* Source Document
* Reference/Description
* Payment terms (update allowed only to a payment term with same number of terms of the same amount and on invoices without any payment)
* Bank Account
* Salesman
* Notes
* Description of invoice lines
* Analytic account
* Analytic tags

    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': [
        'account',
    ],
    'data': [
        'wizard/account_invoice_update_view.xml',
        'views/account_invoice.xml',
    ],
}
