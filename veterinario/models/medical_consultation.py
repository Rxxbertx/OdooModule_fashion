# -*- coding: utf-8 -*-


from odoo import models, fields, api


class medical_consult(models.Model):
    _name = "consult.template"
    _description = "Consulta"

    owner = fields.Many2one(comodel_name= "owner.template", string = "Dueño mascota")
    pet = fields.Many2one(comodel_name= "pet.template", string = "Nombre mascota")
    medication = fields.Many2many('medication.template', "pet", string ="Tratamiento")

    pet_sex = fields.Selection(related='pet.sex')
    pet_specie = fields.Char(related='pet.specie.name')
    total_price = fields.Float(string = "Precio total")
    datetime = fields.Datetime(string = "Fecha y hora")

    @api.onchange('owner')
    def onchange_owner(self):
        self.pet = fields.Many2one(comodel_name = 'pet.template', string = 'Nombre mascota') #resetea el campo pet
        domain = {'pet': [('owner', '=', self.owner.id)]}
        return {'domain': domain}