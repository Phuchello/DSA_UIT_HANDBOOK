# 📘 IT003 — Cấu trúc Dữ liệu và Giải thuật
### UIT DSA Handbook

> Cẩm nang học tập, tra cứu và ôn thi môn **Cấu trúc Dữ liệu và Giải thuật (IT003)** tại **Trường Đại học Công nghệ Thông tin (ĐHQG-HCM)**. Tài liệu được thiết kế theo tiến trình sư phạm: từ trực giác thực tế, phân tích độ phức tạp, mã nguồn C++, bảng chạy tay từng bước (dry-run) đến ngân hàng bài tập và đề thi mẫu.

**Biên soạn:** [Võ Trọng Phúc](https://github.com/Phuchello)

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Book-blue?style=flat&logo=github)](https://phuchello.github.io/DSA_UIT_HANDBOOK/)
[![PDF](https://img.shields.io/badge/PDF-Download%20(1.4MB)-red?style=flat&logo=adobe-acrobat-reader)](IT003_DSA_UIT_CamNang_FINAL.pdf)
[![Course](https://img.shields.io/badge/Course-IT003%20UIT-1e40af?style=flat)](https://www.uit.edu.vn)
[![Code](https://img.shields.io/badge/Code-C%2B%2B17-00599C?style=flat&logo=c%2B%2B)](chapters/)

---

## 🚀 Truy cập & Tải về nhanh

| Phiên bản | Định dạng | Mô tả |
| :--- | :--- | :--- |
| 🌐 **[Đọc trực tuyến trên Web](https://phuchello.github.io/DSA_UIT_HANDBOOK/)** | Web View (Pages) | Giao diện tối ưu đọc trên máy tính, tablet và điện thoại |
| 📄 **[Tải bản PDF hoàn chỉnh (1.4 MB)](IT003_DSA_UIT_CamNang_FINAL.pdf)** | PDF A4 | Sách in chuẩn A4, KaTeX vector sắc nét, layout hoàn thiện |
| 💻 **[File HTML độc lập (Offline)](IT003_DSA_UIT_CamNang_FINAL.html)** | Standalone HTML | Tích hợp sẵn KaTeX & CSS offline, mở không cần Internet |
| 📊 **[Ma trận Đề thi & Bẫy thường gặp](EXAM_DNA.md)** | Markdown | Phân tích cấu trúc đề thi IT003, cách chấm điểm và các bẫy kinh điển |
| 🗺️ **[Bản đồ Kiến thức & Cây phụ thuộc](IT003_SYLLABUS_MAP.md)** | Markdown | Lộ trình 7 tầng kiến thức và biểu đồ Mermaid quan hệ chủ đề |
| 🔍 **[Báo cáo Thẩm định Học thuật (QA)](QA_REPORT_FINAL.md)** | Markdown | Nhật ký kiểm thử thuật toán, fact-check và thang điểm chất lượng |

---

## 💡 Điểm nổi bật của Handbook

* **Trực giác trước cài đặt (Intuition-First):** Mọi cấu trúc dữ liệu và giải thuật đều bắt đầu bằng câu hỏi trực quan *"Vì sao cần cấu trúc này?"* và sơ đồ minh họa trước khi đi vào mã nguồn.
* **Bảng chạy tay từng bước (Dry-run Tables):** Hướng dẫn chi tiết cách lập bảng theo dõi trạng thái biến, con trỏ và mảng qua từng vòng lặp — kỹ năng trọng tâm của các câu hỏi tự luận trong đề thi IT003.
* **Chuẩn C++ giáo khoa & STL song hành:** Trình bày song song mã nguồn C++ thuần con trỏ (phục vụ thi cử, hiểu sâu bản chất cấp phát động) và thư viện chuẩn std:: (phục vụ ứng dụng thực tế).
* **Cảnh báo bẫy học thuật (Pitfalls & Traps):** Làm rõ các lỗi dễ mất điểm như tính chất *Not Stable* của Interchange Sort, điều kiện dừng của tìm kiếm thất bại trên Bảng băm, và quy tắc tách/gộp nút B-Tree bậc 5.

---

## 📚 Phạm vi nội dung (Course Coverage)

Handbook bao quát toàn diện chương trình môn học IT003 tại UIT, được chia thành 5 nhóm kiến thức trọng tâm:

### 1. Nền tảng & Tìm kiếm (Foundations & Searching)
* **Phân tích thuật toán:** Ký pháp tiệm cận Big-O, Big-Omega, Big-Theta, quy tắc cộng/nhân, đếm số phép toán vòng lặp, phân tích độ sâu cây đệ quy và bộ nhớ Call Stack.
* **Thuật toán tìm kiếm:** Linear Search (Tìm kiếm tuyến tính) và Binary Search (Tìm kiếm nhị phân, điều kiện mảng có thứ tự, phòng tránh tràn số khi tính mid).

### 2. 10 Thuật toán Sắp xếp (Sorting Algorithms)
* **Nhóm cơ bản O(n²):** Selection Sort, Interchange Sort (đặc thù UIT, *Not Stable*), Bubble Sort (bản thường vs bản tối ưu cờ hiệu), Insertion Sort, Binary Insertion Sort (giảm phép so sánh nhưng tổng thời gian vẫn O(n²)).
* **Nhóm nâng cao O(n log n):** Shell Sort (phụ thuộc Gap sequence), Heap Sort (với uildHeap chạy trong Theta(n)), Quick Sort (phân hoạch Lomuto chuẩn), Merge Sort (chia để trị, bộ nhớ phụ O(n)).
* **Nhóm phi so sánh:** Radix Sort (sắp xếp theo từng chữ số với cơ số k).

### 3. Cấu trúc Tuyến tính (Linear Data Structures)
* **Danh sách liên kết (Linked List):** DSLK đơn (Singly Linked List) và DSLK đôi (Doubly Linked List), kỹ thuật quản lý con trỏ pHead, pTail, thao tác thêm/xóa đầu/cuối/giữa và giải phóng bộ nhớ an toàn.
* **Ngăn xếp & Hàng đợi (Stack & Queue):** Cơ chế LIFO/FIFO, cài đặt bằng mảng và danh sách liên kết, Hàng đợi vòng (Circular Queue với phép toán Modulo giải quyết tràn giả), ứng dụng kiểm tra ngoặc hợp lệ và chuyển đổi biểu thức Infix sang Postfix.

### 4. Cấu trúc Cây (Tree Structures)
* **Cây nhị phân (Binary Trees):** Định nghĩa nút gốc, nút lá, chiều cao, mức (Level 0), các thứ tự duyệt Pre-order (NLR), In-order (LNR), Post-order (LRN).
* **Cây nhị phân tìm kiếm (BST):** Bất biến cây tìm kiếm, tìm kiếm, chèn, thao tác xóa nút 2 con dùng phần tử thế mạng cực trái cây con phải (Min-Right) hoặc cực phải cây con trái (Max-Left).
* **Cây cân bằng AVL (AVL Trees):** Hệ số cân bằng BF = h(left) - h(right), 4 phép xoay chuẩn (Xoay đơn LL, RR và Xoay kép LR, RL) khôi phục độ phức tạp O(log n).
* **Heap & Hàng đợi ưu tiên (Priority Queue):** Cấu trúc Max-Heap, công thức ánh xạ chỉ số mảng 0-indexed (2i+1, 2i+2, loor((i-1)/2)), thuật toán uildHeap Theta(n) và Heap Sort.
* **Cây B-Tree:** Cấu trúc B-Tree bậc 5 (m = 5, tối đa 4 khóa, tối thiểu 2 khóa), quy tắc tràn khóa tách nút đẩy nổi trung vị thứ 3, và quy tắc xóa nút (mượn anh em hoặc gộp nút).

### 5. Bảng băm, Đồ thị & Luyện thi (Hashing, Graphs & Exam Prep)
* **Bảng băm (Hash Table):** Hàm băm Modulo, các phương pháp giải quyết đụng độ: Linear Probing, Quadratic Probing, Double Hashing (với hàm h2 do đề bài quy định), Separate Chaining; công thức đếm số phép so sánh trung bình tìm kiếm thành công (C_succ) và thất bại (C_unsucc).
* **Đồ thị (Graphs):** Biểu diễn bằng Ma trận kề vs Danh sách kề, duyệt đồ thị theo chiều rộng BFS (Queue) và chiều sâu DFS (Stack/Đệ quy), xử lý đồ thị không liên thông.
* **Đường đi ngắn nhất (Shortest Path):** Thuật toán Dijkstra (trọng số không âm, nguyên lý nới cạnh Relaxation), so sánh với Bellman-Ford (hỗ trợ cạnh âm, phát hiện chu trình âm) và Floyd-Warshall (mọi cặp đỉnh).
* **Exam Toolkit:** Ngân hàng bài tập 5 cấp độ (Level 0 Concept -> Level 5 Challenge) và bộ đề thi thử hoàn chỉnh kèm lời giải chi tiết từng bước.

---

## 📑 Danh mục 16 Phần (Table of Contents)

| Phần | Tên Chương | Nội dung trọng tâm |
| :--- | :--- | :--- |
| **Part 0** | Roadmap & Progression | Phương pháp học tập, lộ trình 4 bước và chiến lược làm bài thi |
| **Part I** | Phân tích Thuật toán | Định nghĩa Big-O, Omega, Theta, quy tắc cộng/nhân, phân tích đệ quy |
| **Part II** | Thuật toán Tìm kiếm | Linear Search, Binary Search, invariants và kỹ thuật tránh tràn số |
| **Part III** | 10 Thuật toán Sắp xếp | Ma trận so sánh 10 thuật toán, độ phức tạp, tính ổn định (Stable) và in-place |
| **Part IV** | Danh sách Liên kết | Singly/Doubly Linked List, thao tác con trỏ và tránh rò rỉ bộ nhớ |
| **Part V** | Ngăn xếp & Hàng đợi | Stack, Queue, Circular Queue (Modulo), chuyển đổi Infix sang Postfix |
| **Part VI** | Cây & Cây Nhị phân | Khái niệm cây, quy ước mức/chiều cao, 3 thứ tự duyệt NLR, LNR, LRN |
| **Part VII** | Cây BST | Cây nhị phân tìm kiếm, tìm kiếm, chèn, xóa nút 2 con (Min-Right / Max-Left) |
| **Part VIII** | Cây Cân bằng AVL | Hệ số BF, bảng tra 4 phép xoay LL, RR, LR, RL và mã nguồn C++ |
| **Part IX** | Heap & Hàng đợi Ưu tiên | Max-Heap, công thức chỉ số mảng 0-indexed, BuildHeap Theta(n), HeapSort |
| **Part X** | Cây B-Tree | B-Tree bậc 5 (m = 5), cơ chế tràn khóa tách nút và mượn/gộp khi xóa |
| **Part XI** | Bảng Băm (Hash Table) | Linear/Quadratic/Double Hashing, đếm số phép so sánh C_succ và C_unsucc |
| **Part XII** | Biểu diễn Đồ thị | Ma trận kề vs Danh sách kề, so sánh bộ nhớ và thời gian truy xuất |
| **Part XIII** | Duyệt Đồ thị | BFS (Queue, loang lớp), DFS (Stack/Đệ quy, đi sâu), bẫy thứ tự đỉnh kề |
| **Part XIV** | Đường đi Ngắn nhất | Thuật toán Dijkstra, bảng trace nới cạnh, so sánh Bellman-Ford & Floyd |
| **Part XV** | Exam Toolkit | Ngân hàng bài tập 5 cấp độ + Đề thi mẫu cuối kỳ kèm đáp án chi tiết |

---

## 📂 Cấu trúc Repository

`	ext
DSA_UIT_HANDBOOK/
├── index.html                           # File phục vụ GitHub Pages (bản xuất bản chính thức)
├── IT003_DSA_UIT_CamNang_FINAL.html      # Bản HTML độc lập (Offline Standalone)
├── IT003_DSA_UIT_CamNang_FINAL.pdf       # Bản PDF hoàn chỉnh chuẩn in ấn A4 (~1.4 MB)
├── print.css                            # CSS định kiểu giao diện web & tối ưu in ấn PDF
├── build.ps1                            # Script PowerShell tự động biên dịch các chapter
├── chapters/                            # Thư mục chứa 16 file nguồn HTML từng chương
│   ├── 00_HOW_TO_MASTER_IT003.html
│   ├── 01_ALGORITHM_ANALYSIS.html
│   ├── ...
│   └── 15_EXAM_TOOLKIT.html
├── assets/                              # Tài nguyên phụ trợ (font KaTeX offline, icons)
├── EXAM_DNA.md                          # Phân tích cấu trúc đề thi IT003 & bẫy kinh điển
├── IT003_SYLLABUS_MAP.md                # Bản đồ phân tầng 7 cấp độ kiến thức & sơ đồ quan hệ
├── SOURCE_AUDIT.md                      # Bảng đối chiếu nguồn tư liệu & tài liệu tham khảo
├── QA_REPORT_FINAL.md                   # Báo cáo thẩm định học thuật và kiểm thử giải thuật
└── CONTRIBUTING.md                      # Hướng dẫn đóng góp & báo lỗi học thuật
`

---

## 🛠️ Hướng dẫn biên dịch tại máy cục bộ (Build Locally)

Nếu bạn muốn chỉnh sửa các chương riêng lẻ trong thư mục chapters/ và biên dịch lại thành file HTML tổng hợp:

1. **Yêu cầu môi trường:** Windows PowerShell 5.1 hoặc PowerShell Core 7+.
2. **Chạy lệnh biên dịch:**
   `powershell
   powershell -ExecutionPolicy Bypass -File .\build.ps1
   `
3. Script sẽ đọc tuần tự 16 chương nguồn và tạo ra file master.html hoàn chỉnh với đầy đủ mục lục, trang bìa và cấu hình KaTeX.

---

## 🔎 Nguồn tư liệu & Quy trình Kiểm định (QA)

* **Nguồn tham chiếu trọng tâm:** Bài giảng chính thức, tài liệu thực hành và các bộ đề thi môn IT003 tại Trường Đại học Công nghệ Thông tin (ĐHQG-HCM).
* **Kiểm chứng học thuật:** Đối chiếu các định lý, công thức tính toán và tính chất thuật toán với giáo trình chuẩn quốc tế (*Introduction to Algorithms - CLRS*).
* **Quy trình QA:** Toàn bộ công thức toán LaTeX, mã nguồn C++, bảng chạy tay và tính chất thuật toán (tính ổn định, độ phức tạp) đã vượt qua quy trình kiểm thử tự động và thẩm định học thuật nghiêm ngặt (đạt điểm đánh giá **100/100** trong [QA_REPORT_FINAL.md](QA_REPORT_FINAL.md)).

---

## 👤 Người biên soạn

**Võ Trọng Phúc**  
* GitHub: [@Phuchello](https://github.com/Phuchello)  
* Dự án: [DSA_UIT_HANDBOOK](https://github.com/Phuchello/DSA_UIT_HANDBOOK)

---

## ⚠️ Lưu ý & Miễn trừ trách nhiệm (Disclaimer)

> Đây là tài liệu học tập độc lập do cá nhân biên soạn nhằm mục đích hỗ trợ sinh viên học tập, tra cứu và ôn thi môn IT003 Cấu trúc Dữ liệu và Giải thuật. Tài liệu **không phải ấn phẩm chính thức** của Trường Đại học Công nghệ Thông tin (ĐHQG-HCM) và không thay thế cho slide bài giảng, giáo trình chính khóa hay các hướng dẫn trực tiếp từ giảng viên bộ môn.

---

## 🤝 Đóng góp (Contributing)

Mọi ý kiến đóng góp, phát hiện lỗi sai học thuật hoặc đề xuất cải tiến nội dung đều được hoan nghênh. Vui lòng đọc kỹ [CONTRIBUTING.md](CONTRIBUTING.md) trước khi tạo Issue hoặc gửi Pull Request.