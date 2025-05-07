from odoo import models, fields

class SoftwareLicense(models.Model):
    _name = 'software.license'
    _description = 'Licence Logicielle'

    name = fields.Char(string='Nom du Logiciel', required=True)
    license_key = fields.Char(string='Clé de Licence')
    expiration_date = fields.Date(string='Date d\'Expiration')
    seats = fields.Integer(string='Nombre de Postes')
    customer_id = fields.Many2one('res.partner', string='Client')
    notes = fields.Text(string='Notes')
    active = fields.Boolean(string='Actif', default=True)