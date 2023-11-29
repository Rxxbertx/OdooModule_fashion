# -*- coding: utf-8 -*-

from odoo import models, fields, api


class owner(models.Model):
    _name="owner.template"
    _description="Dueño"

    name = fields.Char(string = "Nombre", required = "True")
    surname = fields.Char(string = "Apellidos", required = "True")
    phone = fields.Integer(string = "Teléfono", required = "True")
    
