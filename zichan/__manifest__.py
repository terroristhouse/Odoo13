# -*- coding: utf-8 -*-
{
    'name': "资产管理",

    'summary': """
        用于运维组的资产管理软件""",

    'description': """
        用于运维组的资产管理软件
    """,

    'author': "Mr. Liu",
    'website': "/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/zichans.xml',
        'views/zichan_detail.xml',
        'views/zichan_use.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
