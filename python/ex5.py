"""
Mục tiêu: Làm việc với API và dữ liệu JSON từ internet.

Yêu cầu: Sử dụng thư viện requests để lấy dữ liệu tỷ giá hối đoái thực tế (ví dụ từ một API miễn phí) và cho phép người dùng nhập số tiền USD để quy đổi sang AUD hoặc ngược lại.

Kiến thức vận dụng: Cài đặt thư viện ngoài (pip install requests), xử lý dữ liệu JSON, quản lý lỗi (Exception handling) khi không có kết nối mạng.
"""

import requests
API_URL = "https://api.frankfurter.dev/v1/latest?base=USD"

def main():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            amount = float(input("Nhập số tiền USD hoặc AUD để quy đổi: "))
            currency = input("Nhập loại tiền tệ (USD hoặc AUD): ").upper()
            if currency == "USD":
                aud_amount = amount * data["rates"]["AUD"]
                print(f"{amount} USD tương đương với {aud_amount:.2f} AUD.")
            elif currency == "AUD":
                usd_amount = amount / data["rates"]["AUD"]
                print(f"{amount} AUD tương đương với {usd_amount:.2f} USD.")
            else:
                print("Loại tiền tệ không hợp lệ.")
        else:
            print("Không thể lấy dữ liệu từ API. Mã lỗi:", response.status_code)        
    except requests.RequestException as e:
        print("Không thể kết nối đến API:", e)

main()
