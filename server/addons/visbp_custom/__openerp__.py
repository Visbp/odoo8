# -*- coding: utf-8 -*-
 

{
    'name': 'visbp_custom ',
    'version': '1.0',
    'category': 'Base',
    'description': """

    给客户添加财务相关参数：纳税识别号，国税编码，地税编码，法人名称，个税名单（人名+身份证号）


    """,
    'author': 'xiao',
    'website': 'http://www.visbp.com',
    'depends': ['base'],
    'data': [
             'res_partner_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}