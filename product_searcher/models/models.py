from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class ProductSearcherUsers(models.Model):
    _name = 'product.searcher.users'
    _table = "res_users"
    _auto = False
    _description = "Product Search Users"
    _rec_name = "name"
    _order = 'name, login'


    login = fields.Char(required=True)
    partner_id = fields.Many2one('res.partner',
        required=True,
        string='Related Partner')
    name = fields.Char(related='partner_id.name')
    default_operating_unit_id = fields.Many2one(
        'operating.unit', 'Default Operating Unit'
    )


class ProductSearcherOperatingUnit(models.Model):
    _name = 'product.searcher.operating.unit'
    _table = "operating_unit"
    _auto = False
    _description = "Product Search Operating Unit"
    _rec_name = "name"
    _order = 'name'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    active = fields.Boolean('Active', default=True)


class ProductSearcher(models.Model):
    _name = 'product.searcher'
    _description = "Product Searcher"
    _rec_name = "product_name"
    _order = 'max_date desc'

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

    operating_unit_id = fields.Many2one(
        'product.searcher.operating.unit',
        'Operating Unit',
        default=lambda self: self.env['res.users'
                                      ].operating_unit_default_get(self._uid),
        required=True)
    product_name = fields.Char(required=True)
    client = fields.Char(required=True)
    description = fields.Text()
    phone = fields.Char(required=True)
    email = fields.Char()
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
    applicant_id = fields.Many2one(
        'product.searcher.users',
        'Applicant',
        required=True
        )

    @api.onchange('operating_unit_id')
    def _applicants_onchange(self):
        if self.operating_unit_id:
            return {'domain': {'applicant_id': [('default_operating_unit_id', '=', self.operating_unit_id.id)]}}
        return {}

    