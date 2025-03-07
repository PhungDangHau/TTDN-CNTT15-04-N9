from odoo import models, fields, api

class KhenThuongKyLuat(models.Model):
    _name = 'khen_thuong_ky_luat'
    _description = 'Bảng khen thưởng và kỷ luật nhân viên'
    _rec_name = 'nhan_vien_id'

    nhan_vien_id = fields.Many2one("nhan_vien", string="Nhân viên", required=True)
    loai = fields.Selection([
        ('khen_thuong', 'Khen thưởng'),
        ('ky_luat', 'Kỷ luật')
    ], string="Loại", required=True)
    ngay = fields.Date(string="Ngày", required=True, default=fields.Date.today)
    ly_do = fields.Text(string="Lý do", required=True)
    hinh_thuc = fields.Char(string="Hình thức", required=True)
    so_tien = fields.Float(string="Số tiền", help="Số tiền thưởng hoặc phạt, nếu có")