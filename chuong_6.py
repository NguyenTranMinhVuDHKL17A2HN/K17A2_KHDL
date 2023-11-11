#bai tap 6.1
print("*   *    ****    *      *      *****")
print("*   *    *       *      *      *   *")
print("*****    ****    *      *      *   *")
print("*   *    *       *      *      *   *")
print("*   *    ****    ****   ****   *****")
#bai tap 6.2
def tinh_toan():
  x = 10
  y = 5

  print("x=10 y=5")
  print("Tổng x+y={}".format(x + y))
  print("Hiệu x-y={}".format(x - y))
  print("Tích x*y={}".format(x * y))
  print("Thương x/y={}".format(x / y))

tinh_toan()
#bai tap 6.3
# Nhập dữ liệu
ten_hang = input("Tên hàng: ")
so_luong = int(input("Số lượng: "))
don_gia = int(input("Đơn giá: "))

# Tính tiền phải trả
tien_phai_tra = so_luong * don_gia

# Xuất kết quả
print("Tên hàng:", ten_hang)
print("Số lượng:", so_luong)
print("Đơn giá:", don_gia)
print("Tiền phải trả:", tien_phai_tra)
#bai tap 6.4
#Yêu cầu 1 
print("(5-3)//2=",(5-3)//2)
# yêu câù 2
print("8-3*2-(1+1)",8-3*2-(1+1))
#bai tap 6.5
# Nhập dữ liệu
so_luong = int(input("Nhập số lượng: "))
don_gia = int(input("Nhập đơn giá: "))

# Tính tiền hàng
tien_hang = so_luong * don_gia

# Xuất kết quả
print("Thành tiền:", tien_hang)
#bai tap 6.6
# Nhập dữ liệu
so_keo = int(input("Nhập số lượng kẹo: "))
so_nguoi = int(input("Nhập số người: "))

# Tính số kẹo mỗi người được chia
so_keo_moi_nguoi = so_keo // so_nguoi

# Tính số kẹo dư
so_keo_du = so_keo % so_nguoi

# Xuất kết quả
print("Số kẹo mỗi người được chia:", so_keo_moi_nguoi)
print("Số kẹo dư:", so_keo_du)