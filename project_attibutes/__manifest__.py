#!/usr/bin/env python3
# -*- coding: utf-8 -*-

{
    'name': "Project Attributes",
    'version': "14.0.1",
    'author': "Kewitz Colina",
    'website': "https://github.com/colinak",
    'summary': "Project Atributes",
    'sequence': 10,
    'description': "Project Atributes Categories",
    'category': "project",
    'depends': [
        'base',
        'crm',
        'project',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/project_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False

}



