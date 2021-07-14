#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class AccountAsset(models.Model):
    _inherit = 'account.asset'


    image_1920 = fields.Image(
        string="Image",
    )
