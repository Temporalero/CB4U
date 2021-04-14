# -*- coding: utf-8 -*-
import base64

from odoo import fields, models, api


class Partner(models.Model):
    _inherit = "res.partner"

    @api.depends('bank_ids')
    def _compute_bank_item_count(self):
        ResPartnerBank = self.env['res.partner.bank']
        for partner in self:
            partner.bank_item_count = ResPartnerBank.search_count([('partner_id', '=', partner.id)])

    bank_item_count = fields.Integer(compute='_compute_bank_item_count', store=True, string="Bank Items")
    analytic_account_id = fields.Many2one(
        'account.analytic.account', 'Analytic Account',
        help="The analytic account related to a Customer.")
    segment_id = fields.Many2one('res.partner.segment', 'Segmento')

    #_sql_constraints = [
        #('vat_uniq', 'unique (vat)', "El RFC ya existe !"),
        #('check_supplier_bank_count', 'CHECK (supplier_rank = 0 OR (supplier_rank > 0 AND bank_item_count > 0))', "Un Proveedor debe tener al menos una cuanta Bancaria !"),
        #('check_customer_analytic', 'CHECK (customer_rank = 0 OR (customer_rank > 0 AND analytic_account_id IS NOT NULL))', "Un Cliente debe tener cuenta Analitica !"),
    #]


class ResPartnerSegment(models.Model):
    _description = 'Segmento'
    _name = "res.partner.segment"
    _order = "name"

    name = fields.Char('Name', translate=True)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange('partner_id')
    def onchange_partner_id_cb4u(self):
        if self.partner_id and self.partner_id.analytic_account_id:
            self.update({'analytic_account_id': self.partner_id.analytic_account_id})    