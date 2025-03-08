from odoo import models, fields, api
from datetime import date

class ChamCong(models.Model):
    _name = 'cham_cong'
    _description = 'Chấm công nhân viên'
    _rec_name = "nhan_vien_id"

    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên", required=True)
    ngay = fields.Date("Ngày chấm công", required=True, default=fields.Date.context_today)
    trang_thai = fields.Selection([
        ('di_lam', "Đi làm"),
        ('nghi_phep', "Nghỉ phép"),
        ('nghi_khong_phep', "Nghỉ không phép")
    ], string="Trạng thái", required=True, default='di_lam')

    @api.model
    def auto_cham_cong(self):
        """Tự động chấm công cho tất cả nhân viên mỗi ngày"""
        nhan_vien_ids = self.env['nhan_vien'].search([])  # Lấy tất cả nhân viên
        ngay_hom_nay = date.today()

        for nhan_vien in nhan_vien_ids:
            # Kiểm tra nếu hôm nay đã có bản ghi chấm công cho nhân viên này
            if not self.env['cham_cong'].search([('nhan_vien_id', '=', nhan_vien.id), ('ngay', '=', ngay_hom_nay)]):
                self.create({
                    'nhan_vien_id': nhan_vien.id,
                    'ngay': ngay_hom_nay,
                    'trang_thai': 'di_lam'  # Mặc định là đi làm
                })
