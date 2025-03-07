from odoo import models, fields, api

class BangLuong(models.Model):
    _name = 'bang_luong'
    _description = 'Bảng lương của nhân viên'
    _rec_name = 'nhan_vien_id'

    thang = fields.Selection([
        ('1', 'Tháng 1'), ('2', 'Tháng 2'), ('3', 'Tháng 3'), ('4', 'Tháng 4'),
        ('5', 'Tháng 5'), ('6', 'Tháng 6'), ('7', 'Tháng 7'), ('8', 'Tháng 8'),
        ('9', 'Tháng 9'), ('10', 'Tháng 10'), ('11', 'Tháng 11'), ('12', 'Tháng 12')
    ], string="Tháng", required=True)
    
    nam = fields.Integer(string="Năm", required=True, default=lambda self: fields.Date.today().year)
    luong_co_ban = fields.Float(string="Lương cơ bản", required=True)
    phu_cap = fields.Float(string="Phụ cấp", default=0.0)
    thuong = fields.Float(string="Thưởng", default=0.0)
    khau_tru = fields.Float(string="Khấu trừ", default=0.0)
    tong_luong = fields.Float(string="Tổng lương", compute="_compute_tong_luong", store=True)
    nhan_vien_id = fields.Many2one("nhan_vien", string="Nhân viên", required=True)
    phong_ban_id = fields.Many2one("phong_ban", string="Phòng ban", required=True)
    chuc_vu_id = fields.Many2one("chuc_vu", string="Chức vụ", required=True)
    
    @api.depends('luong_co_ban', 'phu_cap', 'thuong', 'khau_tru')
    def _compute_tong_luong(self):
        for record in self:
            record.tong_luong = record.luong_co_ban + record.phu_cap + record.thuong - record.khau_tru