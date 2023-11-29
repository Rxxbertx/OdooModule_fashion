# -*- coding: utf-8 -*-

from odoo import models, fields, api


class specie(models.Model):
    _name = "specie.template"
    _description = "Specie"

    name = fields.Char(string = "Especie", required = 'True')

