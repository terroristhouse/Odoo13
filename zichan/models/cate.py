from odoo import models, fields, api


# 类别表，一对多，一类别有多个资产
class Cate(models.Model):
    _name = 'bm.cate'
    _description = '类别'
    name = fields.Char('资产类别')
