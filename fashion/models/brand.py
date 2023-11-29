# -*- coding: utf-8 -*-

from odoo import models, fields


class brand(models.Model):

   _name = 'fashion.brand'
   _description='fashion.brand'
   
   name = fields.Char('Marca',required=True)
   description = fields.Text('Description')
   