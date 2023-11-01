# -*- coding: utf-8 -*-
{
    'name': "clientes",

    'summary': """
        List of clients and their data""",

    'description': """
        List of clients and their data, vehicle information and maintenance data
    """,

    'author': "Bruno",
    'website': "http://www.google.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/client_view.xml',
        'views/templates.xml',
        'views/vehicles_view.xml',
        'views/service_view.xml',
        'views/shift_views.xml',
        'views/wafers_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
