# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductSearcher(models.Model):
    _name = 'product.searcher'
    _description = "Product Searcher"

    QUALITIES = (
        ('new', 'New'),
        ('opened', 'Opened'),
        ('used', 'Used'),
    )

    STATES = (
        ('new', 'New'),
        ('opened', 'Opened'),
        ('used', 'Used'),
    )

    operating_unit_id = fields.Many2one(
        'operating.unit',
        'Operating Unit',
        default=lambda self: (
            self.env['res.users'].operating_unit_default_get()
            )
    )
    name = fields.Char()
    description = fields.Text()
    phone = fields.Text()
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency'
    )
    max_price = fields.Monetary()
    quality = fields.Selection(QUALITIES)
    max_date = fields.Datetime()
    state = fields.Selection(STATES)
