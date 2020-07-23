from odoo import models, fields, api
import datetime

# 使用记录表，多对一，多个使用记录对应一个资产
class Use(models.Model):
    _name = 'bm.use'
    _description = '使用记录'
    zichan_id = fields.Many2one('bm.zichan','设备编号',required=True)
    name_id = fields.Many2one('bm.user','使用人')
    local_id = fields.Many2one('bm.site','使用地点')
    create_on = fields.Datetime('开始时间', default=lambda self: fields.Datetime.now())
    end_on = fields.Datetime('结束时间')
    # long_on = fields.Datetime('借用时长')
    long_on = fields.Char('借用时长')

    def back_close(self):
        DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
        for item in self:
            self.end_on = fields.Datetime.now()
            self.long_on = self.end_on - self.create_on
        return True

