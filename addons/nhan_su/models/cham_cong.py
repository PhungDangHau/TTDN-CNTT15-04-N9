from odoo import models, fields, api
from datetime import datetime, timedelta
import pytz

class ChamCong(models.Model):
    _name = 'cham_cong'
    _description = 'Chấm Công'

    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân Viên", required=True)
    ngay_lam_viec = fields.Date(string="Ngày Làm Việc", required=True, default=fields.Date.context_today)
    gio_vao = fields.Char(string="Giờ Vào")
    gio_ra = fields.Char(string="Giờ Ra")
    trang_thai = fields.Selection([
        ('di_lam', 'Đi Làm'),
        ('nghi_phep', 'Nghỉ Phép'),
        ('nghi_khong_phep', 'Nghỉ Không Phép')
    ], string="Trạng Thái", default='di_lam')

    @api.model
    def create(self, vals):
        """Tự động ghi nhận giờ vào theo thời gian thực khi tạo bản ghi mới"""
        user_tz = pytz.timezone(self.env.user.tz or 'UTC')
        now = datetime.now(user_tz).strftime('%H:%M')
        if 'gio_vao' not in vals or not vals['gio_vao']:
            vals['gio_vao'] = now
        return super(ChamCong, self).create(vals)

    @api.model
    def auto_check_in(self):
        """Tự động chấm công giờ vào theo thời gian thực cho nhân viên nếu chưa có"""
        nhan_vien_ids = self.env['nhan_vien'].search([])
        today = fields.Date.today()
        user_tz = pytz.timezone(self.env.user.tz or 'UTC')
        now = datetime.now(user_tz).strftime('%H:%M')

        for nhan_vien in nhan_vien_ids:
            cham_cong = self.search([('nhan_vien_id', '=', nhan_vien.id), ('ngay_lam_viec', '=', today)], limit=1)
            if not cham_cong:
                self.create({
                    'nhan_vien_id': nhan_vien.id,
                    'ngay_lam_viec': today,
                    'gio_vao': now,
                    'trang_thai': 'di_lam',
                })

    @api.model
    def auto_check_out(self):
        """Tự động ghi giờ ra theo thời gian thực sau 8 tiếng nếu nhân viên đã có giờ vào"""
        today = fields.Date.today()
        cham_cong_records = self.search([('ngay_lam_viec', '=', today), ('gio_ra', '=', False)])
        user_tz = pytz.timezone(self.env.user.tz or 'UTC')

        for cham_cong in cham_cong_records:
            if cham_cong.gio_vao:
                gio_vao = datetime.strptime(cham_cong.gio_vao, '%H:%M')
                gio_ra = (gio_vao + timedelta(hours=8)).strftime('%H:%M')
                cham_cong.write({'gio_ra': gio_ra})
