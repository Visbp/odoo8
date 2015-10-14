# -*- coding: utf-8 -*-
from openerp import api, models, fields

class SendMail(models.Model):
    _name = 'xiao.mail'
    _inherit = 'mail.compose.message'

    
