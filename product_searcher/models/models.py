from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class ProductSearcher(models.Model):
    _name = 'product.searcher'
    _description = "Product Searcher"

    QUALITIES = (
        ('new', 'New'),
        ('good', 'Good status'),
        ('used', 'Used'),
    )

    STATES = (
        ('new', 'New'),
        ('process', 'In process'),
        ('cancel', 'Cancel'),
        ('approved', 'Approved'),
    )

    operating_unit_id = fields.Many2one(
        'operating.unit',
        'Operating Unit',
        default=lambda self: (
            self.env['res.users'].operating_unit_default_get()
            )
    )
    name = fields.Char(required=True)
    client = fields.Char(required=True)
    description = fields.Text()
    phone = fields.Char(required=True)
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency'
    )
    max_price = fields.Monetary()
    quality = fields.Selection(QUALITIES, required=True)
    max_date = fields.Datetime(
        default=lambda self: fields.Datetime.now()+relativedelta(months=2)
    )
    state = fields.Selection(
        STATES,
        required=True,
        default='new')
