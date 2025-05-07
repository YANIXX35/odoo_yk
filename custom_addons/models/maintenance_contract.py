from odoo import models, fields, api

class MaintenanceContract(models.Model):
    _name = 'maintenance.contract'
    _description = 'Contrat de Maintenance'

    name = fields.Char(string='Nom du Contrat', required=True)
    customer_id = fields.Many2one('res.partner', string='Client', required=True)
    asset_ids = fields.Many2many('it.asset', string='Équipements Couverts')
    start_date = fields.Date(string='Date de Début', required=True)
    end_date = fields.Date(string='Date de Fin', required=True)
    recurring_invoice = fields.Boolean(string='Facturation Récurrente', default=True)
    subscription_id = fields.Many2one('sale.subscription', string='Abonnement')
    notes = fields.Text(string='Notes')

    @api.model
    def _cron_create_subscriptions(self):
        """ Cron method to create subscriptions for recurring contracts """
        contracts = self.search([('recurring_invoice', '=', True), ('subscription_id', '=', False)])
        for contract in contracts:
            contract.create_subscription()

    def create_subscription(self):
        """ Create a subscription for this contract """
        subscription = self.env['sale.subscription'].create({
            'name': 'Contrat de maintenance : ' + self.name,
            'partner_id': self.customer_id.id,
            'start_date': self.start_date,
            'template_id': self.env['sale.subscription.template'].search([], limit=1).id,  # You should create a template
            # Add other relevant fields
        })
        self.subscription_id = subscription.id