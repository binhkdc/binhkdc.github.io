---
name: fix-and-pr
description: "Workflow tự động: pull code mới nhất, tạo nhánh fix, phân tích & sửa lỗi trong source code, push lên remote, rồi chờ người dùng review và merge. Dùng khi: cần fix bug, fix lỗi, sửa code, tạo pull request, push branch, git workflow, fix và PR."
argument-hint: "Mô tả lỗi cần fix (vd: 'fix lỗi TypeScript trong index.html')"
---

# Fix & Pull Request Workflow

## Mô tả
Skill này thực hiện toàn bộ quy trình Git chuẩn:
**pull → tạo nhánh → phân tích lỗi → fix → push → chờ merge**

## Khi nào dùng
- Người dùng yêu cầu fix lỗi, sửa bug, cải thiện code
- Cần tạo nhánh riêng để không ảnh hưởng `main`/`master`
- Muốn push code và chờ review trước khi merge

---

## Quy trình từng bước

### Bước 1 – Xác định trạng thái repository
```bash
git status
git branch
```
- Kiểm tra nhánh hiện tại và các thay đổi chưa commit.
- Nếu có thay đổi chưa commit → hỏi người dùng có muốn stash không.

### Bước 2 – Pull code mới nhất từ remote
```bash
git checkout dev       # hoặc master
git pull origin dev    # cập nhật code mới nhất
```
- Đảm bảo xuất phát từ code mới nhất, tránh conflict.

### Bước 3 – Tạo nhánh fix mới
Đặt tên nhánh theo định dạng: `fix/<mô-tả-ngắn>` hoặc `fix/<ngày>-<mô-tả>`

Ví dụ:
```bash
git checkout -b fix/typescript-loaddata
git checkout -b fix/20260331-camera-section
```
- Dùng chữ thường, dấu gạch ngang, không dấu cách.
- Tối đa 50 ký tự.

### Bước 4 – Phân tích & Fix lỗi
1. Đọc file liên quan để hiểu context đầy đủ.
2. Kiểm tra lỗi compile/lint nếu có.
3. Thực hiện các thay đổi cần thiết — **chỉ sửa đúng phần được yêu cầu**, không refactor thêm.
4. Thêm comment tiếng Việt giải thích logic phức tạp (theo chuẩn dự án).
5. Xác nhận lại file đã sửa đúng và không có lỗi mới.

### Bước 5 – Commit thay đổi
```bash
git add <file-đã-sửa>
git commit -m "fix: <mô tả ngắn gọn bằng tiếng Anh>"
```
Format commit message theo [Conventional Commits](https://www.conventionalcommits.org/):
| Prefix | Dùng khi |
|--------|----------|
| `fix:` | Sửa bug, lỗi |
| `feat:` | Thêm tính năng |
| `refactor:` | Tái cấu trúc code |
| `style:` | Sửa CSS/Tailwind |
| `docs:` | Cập nhật tài liệu |

### Bước 6 – Push nhánh lên remote
```bash
git push origin <tên-nhánh>
```
- Sau khi push, hiển thị URL nhánh để người dùng tạo Pull Request.

### Bước 7 – Thông báo & chờ merge
Sau khi push thành công, **báo cáo rõ ràng** cho người dùng:

```
✅ Đã push nhánh: fix/<tên-nhánh>
📋 Tóm tắt thay đổi:
   - File đã sửa: <danh sách file>
   - Nội dung fix: <mô tả>
   
🔀 Bước tiếp theo (do bạn thực hiện):
   1. Mở Pull Request trên GitHub/GitLab
   2. Review code
   3. Merge vào main khi sẵn sàng
   
🔗 Tạo PR nhanh:
   https://github.com/<owner>/<repo>/compare/fix/<tên-nhánh>
```

---

## Quy tắc quan trọng
- **Không tự merge** vào `main`/`master` — luôn chờ người dùng.
- **Không force push** (`--force`) trừ khi được yêu cầu rõ ràng.
- **Không xóa nhánh** sau khi push — để người dùng review.
- Nếu có conflict khi pull → dừng lại, thông báo cho người dùng xử lý thủ công.
- Nếu push thất bại (ví dụ nhánh đã tồn tại) → đề xuất tên nhánh mới.

---

## Xử lý tình huống đặc biệt

### Có thay đổi chưa commit
```bash
git stash push -m "wip: trước khi fix"
# sau khi xong có thể restore bằng: git stash pop
```

### Nhánh đã tồn tại trên remote
Đổi tên nhánh thêm suffix `-v2`, `-v3`, hoặc thêm timestamp:
```bash
git checkout -b fix/typescript-loaddata-v2
```

### Không có remote origin
Thông báo cho người dùng cần cấu hình remote trước:
```bash
git remote add origin <url>
```
