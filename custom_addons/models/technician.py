from odoo import models, fields

class ITTechnician(models.Model):
    _name = 'it.technician'
    _description = 'Technicien'

    name = fields.Char(string="Nom", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Téléphone")
    active = fields.Boolean(string="Actif", default=True)
    skill_level = fields.Selection([
        ('junior', 'Junior'),
        ('intermediate', 'Intermédiaire'),
        ('senior', 'Senior'),
    ], string="Niveau de compétence", default='intermediate')