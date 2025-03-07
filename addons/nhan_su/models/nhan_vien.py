from odoo import models, fields

class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'
    _rec_name = 'ten_nhan_vien'  # Đảm bảo trường này tồn tại trong model

    ten_nhan_vien = fields.Char("Tên nhân viên", required=True)
    ma_dinh_danh = fields.Char("Mã định danh", required=True)
    ngay_sinh = fields.Date("Ngày sinh")
    gioi_tinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
        ('khac', 'Khác')
    ], string="Giới tính", default='')

    que_quan = fields.Char("Quê quán")
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    phong_ban_id = fields.Many2one('phong_ban', string="Phòng ban")


    lich_su_dao_tao_ids = fields.One2many('lich_su_dao_tao', 'nhan_vien_id', string="Lịch sử đào tạo")
