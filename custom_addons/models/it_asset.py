from odoo import models, fields

class ITAsset(models.Model):
    _name = 'it.asset'
    _description = 'Équipement Informatique'

    name = fields.Char(string='Nom', required=True)
    asset_type = fields.Selection([
        ('computer', 'Ordinateur'),
        ('printer', 'Imprimante'),
        ('router', 'Routeur'),
        ('other', 'Autre'),
    ], string='Type', default='computer')
    serial_number = fields.Char(string='Numéro de Série', required=True)
    purchase_date = fields.Date(string='Date d\'Achat')
    customer_id = fields.Many2one('res.partner', string='Client')
    location = fields.Char(string='Emplacement')
    notes = fields.Text(string='Notes')
    active = fields.Boolean(string='Actif', default=True)