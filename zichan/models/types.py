from odoo import models, fields, api


# 型号表，一对多，一型号有多个资产
class Type(models.Model):
    _name = 'bm.type'
    _description = '型号'
    name = fields.Char('资产型号')
