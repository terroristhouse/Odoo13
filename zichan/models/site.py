from odoo import models, fields, api


# 地点表一对多，一个地点可以有多个设备
class Local(models.Model):
    _name = 'bm.site'
    _description = '资产地点'
    name = fields.Char('地点')
    # local_ids = fields.One2many('bm.zichan','local_id',string='资产地点')

