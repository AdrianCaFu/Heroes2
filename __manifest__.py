# -*- coding: utf-8 -*-
{
    'name': "Heroes",

    'summary': "Modulo para heroes",

    'description': "Modulo que permite asignar superheroes a los trabajadores",

    'author': "Adrian Cano",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/heroe_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'license':  'LGPL-3'
}

