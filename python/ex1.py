"""
Mục tiêu: Làm quen với nhập dữ liệu (input), ép kiểu và các phép toán cơ bản.

Yêu cầu: Viết chương trình yêu cầu người dùng nhập vào hai số thực và một phép tính (+, -, *, /). Sau đó, in ra kết quả tương ứng.

Kiến thức vận dụng: input(), float(), cấu trúc điều kiện if...elif...else.
"""

a = float(input("Nhập số thực a: "))
b = float(input("Nhập số thực b: "))
phep_tinh = input("Nhập phép tính (+, -, *, /): ")

if phep_tinh == "+":
    print("Kết quả:", a + b)
elif phep_tinh == "-":
    print("Kết quả:", a - b)
elif phep_tinh == "*":
    print("Kết quả:", a * b)
elif phep_tinh == "/":
    if b != 0:
        print("Kết quả:", a / b)
    else:
        print("Lỗi: Không thể chia cho 0")
else:
    print("Lỗi: Phép tính không hợp lệ")