# -*- coding: utf-8 -*-
from openerp.osv import fields,osv

class res_partner(osv.osv):
    _inherit = 'res.partner'
    
    _columns = {
        'guoshui': fields.char('国税编码'),
        'dishui': fields.char('地税编码'),
        'shibiehao': fields.char('纳税识别号'),
        'faren': fields.char('法人名称'),
        'vip': fields.char('VIP号', help="代办完成后，下发此代码"),

    }