# -*- coding: utf-8 -*-

from odoo import models, fields, api


class race(models.Model):
    _name = "race.template"
    _description = "Race"

    name = fields.Char(string = "Raza", required = 'True')
    specie = fields.Many2one(comodel_name = "specie.template", string = "Especie", required = 'True')