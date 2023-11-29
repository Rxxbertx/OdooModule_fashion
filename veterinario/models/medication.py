# -*- coding: utf-8 -*-

from odoo import models, fields, api


class medication(models.Model):
    _name = "medication.template"
    _description = "Tratamiento"

    name = fields.Char(string = "Nombre")
    price = fields.Float(string = "Precio")
    specie = fields.Many2one(comodel_name = 'specie.template', string = 'Especie')
    sex = fields.Selection([("M","Macho"), ("H","Hembra")], string = "Sexo")