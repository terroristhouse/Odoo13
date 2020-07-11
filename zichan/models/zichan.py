from odoo import models, fields, api


# 资产主表
class Zichan(models.Model):
    _name = 'bm.zichan'
    _description = '资产'
    name = fields.Char('设备编号', required=True)  # 设备编号
    desc_detail = fields.Text('备注')  # 设备备注
    number = fields.Integer('数量')  # 资产数量
    sequ = fields.Char('序列号')  # 资产序列号
    local_id = fields.Many2one('bm.site', '地点')  # 所在地点
    section_id = fields.Many2one('bm.section', '部门')  # 所在部门
    user_id = fields.Many2one('bm.user', '使用人')  # 使用人
    cate_id = fields.Many2one('bm.cate', '类别')  # 资产类别
    secret_id = fields.Many2one('bm.secret', '密级')  # 资产密级
    state_id = fields.Many2one('bm.state', '状态')  # 资产状态
    type_id = fields.Many2one('bm.type', '型号')  # 资产型号
    use_ids = fields.One2many('bm.use','zichan_id', string='使用记录')  # 使用记录

    def do_close(self):
        for item in self:
            self.state_id = 3
        return True
