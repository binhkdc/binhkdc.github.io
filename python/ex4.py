"""
Mục tiêu: Quản lý dữ liệu và sử dụng danh sách (List).

Yêu cầu: Tạo một chương trình cho phép người dùng:

Thêm công việc mới.

Xem danh sách công việc hiện tại.

Xóa một công việc theo vị trí.

Thoát chương trình.

Kiến thức vận dụng: list, các phương thức .append(), .pop(), vòng lặp vô hạn để duy trì menu.
"""

def main():
    work_list = []
    print("Chào mừng bạn đến với chương trình quản lý công việc!")

    while True:
        print("\n1. Thêm công việc.")
        print("2. Xem danh sách công việc hiện tại.")
        print("3. Xóa một công việc theo vị trí.")
        print("4. Thoát chương trình.")
        
        key = int(input("Nhập số để tương tác với menu: "))

        if key == 1:
            name = input("Nhập tên công việc: ")
            work_list.append(name)
            print(f"Đã thêm công việc '{name}'.")

        elif key == 2:
            if not work_list:
                print("Không có công việc nào trong danh sách.")
            else:
                print("Công việc hiện tại:")
                for i, work in enumerate(work_list, 1):
                    print(f"  {i}. {work}")

        elif key == 3:
            if not work_list:
                print("Không có công việc nào để xóa.")
            else:
                pos = int(input(f"Nhập vị trí cần xóa (1-{len(work_list)}): "))
                if 1 <= pos <= len(work_list):
                    removed = work_list.pop(pos - 1)
                    print(f"Đã xóa công việc '{removed}'.")
                else:
                    print("Vị trí không hợp lệ.")

        elif key == 4:
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

main()