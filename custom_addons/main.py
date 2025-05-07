# -*- coding: utf-8 -*-
from odoo import http

class ITAssetManagement(http.Controller):
    @http.route('/it_asset_management/assets', auth='user')
    def list_assets(self, **kw):
        assets = http.request.env['it.asset'].search([])
        return http.request.render('it_asset_management.asset_list', {
            'assets': assets,
        })