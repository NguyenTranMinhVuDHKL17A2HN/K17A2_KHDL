#bai tap 5.1
print("*   *    ****    *      *      *****")
print("*   *    *       *      *      *   *")
print("*****    ****    *      *      *   *")
print("*   *    *       *      *      *   *")
print("*   *    ****    ****   ****   *****")
#bai tap 5.2
def tinh_toan():
  x = 10
  y = 5

  print("x=10 y=5")
  print("Tổng x+y={}".format(x + y))
  print("Hiệu x-y={}".format(x - y))
  print("Tích x*y={}".format(x * y))
  print("Thương x/y={}".format(x / y))

tinh_toan()
#bai tap 5.3
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
