from odoo import models, fields

class ITLocation(models.Model):
    _name = 'it.location'
    _description = 'Emplacement'

    name = fields.Char(string="Nom", required=True)
    address = fields.Char(string="Adresse")
    city = fields.Char(string="Ville")
    country = fields.Char(string="Pays")
    active = fields.Boolean(string="Actif", default=True)