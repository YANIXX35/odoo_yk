from odoo import models, fields

class ITIntervention(models.Model):
    _name = 'it.intervention'
    _description = 'Intervention sur un équipement'

    name = fields.Char(string="Nom de l'intervention", required=True)
    intervention_date = fields.Date(string="Date d'intervention", required=True)
    description = fields.Text(string="Description")
    asset_id = fields.Many2one('it.asset', string="Équipement", required=True)
    technician_id = fields.Many2one('it.technician', string="Technicien", help="Technicien responsable de l'intervention")
    state = fields.Selection([
        ('new', 'Nouveau'),
        ('in_progress', 'En cours'),
        ('resolved', 'Résolu'),
        ('cancelled', 'Annulé'),
    ], string="Statut", default='new', required=True)
    priority = fields.Selection([
        ('low', 'Basse'),
        ('medium', 'Moyenne'),
        ('high', 'Haute'),
    ], string="Priorité", default='medium')