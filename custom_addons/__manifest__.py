{
    'name': 'Gestion de Parc Informatique',
    'version': '1.0',
    'summary': 'Module Odoo pour la gestion de parc informatique et la facturation récurrente',
    'description': """
        Ce module permet de gérer les équipements informatiques, les licences logicielles et les contrats de maintenance.
        Il intègre également la facturation récurrente.
    """,
    'category': 'Services',
    'author': 'Votre Nom',
    'website': 'votre_site_web.com',
    'depends': ['base', 'sale_subscription', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/it_asset_views.xml',
        'views/software_license_views.xml',
        'views/maintenance_contract_views.xml',
        'views/technician_views.xml',
        'views/asset_category_views.xml',
        'views/location_views.xml',
        'views/intervention_views.xml',
        'views/ticket_views.xml',
        'views/menus.xml',
        'data/cron.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}