# -*- coding: utf-8 -*-

from odoo import models, fields, api

class saleorder(models.Model):
    _inherit='sale.order'
    
    credit_limit = fields.Boolean(string="Credit Limit" , compute='_compute_credit_limit')
    
  #  @api.depends('credit_limit,credit_limit_value')
   # def _compute_credit_limit(self):
    #    for record in self :
     #       record[('credit_limit')]=record.partner_invoice_id.credit > record.partner_id.total_due
            
            
class resPartner(models.Model):
    _inherit = 'res.partner'
    
    credit_limit_value = fields.Float(string="Credit Limit Value")
