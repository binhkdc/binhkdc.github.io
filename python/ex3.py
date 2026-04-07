"""
Mục tiêu: Làm quen với xử lý chuỗi và cấu trúc dữ liệu Dictionary.

Yêu cầu: Cho một đoạn văn bản dài. Hãy viết chương trình đếm xem mỗi từ xuất hiện bao nhiêu lần và in kết quả ra màn hình dưới dạng danh sách.

Kiến thức vận dụng: Các phương thức của string (split, lower, strip), vòng lặp for, kiểu dữ liệu dict.
"""

txt = "lorEm ipsum dolor sIt amet, consECtetur adipiScing elit. Sed do eiusmod tempor inciDidunt ut labore et dolore Magna aliquA."

def count_words(text):
    word_count = {}
    for word in text.split():
        word = word.strip(",.?!;:").lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

result = count_words(txt)
for word, count in result.items():
    print(f"'{word}': {count} lần")