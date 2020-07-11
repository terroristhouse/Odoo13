from odoo import models, fields, api


# 部门表，一对多，一个部门有多个资产
class Section(models.Model):
    _name = 'bm.section'
    _description = '部门'
    name = fields.Char('部门')
    # section_ids = fields.One2many('bm.zichan','section_id',string='部门')
