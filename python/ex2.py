"""
Mục tiêu: Hiểu về thư viện ngoài và vòng lặp không xác định.

Yêu cầu: Máy tính sẽ chọn ngẫu nhiên một con số từ 1 đến 100. Người dùng có nhiệm vụ đoán số đó. Sau mỗi lần đoán, máy tính sẽ gợi ý "Quá cao" hoặc "Quá thấp" cho đến khi người dùng chọn đúng.

Kiến thức vận dụng: import random, vòng lặp while, so sánh số nguyên.
"""

import random

random_number = random.randint(1, 100)

guess_number = int(input("Đoán một số từ 1 đến 100: "))

while guess_number != random_number:
    if guess_number < random_number:
        print("Quá thấp! Thử lại.")
    else:
        print("Quá cao! Thử lại.")
    
    guess_number = int(input("Đoán một số từ 1 đến 100: "))

print("Chúc mừng! Bạn đã đoán đúng số:", random_number)