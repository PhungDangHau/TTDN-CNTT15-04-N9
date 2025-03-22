from odoo import models, fields, api

class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'
    _rec_name = 'ten_nhan_vien'

    ten_nhan_vien = fields.Char("Tên nhân viên", required=True)
    ma_dinh_danh = fields.Char("Mã định danh", required=True)
    ngay_sinh = fields.Date("Ngày sinh")
    gioi_tinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
        ('khac', 'Khác')
    ], string="Giới tính", default='nam')

    que_quan = fields.Char("Quê quán")
    email = fields.Char("Email", required=True)
    so_dien_thoai = fields.Char("Số điện thoại", required=True)
    dia_chi = fields.Text("Địa chỉ")
    ngay_vao_cong_ty = fields.Date("Ngày vào công ty", required=True)
    trang_thai = fields.Selection([
        ('dang_lam', 'Đang làm việc'),
        ('nghi_phep', 'Nghỉ phép'),
        ('da_nghi', 'Đã nghỉ việc')
    ], string="Trạng thái", default='dang_lam')

    so_yeu_ly_lich_ids = fields.One2many('so_yeu_ly_lich', 'nhan_vien_id', string="Sơ yếu lý lịch")
    phong_ban_id = fields.Many2one("phong_ban", string="Phòng Ban")
    chuc_vu_id = fields.Many2one("chuc_vu", string="Chức Vụ")
    lich_su_dao_tao_ids = fields.One2many('lich_su_dao_tao', 'nhan_vien_id', string="Lịch sử đào tạo")
    lich_su_cong_tac_ids = fields.One2many('lich_su_cong_tac', 'nhan_vien_id', string="Lịch sử công tác")

    file_preview = fields.Html(string="Xem trước Sơ yếu lý lịch", compute="_compute_file_preview")

    @api.depends("so_yeu_ly_lich_ids.file_sy_ly_lich")
    def _compute_file_preview(self):
        for record in self:
            if record.so_yeu_ly_lich_ids:
                file_data = record.so_yeu_ly_lich_ids[0].file_sy_ly_lich
                if file_data:
                    record.file_preview = f"""
                    <iframe src="data:application/pdf;base64,{file_data.decode()}" width="100%" height="500px"></iframe>
                    """
                else:
                    record.file_preview = "<p>Không có sơ yếu lý lịch</p>"
            else:
                record.file_preview = "<p>Không có sơ yếu lý lịch</p>"

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email and '@' not in record.email:
                raise models.ValidationError("Email không hợp lệ!")

    @api.constrains('so_dien_thoai')
    def _check_so_dien_thoai(self):
        for record in self:
            if record.so_dien_thoai and not record.so_dien_thoai.isdigit():
                raise models.ValidationError("Số điện thoại chỉ được chứa chữ số!")
            

