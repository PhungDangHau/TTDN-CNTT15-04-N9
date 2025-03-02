from odoo import models, fields

class ChamCong(models.Model):
    _name = 'cham_cong'
    _description = 'Chấm Công'

    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên")
    ngay_lam_viec = fields.Date(string="Ngày làm việc") 
    gio_vao = fields.Float(string="Giờ vào")
    gio_ra = fields.Float(string="Giờ ra")
    trang_thai = fields.Selection([
        ('di_lam', 'Đi làm'),
        ('nghi_phep', 'Nghỉ phép'),
        ('vang', 'Vắng')
    ], string="Trạng thái")
