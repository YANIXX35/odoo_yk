from odoo import models, fields

class ITTicket(models.Model):
    _name = 'it.ticket'
    _description = 'Ticket d\'assistance'

    name = fields.Char(string="Titre", required=True)
    description = fields.Text(string="Description")
    asset_id = fields.Many2one('it.asset', string="Équipement concerné")
    requester_id = fields.Many2one('res.partner', string="Demandeur", required=True)
    technician_id = fields.Many2one('it.technician', string="Technicien assigné")
    state = fields.Selection([
        ('new', 'Nouveau'),
        ('in_progress', 'En cours'),
        ('resolved', 'Résolu'),
        ('closed', 'Cloturé'),
    ], string="Statut", default='new', required=True)
    priority = fields.Selection([
        ('low', 'Basse'),
        ('medium', 'Moyenne'),
        ('high', 'Haute'),
    ], string="Priorité", default='medium')
    create_date = fields.Date(string="Date de création", default=fields.Date.today)