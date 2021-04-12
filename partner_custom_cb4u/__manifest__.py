# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Partner Custom CB4U",
    'summary': "Partner Custom CB4U",
    'description': """Supplier VAT mandatory.""",
    'author': 'Antonio Silva',
    'website': 'https://www.workana.com/freelancer/90449a268cbe15ca4d54379c2a400f9a',
    'category': 'base',
    'version': '0.1',
    'depends': ['contacts','sale','account'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    
}
