# -*- coding: utf-8 -*-
from openerp.osv import fields,osv

class res_partner(osv.osv):
    _inherit = 'res.partner'
    
    _columns = {
        'vip': fields.char('VIP number', help="While the Company registration is completed, issued this number"),

    }
    _sql_constraints = [
        ('vip_uniq', 'unique(vip, company_id)', 'VIP number must be unique per Company!'),
    ]    
        
