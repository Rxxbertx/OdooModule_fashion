# -*- coding: utf-8 -*-


from odoo import models, fields, api


class pet(models.Model):
    _name = "pet.template"
    _description = "Mascota"

    name = fields.Char(string = 'Nombre', required = 'True')
    race = fields.Many2one(comodel_name = 'race.template', string = 'Raza')
    specie = fields.Many2one(comodel_name = 'specie.template', string = 'Especie')
    owner = fields.Many2one(comodel_name= 'owner.template', string = 'Dueño')
    image = fields.Image(string = "Imagen", max_width=400, max_height=400)
    sex = fields.Selection([("M","Macho"), ("H","Hembra")], string = "Sexo")
 
    @api.onchange('specie')
    def onchange_specie(self):
        self.race = fields.Many2one(comodel_name = 'race.template', string = 'Por la Raza!') #resetea el campo race
        domain = {'race': [('specie', '=', self.specie.id)]}
        return {'domain': domain}

