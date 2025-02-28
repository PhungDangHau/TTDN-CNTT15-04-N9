from odoo import models, fields

class PhongBan(models.Model):
    _name = 'phong_ban'
    _description = 'Phòng ban'

    ten_phong_ban = fields.Char("Tên phòng ban", required=True)
    ma_phong_ban = fields.Char("Mã phòng ban", required=True)
    truong_phong_id = fields.Many2one('nhan_vien', string="Trưởng phòng")
    nhan_vien_ids = fields.One2many('nhan_vien', 'phong_ban_id', string="Danh sách nhân viên")
