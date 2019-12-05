# -*- coding: utf-8 -*-

from odoo import models, fields, api

class saleorder(models.Model):
    _inherit='sale.order'
    
    # Over credit is Computed value to check if the customer exceeds his credit limit
    credit_limit_bool = fields.Boolean(string="Over Credit" , compute='_compute_credit_limit' , store=True
                                       , default= False , help='This value is true if customer exceed his credit limit')
    
    # Method used to assign the value of the Over credit by calculating the amount due of the current sales order
    # plus the value of the total amount this customer owes your company.
    # it assigns True only in this total exceeds the credit limit value given to each customer.
    
    @api.depends('partner_invoice_id.credit_limit' ,'partner_invoice_id.credit','amount_total')
    def _compute_credit_limit(self):
         for record in self :
                if record.amount_total + record.partner_invoice_id.credit > record.partner_invoice_id.credit_limit :
                        record[('credit_limit_bool')] = True
