{
    'name': 'Graduación Lentes de Contacto en Ecommerce',
    'version': '1.0',
    'summary': 'Añade campos de graduación para lentes de contacto en el ecommerce',
    'category': 'Website/Website',
    'author': 'Tu Nombre',
    'website': 'https://www.tusitio.com',
    'depends': ['website_sale', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/sale_views.xml',
        'views/website_sale_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'odoo_graduacion_contactos/static/src/css/graduacion.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
