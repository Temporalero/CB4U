# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class ProjectProject(models.Model):
    _inherit = "project.project"

    category_id = fields.Many2one(
        'crm.tag',
        string="Category",
        help="Project Category CRM"
    )
    project_type_id = fields.Many2one(
        'project.type',
        string="Project Type"
    )
    project_size_id = fields.Many2one(
        'project.size',
        string="Project Size",
    )




