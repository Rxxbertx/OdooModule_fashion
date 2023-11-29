from encodings import utf_8


coding: utf_8

from odoo import models,api,fields
    
class Modelo(models.Model):
     _name = 'taller.modelo'
     _description='taller.modelo'
     
     name = fields.Char('Nombre', required=True)
     
    