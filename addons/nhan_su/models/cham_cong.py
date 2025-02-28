from odoo import models, fields

class ChamCong(models.Model):
    _name = 'cham_cong'
    _description = 'Chấm công nhân viên'

    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên", required=True)
    ngay = fields.Date("Ngày chấm công", required=True)
    trang_thai = fields.Selection([
        ('di_lam', "Đi làm"),
        ('nghi_phep', "Nghỉ phép"),
        ('nghi_khong_phep', "Nghỉ không phép")
    ], string="Trạng thái", required=True)
