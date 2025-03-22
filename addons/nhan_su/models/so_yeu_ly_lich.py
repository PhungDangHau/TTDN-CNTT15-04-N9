from odoo import models, fields

class SoYeuLyLich(models.Model):
    _name = "so_yeu_ly_lich"
    _description = "Sơ yếu lý lịch"

    nhan_vien_id = fields.Many2one("nhan_vien", string="Nhân viên", ondelete="cascade")
    
    # Thay vì nhập từng thông tin, chỉ cần file upload
    file_sy_ly_lich = fields.Binary(string="Tải lên sơ yếu lý lịch")
    file_name = fields.Char(string="Tên file")  # Lưu tên file để hiển thị
