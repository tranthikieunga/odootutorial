# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class ZooCage(models.Model):
    _name = "zoo.cage"
    _description = "Cage of animal in the zoo"

    name = fields.Many2one(comodel_name='product.product',
                               string="Meal name")
    volume = fields.Float('Volume', required=True)
    meals = fields.selection([
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('super', ' Super')
    ], string='meals', default ='breakfast', required=True)

