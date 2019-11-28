# -*- coding: utf-8 -*-

from odoo import models, fields, api

class saleorder(models.Model):
    _inherit='sale.order'
    
    credit_limit_bool = fields.Boolean(string="Over Credit" , compute='_compute_credit_limit')
    
    
    @api.depends('partner_invoice_id.credit_limit' ,'partner_invoice_id.credit')
    def _compute_credit_limit(self):
         for record in self :
                if record.amount_total > record.partner_invoice_id.credit_limit :
                        record[('credit_limit_bool')] = True   
                elif record.partner_invoice_id.credit > record.partner_invoice_id.credit_limit :
                        record[('credit_limit_bool')] = True
