# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Saleorder(models.Model):
    _inherit='sale.order'
    
    credit_limit = fields.Boolean(string="Credit Limit")