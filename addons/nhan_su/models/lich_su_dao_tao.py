from odoo import models, fields

class LichSuDaoTao(models.Model):
    _name = 'lich_su_dao_tao'  
    _description = 'Lịch sử đào tạo của nhân viên'
    _rec_name = 'nhan_vien_id'
    
    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên", required=True, ondelete='cascade')
    ten_khoa_dao_tao = fields.Char("Tên khóa đào tạo", required=True)
    ngay_bat_dau = fields.Date("Ngày bắt đầu")
    ngay_ket_thuc = fields.Date("Ngày kết thúc")
    noi_dung_dao_tao = fields.Text("Nội dung đào tạo")
    ghi_chu = fields.Text("Ghi chú")
