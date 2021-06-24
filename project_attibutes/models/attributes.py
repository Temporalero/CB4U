# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class ProjectType(models.Model):
    _name = "project.type"
    _description = 'Project Type'
    _rec_name = 'name'
    _order = 'name'


    name = fields.Char(
        string="Description"
    )



class ProjectSize(models.Model):
    _name = "project.size"
    _description = 'Project Size'
    _rec_name = 'name'
    _order = 'name'


    name = fields.Char(
        string="Description"
    )
