# -*- coding:utf-8 -*-
from openerp import http

class App(http.Controller):
    @http.route('/app/version/', auth='public', website=True)
    def index(self, **kw):
        Apps = http.request.env['xiao.app']
        return http.request.render('xiao_app.index', {'apps': Apps.search([])})