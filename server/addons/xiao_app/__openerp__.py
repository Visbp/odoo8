# -*- coding:utf-8 -*-
{
    'name': 'App',
    'author': 'Xiao',
    'description': """
    手机APP相关的信息，比如版本更新等！
    """,
    'depends': ['website', 'mail'],
    'data': ['views/app_view.xml', 'views/templates.xml',
             'security/ir.model.access.csv',
             ],
}