Đề Tài: Quản lý nhân sự của tôi gồm những chức năng
Thông tin nhân viên
Hợp đồng 
Chấm công
Phòng ban
Lịch sử công tác
Chức vụ
Bảng lương
Khen thưởng kỷ luật
Demo sản phẩm:

Chức năng Nhân viên

![image](https://github.com/user-attachments/assets/e9266915-e881-4f7f-b2c4-e1322a0ace61)
![image](https://github.com/user-attachments/assets/5a9a8e3e-2c31-4373-a131-4ba0534432ab)

Chức năng Hợp đồng

![image](https://github.com/user-attachments/assets/610d3cfd-cd4c-4f78-ac37-1c5bba41142a)
![image](https://github.com/user-attachments/assets/43ebde36-04ba-4199-af68-961403353a8c)

Chức năng chấm công

![image](https://github.com/user-attachments/assets/d8d59052-46cc-40f9-a493-8d7998221f94)
![image](https://github.com/user-attachments/assets/7b6fd457-2992-4e6c-8f49-00e575c296af)





---
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)



# 1. Cài đặt công cụ, môi trường và các thư viện cần thiết

## 1.1. Clone project.
```
git clone https://gitlab.com/anhlta/odoo-fitdnu.git
```
```
cd odoo-fitdnu
```

```
git checkout cntt15_04
```


## 1.2. cài đặt các thư viện cần thiết

Người sử dụng thực thi các lệnh sau đề cài đặt các thư viện cần thiết

```
sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev libssl-dev python3.10-distutils python3.10-dev build-essential libssl-dev libffi-dev zlib1g-dev python3.10-venv libpq-dev
```
## 1.3. khởi tạo môi trường ảo.

Thay đổi trình thông dịch sang môi trường ảo và chạy requirements.txt để cài đặt tiếp các thư viện được yêu cầu
```
python3.10 -m venv ./venv
```
```
source venv/bin/activate
```
```
pip3 install -r requirements.txt
```

# 2. Setup database

Khởi tạo database trên docker bằng việc thực thi file dockercompose.yml.
```
sudo apt install docker-compose
```
```
sudo docker-compose up -d
```

# 3. Setup tham số chạy cho hệ thống

## 3.1. Khởi tạo odoo.conf

Tạo tệp **odoo.conf** có nội dung như sau:

```
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5434
xmlrpc_port = 8069
```

# 4. Chạy hệ thống và cài đặt các ứng dụng cần thiết

Lệnh chạy
```
python3 odoo-bin.py -c odoo.conf -u all
```


Người sử dụng truy cập theo đường dẫn _http://localhost:8069/_ để đăng nhập vào hệ thống.

Hoàn tất
    
