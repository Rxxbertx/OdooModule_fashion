
from odoo import models, fields


class subrand(models.Model):

   _name = 'fashion.subrand'
   _description='fashion.subrand'
   
   name = fields.Char('Submarca',required=True)
   description = fields.Text('Description')
   brand= fields.Many2one(comodel_name="fashion.brand",string="Marca")
   