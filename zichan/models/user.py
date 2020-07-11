from odoo import models, fields, api


# 使用人表，一对多，一个人有多个资产
class User(models.Model):
    _name = 'bm.user'
    _description = '使用人'
    name = fields.Char('使用人')
