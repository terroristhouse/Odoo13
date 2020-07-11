from odoo import models, fields, api


# 状态表，一对多，一状态有多个资产
class State(models.Model):
    _name = 'bm.state'
    _description = '状态'
    name = fields.Char('资产状态')
