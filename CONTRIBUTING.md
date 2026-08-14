# 🤝 Hướng Dẫn Đóng Góp (Contributing Guidelines)

Cảm ơn bạn đã quan tâm đến dự án **IT003 — Cấu trúc Dữ liệu và Giải thuật (UIT DSA Handbook)**! Chúng tôi rất hoan nghênh mọi đóng góp từ cộng đồng sinh viên và giảng viên để cẩm nang ngày càng chính xác, hoàn thiện và hữu ích hơn.

---

## 🎯 Các hình thức đóng góp được ưu tiên

1. **Báo lỗi học thuật (Academic / Factual Corrections):**
   - Sai lệch công thức toán, định lý hoặc độ phức tạp thuật toán.
   - Nhầm lẫn về tính chất thuật toán (ví dụ: tính ổn định Stable / Unstable, in-place).
   - Lỗi logic trong bảng chạy tay (dry-run trace) hoặc lời giải bài tập.
2. **Cải tiến mã nguồn & ví dụ (Code & Examples):**
   - Phát hiện lỗi tiềm ẩn trong code C++ (null pointer, tràn số, rò rỉ bộ nhớ).
   - Bổ sung giải thích trực quan ngắn gọn cho các đoạn mã phức tạp.
3. **Sửa lỗi chính tả & định dạng (Formatting & Typos):**
   - Lỗi gõ tiếng Việt, lỗi ngắt dòng hoặc hiển thị KaTeX / SVG.
   - Cải thiện tính tiếp cận (accessibility) trên các thiết bị di động.

---

## 📝 Quy trình gửi đóng góp

### Báo lỗi qua Issue
- Sử dụng các mẫu có sẵn trong mục **Issues**:
  - **[Báo lỗi nội dung học thuật]** nếu phát hiện sai sót kiến thức/thuật toán.
  - **[Báo lỗi hiển thị / kỹ thuật]** nếu gặp sự cố giao diện hoặc render trang.
- Vui lòng trích dẫn rõ vị trí (Tên chương, mục số mấy) và cung cấp tài liệu/nguồn tham chiếu đối chiếu nếu có.

### Gửi Pull Request (PR)
1. Fork repository về tài khoản GitHub cá nhân của bạn.
2. Tạo branch mới với tên gợi mở: ix/ch08-avl-rotation-note hoặc 	ypo/ch03-sorting-table.
3. Chỉ chỉnh sửa các file mã nguồn liên quan trong thư mục chapters/ hoặc tài liệu Markdown.
4. Chạy script uild.ps1 để kiểm tra bản xuất bản master.html vẫn biên dịch bình thường.
5. Tạo Pull Request mô tả rõ nguyên nhân và nội dung thay đổi.

---

## ⚖️ Quy chuẩn nội dung

- **Tôn trọng tài liệu gốc:** Ưu tiên bám sát chương trình giảng dạy và chuẩn thi của Trường ĐH Công nghệ Thông tin (ĐHQG-HCM).
- **Giữ phong cách sư phạm:** Ngắn gọn, trực quan, giải thích rõ trực giác trước khi đưa ra mã nguồn.
- **Không thay đổi phạm vi lớn vô căn cứ:** Tránh viết lại toàn bộ một chương nếu không có lỗi học thuật nghiêm trọng đã được thảo luận từ trước.