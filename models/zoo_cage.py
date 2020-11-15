# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class ZooCage(models.Model):
    _name = "zoo.cage"
    _description = "Cage of animal in the zoo"

    name = fields.Char('Cage Name', required=True)
    Code = fields.Char('Code', required=True)
    length = fields.Float('Length', required=True)
    width = fields.Float('Width', required=True)
    Height = fields.Float('Height', required=True)
    description = fields.Text('Description')


