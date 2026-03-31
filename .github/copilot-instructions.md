# Custom Instructions for GitHub Copilot

## General Principles
- Luôn trả lời bằng tiếng Việt.
- Ưu tiên viết code ngắn gọn, dễ đọc và sử dụng TypeScript.
- Sử dụng mô hình Functional Components và React Hooks.

## Frontend Standards
- **Styling:** Luôn sử dụng Tailwind CSS v4. Tuyệt đối không viết CSS thuần trừ khi bắt buộc.
- **Components:** Sử dụng các component từ daisyUI để xây dựng nhanh giao diện.
- **Icons:** Sử dụng thư viện `lucide-react`.

## Backend Standards
- **Runtime:** Node.js (v20+).
- **Framework:** Express.js với cấu trúc thư mục Monorepo.
- **Database:** Sử dụng Prisma ORM để truy vấn dữ liệu.

## Workflow
- Khi viết mã mới, hãy đi kèm với các comment giải thích logic phức tạp.
- Luôn kiểm tra lỗi (Error Handling) trong các hàm xử lý API (try-catch).