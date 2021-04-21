# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Account Custom CB4U",
    'summary': "Account Custom CB4U",
    'description': """Propage Segment from Partner.""",
    'author': 'Antonio Silva',
    'website': 'https://www.workana.com/freelancer/90449a268cbe15ca4d54379c2a400f9a',
    'category': 'Account',
    'version': '0.1',
    'depends': ['account','partner_custom_cb4u'],
    'data': [
        #'security/ir.model.access.csv',
        'views/account_account_views.xml',
    ],
    'installable': True,
    
}
