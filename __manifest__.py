{
    'name': 'Vertical Hospital',
    'icon': "/vertical_hospital/static/description/icon.png",
    'version': '1.0',
    'category': 'Vertical',
    'website': 'https://github.com/DiTo05',
    'summary': 'Aplicación para hospitales',
    'description': """
        Este módulo agrega funcionalidades para la gestión de hospitales.
    """,
    'depends': ['base', 'portal'],
    'data': [
        'security/ir.model.access.csv',
        'report/patient_report.xml',
        'data/ir_sequence.xml',
        'data/treatment_restriction_data.xml',
        'views/patient_views.xml',
        'views/treatment_views.xml',
        'views/ir_ui_menu_views.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'OEEL-1',
}


