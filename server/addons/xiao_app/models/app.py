# -*- coding:utf-8 -*-
from openerp import fields, api, models

class App(models.Model):
    _name = 'xiao.app'

    name = fields.Char(string="Name")
    version = fields.Char(string="Version", required = True)
    url_download = fields.Char(string="Url", required = True)
    sequence = fields.Integer(string="Sequence")