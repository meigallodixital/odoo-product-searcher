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
        ('pending', 'Pending'),
        ('process', 'In process'),
        ('cancel', 'Cancel'),
        ('approved', 'Approved'),
    )

    operating_unit_id = fields.Selection(
        selection=lambda self: self._compute_operating_unit(),
        string='Operating Unit',
        default=lambda self: (
                self.env['res.users'].operating_unit_default_get().id
            ),
        required=True
        
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
        default='pending')

    def _compute_operating_unit(self):
        return [(str(ou.id), ou.name) for ou in self.env['operating.unit'].sudo().search([('active', '=', True)]).sorted(key=lambda r: r.name)]