from encodings import utf_8


coding: utf_8

from odoo import models,fields


class Vehiculo(models.Model):
     _name = 'taller.vehiculo'
     _description='taller.vehiculo'
     
     marca = fields.Many2one(comodel_name = 'taller.marca', string = 'Marca', required=True)
     modelo = fields.Many2one(comodel_name = 'taller.modelo', string = 'Modelo', required=True)
     owner= fields.Many2one(comodel_name = 'taller.owner', string = 'Dueño', required=True)

     ano = fields.Date(required=True, string="Año")
     
     cilindrada = fields.Integer('Cilindrada en cm3',required=True,size=4)
     
     bastidor = fields.Char(required=True, size=100, string="Bastidor")
     matricula = fields.Char(required=True, size=10, string="Matrícula")
     color= fields.Char('Color')
     
     imagen = fields.Image('Imagen')
     
     tipo_combustible = fields.Selection([("Diesel","Diesel"), ("Gasolina","Gasolina")], string = "Combustible",required=True)
     tipo_vehiculo= field_name = fields.Selection([
        ('Camion', 'Camion'),('Bicicleta','Bicicleta'),('Turismo','Turismo'),('Motocultor','Motocultor'),('Motocicleta','Motocicleta'),('Quad','Quad'),('Portador','Portador'),('Autobus','Autobus'),('Furgón','Furgón')
     ], string='Tipo de Vehiculo',required=True)
     