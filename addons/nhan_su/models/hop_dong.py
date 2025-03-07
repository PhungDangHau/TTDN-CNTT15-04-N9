from odoo import models, fields

class HopDong(models.Model):
    _name = 'hop_dong'
    _description = 'Hợp đồng lao động'
    _rec_name = "ma_hop_dong"
    
    ma_hop_dong = fields.Char("Mã hợp đồng", required=True)
    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên", required=True)
    ngay_ky = fields.Date("Ngày ký")
    ngay_het_han = fields.Date("Ngày hết hạn")
    loai_hop_dong = fields.Selection([
        ('thu_viec', "Thử việc"),
        ('chinh_thuc', "Chính thức"),
        ('thoi_vu', "Thời vụ")
    ], string="Loại hợp đồng", required=True)
    luong_co_ban = fields.Float("Lương cơ bản")
