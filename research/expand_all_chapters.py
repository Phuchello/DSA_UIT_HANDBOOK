import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

BASE_DIR = r"C:\Users\lyle3\.gemini\antigravity\scratch\IT003_DSA_BOOK"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
os.makedirs(CHAPTERS_DIR, exist_ok=True)

def write_ch02():
    html = """<section class="chapter" id="ch02">
    <div class="chapter-header">
        <span class="badge badge-core">PART II</span>
        <h1>THUẬT TOÁN TÌM KIẾM (SEARCHING ALGORITHMS)</h1>
    </div>

    <h2>1. Intuition (Trực giác & Động lực)</h2>
    <p>Tìm kiếm là thao tác cơ bản nhất trong khoa học máy tính. Hãy tưởng tượng việc tìm một từ trong từ điển 1,000 trang: bạn sẽ lật từng trang từ đầu (Linear Search) hay mở đôi cuốn sách ở giữa rồi tiếp tục chia đôi (Binary Search)? Bài toán tìm kiếm quyết định hiệu năng của mọi cơ sở dữ liệu lớn.</p>

    <h2>2. Formal Model (Định nghĩa Thuật toán)</h2>
    <p>Cho dãy $A = (a_0, a_1, \dots, a_{n-1})$ và giá trị $x$. Tìm vị trí index $i \in [0, n-1]$ sao cho $a_i = x$, hoặc trả về $-1$ nếu $x \notin A$.</p>
    <p><span class="badge badge-uit-convention">IT003 CONVENTION</span>: Với Tìm kiếm Nhị phân, điều kiện tiên quyết bắt buộc là dãy $A$ phải <strong>được sắp xếp theo một thứ tự xác định (tăng dần hoặc giảm dần)</strong>.</p>

    <h2>3. Visual Diagram (Sơ đồ Tìm kiếm Nhị phân)</h2>
    <div class="diagram-container">
        <svg width="600" height="140" viewBox="0 0 600 140" xmlns="http://www.w3.org/2000/svg">
            <rect width="600" height="140" fill="#f8fafc" rx="8"/>
            <g transform="translate(40, 40)">
                <rect x="0" y="0" width="50" height="45" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
                <text x="25" y="27" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">3</text>
                <text x="25" y="62" font-family="Inter" font-size="10" fill="#64748b" text-anchor="middle">0</text>
                <rect x="50" y="0" width="50" height="45" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
                <text x="75" y="27" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">7</text>
                <text x="75" y="62" font-family="Inter" font-size="10" fill="#64748b" text-anchor="middle">1 (L)</text>
                <rect x="100" y="0" width="50" height="45" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
                <text x="125" y="27" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">11</text>
                <text x="125" y="62" font-family="Inter" font-size="10" fill="#64748b" text-anchor="middle">2</text>
                <rect x="150" y="0" width="50" height="45" fill="#3b82f6" stroke="#1e40af" stroke-width="2"/>
                <text x="175" y="27" fill="#ffffff" font-family="Inter" font-size="13" font-weight="bold" text-anchor="middle">15</text>
                <text x="175" y="62" font-family="Inter" font-size="10" fill="#1e40af" font-weight="bold" text-anchor="middle">3 (MID)</text>
                <rect x="200" y="0" width="50" height="45" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
                <text x="225" y="27" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">19</text>
                <text x="225" y="62" font-family="Inter" font-size="10" fill="#64748b" text-anchor="middle">4</text>
                <rect x="250" y="0" width="50" height="45" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
                <text x="275" y="27" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">24</text>
                <text x="275" y="62" font-family="Inter" font-size="10" fill="#64748b" text-anchor="middle">5 (R)</text>
                <rect x="300" y="0" width="50" height="45" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
                <text x="325" y="27" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">31</text>
                <text x="325" y="62" font-family="Inter" font-size="10" fill="#64748b" text-anchor="middle">6</text>
            </g>
        </svg>
    </div>

    <h2>4. Algorithm & Mechanics (Cơ chế hoạt động)</h2>
    <p>So sánh $x$ với phần tử ở giữa `mid = left + (right - left) / 2`. Nếu $x == a[mid]$, trả về `mid`. Nếu $x < a[mid]$, thu hẹp phạm vi về bên trái (`right = mid - 1`). Ngược lại về bên phải (`left = mid + 1`).</p>

    <h2>5. C++ Educational & STL Code</h2>
    <pre><code>// Educational Iterative Binary Search
int binarySearch(int a[], int n, int x) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2; // Phòng tránh tràn số int
        if (a[mid] == x) return mid;
        if (a[mid] < x) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

// STL Implementation Example
#include <iostream>
#include <vector>
#include <algorithm>

bool searchSTL(const std::vector<int>& v, int x) {
    return std::binary_search(v.begin(), v.end(), x);
}</code></pre>

    <h2>6. Complexity Analysis & Invariants</h2>
    <ul>
        <li><strong>Linear Search:</strong> Best Case $\mathcal{O}(1)$, Worst Case $\Theta(n)$, Average Case $\Theta(n)$. Space: $\mathcal{O}(1)$.</li>
        <li><strong>Binary Search:</strong> Best Case $\mathcal{O}(1)$, Worst Case $\Theta(\log_2 n)$, Average Case $\Theta(\log_2 n)$. Space: $\mathcal{O}(1)$ với lặp, $\mathcal{O}(\log n)$ với đệ quy.</li>
    </ul>

    <h2>7. Dry Run Table (Chạy tay chi tiết)</h2>
    <p>Tìm $x = 19$ trong mảng $A = [3, 7, 11, 15, 19, 24, 31]$ ($n=7$):</p>
    <table>
        <thead>
            <tr><th>Bước</th><th>left</th><th>right</th><th>mid</th><th>a[mid]</th><th>So sánh x=19</th><th>Hành động</th></tr>
        </thead>
        <tbody>
            <tr><td>1</td><td>0</td><td>6</td><td>3</td><td>15</td><td>$15 < 19$</td><td>`left = mid + 1 = 4`</td></tr>
            <tr><td>2</td><td>4</td><td>6</td><td>5</td><td>24</td><td>$24 > 19$</td><td>`right = mid - 1 = 4`</td></tr>
            <tr><td>3</td><td>4</td><td>4</td><td>4</td><td>19</td><td>$19 == 19$</td><td><strong>Tìm thấy! Trả về index 4</strong></td></tr>
        </tbody>
    </table>

    <h2>8. Common Errors & IT003 Exam Style</h2>
    <div class="callout callout-warning">
        <span class="badge badge-exam-style">IT003 EXAM STYLE</span>
        <p><strong>Lỗi thường gặp:</strong> Tính `mid = (left + right) / 2` có thể bị tràn số khi `left + right > INT_MAX`. Luôn dùng `left + (right - left) / 2`. Ngoài ra, điều kiện vòng lặp phải là `left <= right` (dấu `<=` bắt buộc để không bỏ sót trường hợp 1 phần tử).</p>
    </div>

    <h2>9. Quick Recall & Exercise Ladder</h2>
    <ul>
        <li><strong>Level 0:</strong> Tìm kiếm Nhị phân có thể áp dụng cho danh sách liên kết đơn được sắp xếp không? Vì sao?
            <br><em>Đáp án:</em> Không hiệu quả, vì DSLK không hỗ trợ truy xuất ngẫu nhiên $a[mid]$ trong $\mathcal{O}(1)$, làm độ phức tạp tăng lên $\mathcal{O}(n)$.
        </li>
        <li><strong>Level 1:</strong> Cho mảng $A = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]$. Trình bày bảng trace tìm kiếm $x = 23$.
            <br><em>Gợi ý:</em> Bước 1: mid=4 (16 < 23) $\rightarrow$ Bước 2: mid=7 (56 > 23) $\rightarrow$ Bước 3: mid=5 (23 == 23).
        </li>
    </ul>

    <div class="callout">
        <div class="callout-title">📝 Tóm kết Chương 2</div>
        <p>Tìm kiếm nhị phân giảm phạm vi tìm kiếm đi một nửa sau mỗi bước ($\mathcal{O}(\log n)$). Hãy luôn nhớ kiểm tra mảng đã sắp xếp trước khi gọi thuật toán!</p>
    </div>
</section>"""
    with open(os.path.join(CHAPTERS_DIR, "02_SEARCHING.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated 02_SEARCHING.html")

def write_ch03():
    html = """<section class="chapter" id="ch03">
    <div class="chapter-header">
        <span class="badge badge-core">PART III</span>
        <h1>CÁC THUẬT TOÁN SẮP XẾP (SORTING ALGORITHMS)</h1>
    </div>

    <h2>1. Intuition (Trực giác & Động lực)</h2>
    <p>Sắp xếp dữ liệu giúp việc tìm kiếm, thống kê và xử lý trở nên dễ dàng và nhanh chóng hơn. Trong thực tế, các thuật toán sắp xếp được chia làm 2 nhóm chính: <strong>Sắp xếp cơ bản ($\mathcal{O}(n^2)$)</strong> dễ cài đặt và <strong>Sắp xếp nâng cao ($\mathcal{O}(n \log n)$)</strong> cho dữ liệu lớn.</p>

    <h2>2. Formal Model & Complexity Matrix</h2>
    <div class="callout">
        <div class="callout-title">📊 Bảng Tổng Hợp 10 Thuật Toán Sắp Xếp Chuẩn IT003</div>
        <table>
            <thead>
                <tr><th>Thuật toán</th><th>Best Case</th><th>Average Case</th><th>Worst Case</th><th>Space</th><th>Stable?</th><th>In-Place?</th></tr>
            </thead>
            <tbody>
                <tr><td><strong>Selection Sort</strong></td><td>$\Theta(n^2)$</td><td>$\Theta(n^2)$</td><td>$\Theta(n^2)$</td><td>$\mathcal{O}(1)$</td><td>No</td><td>Yes</td></tr>
                <tr><td><strong>Interchange Sort</strong></td><td>$\Theta(n^2)$</td><td>$\Theta(n^2)$</td><td>$\Theta(n^2)$</td><td>$\mathcal{O}(1)$</td><td>No</td><td>Yes</td></tr>
                <tr><td><strong>Bubble Sort</strong></td><td>$\Theta(n)$</td><td>$\Theta(n^2)$</td><td>$\Theta(n^2)$</td><td>$\mathcal{O}(1)$</td><td>Yes</td><td>Yes</td></tr>
                <tr><td><strong>Insertion Sort</strong></td><td>$\Theta(n)$</td><td>$\Theta(n^2)$</td><td>$\Theta(n^2)$</td><td>$\mathcal{O}(1)$</td><td>Yes</td><td>Yes</td></tr>
                <tr><td><strong>Binary Insertion</strong></td><td>$\Theta(n \log n)$</td><td>$\Theta(n^2)$</td><td>$\Theta(n^2)$</td><td>$\mathcal{O}(1)$</td><td>Yes</td><td>Yes</td></tr>
                <tr><td><strong>Shell Sort</strong></td><td>$\Theta(n \log n)$</td><td>$\Theta(n^{1.3})$</td><td>$\Theta(n^2)$</td><td>$\mathcal{O}(1)$</td><td>No</td><td>Yes</td></tr>
                <tr><td><strong>Heap Sort</strong></td><td>$\Theta(n \log n)$</td><td>$\Theta(n \log n)$</td><td>$\Theta(n \log n)$</td><td>$\mathcal{O}(1)$</td><td>No</td><td>Yes</td></tr>
                <tr><td><strong>Quick Sort</strong></td><td>$\Theta(n \log n)$</td><td>$\Theta(n \log n)$</td><td>$\Theta(n^2)$</td><td>$\mathcal{O}(\log n)$</td><td>No</td><td>Yes</td></tr>
                <tr><td><strong>Merge Sort</strong></td><td>$\Theta(n \log n)$</td><td>$\Theta(n \log n)$</td><td>$\Theta(n \log n)$</td><td>$\Theta(n)$</td><td>Yes</td><td>No</td></tr>
                <tr><td><strong>Radix Sort</strong></td><td>$\Theta(d \cdot n)$</td><td>$\Theta(d \cdot n)$</td><td>$\Theta(d \cdot n)$</td><td>$\Theta(n + k)$</td><td>Yes</td><td>No</td></tr>
            </tbody>
        </table>
    </div>

    <h2>3. Visual Diagram (Sơ đồ Phân hoạch Quick Sort)</h2>
    <div class="diagram-container">
        <svg width="620" height="150" viewBox="0 0 620 150" xmlns="http://www.w3.org/2000/svg">
            <rect width="620" height="150" fill="#f8fafc" rx="8"/>
            <g transform="translate(30, 40)">
                <!-- Elements < Pivot -->
                <rect x="0" y="0" width="180" height="45" fill="#dcfce7" stroke="#15803d" stroke-width="2"/>
                <text x="90" y="27" fill="#15803d" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">Phần tử &le; Pivot</text>
                <!-- Pivot -->
                <rect x="190" y="0" width="80" height="45" fill="#3b82f6" stroke="#1e40af" stroke-width="2"/>
                <text x="230" y="27" fill="#ffffff" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">PIVOT</text>
                <!-- Elements > Pivot -->
                <rect x="280" y="0" width="280" height="45" fill="#fee2e2" stroke="#b91c1c" stroke-width="2"/>
                <text x="420" y="27" fill="#b91c1c" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">Phần tử &ge; Pivot</text>
            </g>
        </svg>
    </div>

    <h2>4. Algorithm & Mechanics (Interchange Sort & Quick Sort)</h2>
    <p><span class="badge badge-uit-convention">IT003 CONVENTION</span>: <strong>Interchange Sort</strong> so sánh phần tử $a[i]$ lần lượt với các phần tử $a[j]$ ($j > i$), hễ $a[i] > a[j]$ là đổi chỗ ngay lập tức.</p>

    <h2>5. C++ Educational & STL Code</h2>
    <pre><code>// Interchange Sort (Đặc thù UIT)
void interchangeSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] > a[j]) {
                std::swap(a[i], a[j]);
            }
        }
    }
}

// Quick Sort với phân hoạch Lomuto
int partitionLomuto(int a[], int low, int high) {
    int pivot = a[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (a[j] < pivot) {
            i++;
            std::swap(a[i], a[j]);
        }
    }
    std::swap(a[i + 1], a[high]);
    return i + 1;
}

void quickSort(int a[], int low, int high) {
    if (low < high) {
        int pi = partitionLomuto(a, low, high);
        quickSort(a, low, pi - 1);
        quickSort(a, pi + 1, high);
    }
}</code></pre>

    <h2>6. Complexity Analysis & Invariants</h2>
    <p><strong>Số phép toán Interchange Sort:</strong> Phép so sánh $C = \frac{n(n-1)}{2}$ luôn cố định. Số phép gán/đổi chỗ $M$: Best $M=0$, Worst $M = 3 \cdot \frac{n(n-1)}{2}$.</p>

    <h2>7. Dry Run Table (Chạy tay Quick Sort ví dụ)</h2>
    <p>Mảng đầu vào $A = [25, 12, 40, 8, 30]$ ($n=5$), Pivot $a[high] = 30$:</p>
    <table>
        <thead>
            <tr><th>Bước j</th><th>a[j]</th><th>So sánh với Pivot=30</th><th>i</th><th>Mảng sau khi xử lý</th></tr>
        </thead>
        <tbody>
            <tr><td>0 (val 25)</td><td>25</td><td>$25 < 30$ (Đúng)</td><td>0</td><td>Swap(a[0], a[0]) $\rightarrow [25, 12, 40, 8, 30]$</td></tr>
            <tr><td>1 (val 12)</td><td>12</td><td>$12 < 30$ (Đúng)</td><td>1</td><td>Swap(a[1], a[1]) $\rightarrow [25, 12, 40, 8, 30]$</td></tr>
            <tr><td>2 (val 40)</td><td>40</td><td>$40 > 30$ (Sai)</td><td>1</td><td>Không swap $\rightarrow [25, 12, 40, 8, 30]$</td></tr>
            <tr><td>3 (val 8)</td><td>8</td><td>$8 < 30$ (Đúng)</td><td>2</td><td>Swap(a[2], a[3]) $\rightarrow [25, 12, 8, 40, 30]$</td></tr>
            <tr><td>Kết thúc</td><td>-</td><td>Swap pivot về đúng vị trí</td><td>2</td><td>Swap(a[3], a[4]) $\rightarrow \mathbf{[25, 12, 8, 30, 40]}$</td></tr>
        </tbody>
    </table>

    <h2>8. Common Errors & IT003 Exam Style</h2>
    <div class="callout callout-warning">
        <span class="badge badge-exam-style">IT003 EXAM STYLE</span>
        <p><strong>Bẫy Đề Thi:</strong> Phân biệt Tính Ổn định (Stability) và Tính Tại chỗ (In-place). Quick Sort là **In-place** nhưng **Không ổn định**. Merge Sort **Ổn định** nhưng **Không In-place** ($\mathcal{O}(n)$ bộ nhớ phụ).</p>
    </div>

    <h2>9. Quick Recall & Exercise Ladder</h2>
    <ul>
        <li><strong>Level 0:</strong> Thuật toán nào có số phép so sánh $C = \frac{n(n-1)}{2}$ cố định trong mọi trường hợp?
            <br><em>Đáp án:</em> Selection Sort và Interchange Sort.
        </li>
        <li><strong>Level 1:</strong> Thực hiện chạy tay 2 lượt đầu tiên của Bubble Sort trên mảng $A = [5, 1, 4, 2, 8]$.
            <br><em>Gợi ý:</em> Lượt 1: $[1, 4, 2, 5, 8]$. Lượt 2: $[1, 2, 4, 5, 8]$.
        </li>
    </ul>

    <div class="callout">
        <div class="callout-title">📝 Tóm kết Chương 3</div>
        <p>Nắm vững bảng ma trận độ phức tạp 10 thuật toán sắp xếp và kỹ năng chạy tay từng lượt để đạt điểm tối đa câu 1 trong đề thi IT003!</p>
    </div>
</section>"""
    with open(os.path.join(CHAPTERS_DIR, "03_SORTING.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated 03_SORTING.html")

def main():
    write_ch02()
    write_ch03()

if __name__ == "__main__":
    main()
