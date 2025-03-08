from odoo import models, fields

class LichSuCongTac(models.Model):
    _name = 'lich_su_cong_tac'
    _description = 'Bảng chứa thông tin lịch sử công tác'
    _rec_name = 'nhan_vien_id'

    nhan_vien_id = fields.Many2one("nhan_vien", string="Nhân viên", required=True)
    phong_ban_id = fields.Many2one("phong_ban", string="Phòng ban", required=True)
    chuc_vu_id = fields.Many2one("chuc_vu", string="Chức vụ", required=True)
    ngay_bat_dau = fields.Date(string="Ngày bắt đầu", required=True)
    ngay_ket_thuc = fields.Date(string="Ngày kết thúc")
    ghi_chu = fields.Text(string="Ghi chú")
