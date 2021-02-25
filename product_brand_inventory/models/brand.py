# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################

from odoo import models,fields,api


class ProductBrand(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one('product.brand',string='Brand')
    finished_product = fields.Boolean('Finished Product', compute='_compute_finished_product', store=True)

    @api.onchange('categ_id')
    @api.depends('categ_id')
    def _compute_finished_product(self):
        ProductCategory = self.env['product.category']
        pt_categ = ProductCategory.search([('name','=ilike','PT')], limit=1)
        pt_categories = ProductCategory.search([('id','child_of',pt_categ.id)]).ids if pt_categ else []
        print("__pt_categories", pt_categories)
        for template in self:
            self.finished_product = True if template.categ_id.id in pt_categories else False
 

class BrandProduct(models.Model):
    _name = 'product.brand'
    _description = "Product Brand"


    name= fields.Char('Name')
    brand_image = fields.Binary()
    member_ids = fields.One2many('product.template', 'brand_id')
    product_count = fields.Char('Product Count', compute='get_count_products', store=True)

    @api.depends('member_ids')
    def get_count_products(self):
        self.product_count = len(self.member_ids)


class BrandReportStock(models.Model):
    _inherit = 'stock.quant'

    brand_id  = fields.Many2one(related='product_id.brand_id',
        string='Brand', store=True, readonly=True)
