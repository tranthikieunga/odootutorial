# -*- coding: utf-8 -*-
# https://www.odoo.com/documentation/14.0/reference/module.html
{
    'name': 'Zoo City',
    'summary': """Zoo City Tutorials""",
    'description': """Building my own zoo city""",
    'author': 'minhng.info',
    'maintainer': 'minhng.info',
    'website': 'https://minhng.info',
    'category': 'Uncategorized', # https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/zoo_animal_views.xml',   # <-- add this line
        'wizard/toy_add_views.xml',     # <-- add this line
        'views/zoo_creature_views.xml',
        'views/zoo_cage_views.xml',
    ],
    'demo': [],
    'css': [],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
}