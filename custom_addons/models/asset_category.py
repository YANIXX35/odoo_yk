from odoo import models, fields

class ITAssetCategory(models.Model):
    _name = 'it.asset_category'
    _description = 'Catégorie d\'équipement'

    name = fields.Char(string="Nom", required=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Actif", default=True)