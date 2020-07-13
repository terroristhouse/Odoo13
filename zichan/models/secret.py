from odoo import models, fields, api


# 密级表，一对多，一密级有多个资产
class Secret(models.Model):
    _name = 'bm.secret'
    _description = '密级'
    name = fields.Char('资产密级')
    secret_ids = fields.One2many('bm.zichan','secret_id',string='密级')
