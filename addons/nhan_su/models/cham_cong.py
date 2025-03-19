from odoo import models, fields, api
from datetime import datetime

class ChamCong(models.Model):
    _name = 'cham_cong'
    _description = 'Chấm Công'

    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân Viên", required=True)
    ngay_lam_viec = fields.Date(string="Ngày Làm Việc", required=True, default=fields.Date.context_today)
    gio_vao = fields.Char(string="Giờ Vào", default=lambda self: datetime.now().strftime('%H:%M'))
    gio_ra = fields.Char(string="Giờ Ra")

    trang_thai = fields.Selection([
        ('di_lam', 'Đi Làm'),
        ('nghi_phep', 'Nghỉ Phép'),
        ('nghi_khong_phep', 'Nghỉ Không Phép')
    ], string="Trạng Thái", default='di_lam')
@api.onchange('gio_vao')
def _onchange_gio_vao(self):
    """ Khi có giờ vào, tự động tính giờ ra sau 8 tiếng """
    if self.gio_vao:
        gio, phut = map(int, self.gio_vao.split(':'))
        gio_ra = (gio + 8) % 24  # Giới hạn trong 24h
        self.gio_ra = f"{gio_ra:02}:{phut:02}"
