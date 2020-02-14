
{
    'name': "Product searcher",
    'description': """
        Search for products with low stock manually
    """,
    'author': "Meigallo Dixital",
    'website': "http://www.meigallodixital.com",
    'category': 'Generic',
    'version': '12.0.1.0',
    'depends': ['operating_unit'],
    'data': [
        'security/product_searcher_security.xml',
        'security/ir.model.access.csv',
        'views/product_searcher_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}