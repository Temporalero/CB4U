# -*- coding: utf-8 -*-

from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = "account.move"

    segment_id = fields.Many2one(related='partner_id.segment_id', readonly=True, store=True)
    invoice_date_end = fields.Date(
        string="Fecha Promesa de Pago",
        help="Extensión Fecha Promesa de Pago"
    )
