import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

BASE_DIR = r"C:\Users\lyle3\.gemini\antigravity\scratch\IT003_DSA_BOOK"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
os.makedirs(CHAPTERS_DIR, exist_ok=True)

def write_ch07():
    html = """<section class="chapter" id="ch07">
    <div class="chapter-header">
        <span class="badge badge-core">PART VII</span>
        <h1>CÂY NHỊ PHÂN TÌM KIẾM (BINARY SEARCH TREE - BST)</h1>
    </div>

    <h2>1. Intuition (Trực giác & Động lực)</h2>
    <p>Mảng sắp xếp cho phép Tìm kiếm Nhị phân $\mathcal{O}(\log n)$ nhưng chèn/xóa tốn $\mathcal{O}(n)$. Danh sách liên kết cho phép chèn/xóa $\mathcal{O}(1)$ nhưng tìm kiếm tốn $\mathcal{O}(n)$. **Binary Search Tree (BST)** kết hợp ưu điểm của cả hai: cho phép Tìm kiếm, Chèn, Xóa đều đạt trung bình $\mathcal{O}(\log n)$!</p>

    <h2>2. Formal Model & Invariants (Định nghĩa & Bất biến)</h2>
    <p>BST là cây nhị phân thỏa mãn tính chất bất biến tại mọi nút $X$:</p>
    <ul>
        <li>Mọi khóa ở cây con trái của $X$ đều **nhỏ hơn** khóa của $X$ ($\text{key}(Left) < \text{key}(X)$).</li>
        <li>Mọi khóa ở cây con phải của $X$ đều **lớn hơn** khóa của $X$ ($\text{key}(Right) > \text{key}(X)$).</li>
    </ul>

    <h2>3. Visual Diagram (Sơ đồ Xóa Nút BST 2 Con)</h2>
    <div class="diagram-container">
        <svg width="550" height="150" viewBox="0 0 550 150" xmlns="http://www.w3.org/2000/svg">
            <rect width="550" height="150" fill="#f8fafc" rx="8"/>
            <g transform="translate(100, 30)">
                <circle cx="0" cy="0" r="18" fill="#b91c1c"/>
                <text x="0" y="5" fill="#ffffff" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">50</text>
                <text x="0" y="32" font-family="Inter" font-size="10" fill="#b91c1c">Cần xóa</text>
            </g>
            <path d="M 140 30 L 220 30" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>
            <g transform="translate(300, 30)">
                <circle cx="0" cy="0" r="18" fill="#15803d"/>
                <text x="0" y="5" fill="#ffffff" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">55</text>
                <text x="0" y="32" font-family="Inter" font-size="10" fill="#15803d">Thế mạng (Min Right)</text>
            </g>
        </svg>
    </div>

    <h2>4. Algorithm & Mechanics (3 Trường hợp Xóa Nút)</h2>
    <ol>
        <li><strong>Nút lá:</strong> Xóa trực tiếp nút và cho con trỏ từ cha trỏ về `nullptr`.</li>
        <li><strong>Nút có 1 con:</strong> Nối con trỏ từ cha của nút cần xóa trực tiếp tới nút con duy nhất của nó, sau đó giải phóng bộ nhớ.</li>
        <li><strong>Nút có 2 con:</strong> <span class="badge badge-uit-convention">IT003 CONVENTION</span>
            <br>• Option A: Thay bằng **Nút cực phải của cây con trái (Max Left)**.
            <br>• Option B: Thay bằng **Nút cực trái của cây con phải (Min Right)**.
        </li>
    </ol>

    <h2>5. C++ Educational Implementation</h2>
    <pre><code>TreeNode* findMin(TreeNode* root) {
    while (root->pLeft != nullptr) root = root->pLeft;
    return root;
}

TreeNode* deleteNode(TreeNode* root, int key) {
    if (root == nullptr) return root;

    if (key < root->data) root->pLeft = deleteNode(root->pLeft, key);
    else if (key > root->data) root->pRight = deleteNode(root->pRight, key);
    else {
        if (root->pLeft == nullptr) {
            TreeNode* temp = root->pRight;
            delete root; return temp;
        } else if (root->pRight == nullptr) {
            TreeNode* temp = root->pLeft;
            delete root; return temp;
        }
        TreeNode* temp = findMin(root->pRight); // Min Right
        root->data = temp->data;
        root->pRight = deleteNode(root->pRight, temp->data);
    }
    return root;
}</code></pre>

    <h2>6. Complexity Analysis</h2>
    <ul>
        <li><strong>Cây cân bằng tương đối:</strong> Tìm kiếm / Chèn / Xóa tốn $\Theta(\log n)$ thời gian.</li>
        <li><strong>Cây suy biến (Skewed Tree):</strong> Trở thành DSLK, thời gian tệ nhất tốn $\Theta(n)$.</li>
    </ul>

    <h2>7. Dry Run Table (Trace Xóa Nút có 2 con)</h2>
    <table>
        <thead>
            <tr><th>Bước</th><th>Hành động</th><th>Trạng thái Nút 50</th><th>Nút thế mạng Min Right</th></tr>
        </thead>
        <tbody>
            <tr><td>1</td><td>Tìm nút 50</td><td>Xác định có 2 con (Left 30, Right 70)</td><td>-</td></tr>
            <tr><td>2</td><td>Tìm Min Right trên cây con 70</td><td>-</td><td>Tìm thấy Nút 55</td></tr>
            <tr><td>3</td><td>Gán `root->data = 55`</td><td>Dữ liệu đổi thành 55</td><td>-</td></tr>
            <tr><td>4</td><td>Đệ quy xóa 55 trên cây con phải</td><td>Nút 50 cũ giữ giá trị 55</td><td>Xóa nút 55 ban đầu</td></tr>
        </tbody>
    </table>

    <h2>8. Common Errors & IT003 Exam Style</h2>
    <div class="callout callout-warning">
        <span class="badge badge-exam-style">IT003 EXAM STYLE</span>
        <p><strong>Bẫy Đề Thi:</strong> Luôn đọc kỹ yêu cầu bài thi: "Thay bằng phần tử lớn nhất bên cây con trái" (Max Left) hay "nhỏ nhất bên cây con phải" (Min Right). Chọn sai phần tử thế mạng sẽ bị trừ điểm toàn bộ cây kết quả!</p>
    </div>

    <h2>9. Quick Recall & Exercise Ladder</h2>
    <ul>
        <li><strong>Level 0:</strong> BST bị suy biến thành danh sách tuyến tính khi nào?
            <br><em>Đáp án:</em> Khi chèn các phần tử theo thứ tự đã sắp xếp tăng dần hoặc giảm dần.
        </li>
        <li><strong>Level 1:</strong> Vẽ BST kết quả sau khi chèn dãy khóa: $50, 30, 70, 20, 40, 60, 80$.
            <br><em>Gợi ý:</em> 50 là Root. 30 bên trái 50, 70 bên phải 50, ... thu được cây cân bằng hoàn hảo.
        </li>
    </ul>

    <div class="callout">
        <div class="callout-title">📝 Tóm kết Chương 7</div>
        <p>BST là nền tảng quan trọng nhất của cấu trúc cây tìm kiếm. Hãy luyện tập thành thạo thao tác xóa nút 2 con trên giấy!</p>
    </div>
</section>"""
    with open(os.path.join(CHAPTERS_DIR, "07_BST.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated 07_BST.html")

def write_ch08():
    html = """<section class="chapter" id="ch08">
    <div class="chapter-header">
        <span class="badge badge-core">PART VIII</span>
        <h1>CÂY CÂN BẰNG AVL (AVL TREES)</h1>
    </div>

    <h2>1. Intuition (Trực giác & Động lực)</h2>
    <p>Để khắc phục nhược điểm bị suy biến thành $\mathcal{O}(n)$ của BST thông thường, Adelson-Velsky và Landis (AVL) đã đề xuất cây BST tự cân bằng: tự động thực hiện phép **Xoay (Rotation)** mỗi khi độ lệch chiều cao giữa 2 cây con vượt quá 1.</p>

    <h2>2. Formal Model & Balance Factor</h2>
    <p>Chỉ số cân bằng của nút $X$:</p>
    $$BF(X) = h_{left} - h_{right}$$
    <p>Điều kiện AVL: $BF(X) \in \{-1, 0, +1\}$ với mọi nút $X$. Nếu $|BF(X)| \ge 2$, cây bị mất cân bằng tại $X$.</p>

    <h2>3. Visual Diagram (Ma trận 4 Phép Xoay AVL Matrix)</h2>
    <div class="callout">
        <div class="callout-title">🔄 Rotation Cheat Sheet Table</div>
        <table>
            <thead>
                <tr><th>Trường hợp</th><th>$BF(A)$ và $BF(Child)$</th><th>Phép Xoay Khôi Phục</th></tr>
            </thead>
            <tbody>
                <tr><td><strong>LL (Left-Left)</strong></td><td>$BF(A) = +2$, $BF(Left) \ge 0$</td><td><strong>Xoay Đơn Phải (Rotate Right) tại A</strong></td></tr>
                <tr><td><strong>RR (Right-Right)</strong></td><td>$BF(A) = -2$, $BF(Right) \le 0$</td><td><strong>Xoay Đơn Trái (Rotate Left) tại A</strong></td></tr>
                <tr><td><strong>LR (Left-Right)</strong></td><td>$BF(A) = +2$, $BF(Left) = -1$</td><td><strong>Xoay Kép LR</strong> (Rotate Left tại Left, rồi Rotate Right tại A)</td></tr>
                <tr><td><strong>RL (Right-Left)</strong></td><td>$BF(A) = -2$, $BF(Right) = +1$</td><td><strong>Xoay Kép RL</strong> (Rotate Right tại Right, rồi Rotate Left tại A)</td></tr>
            </tbody>
        </table>
    </div>

    <h2>4. Algorithm & Mechanics (Xoay Đơn Phải Rotate Right)</h2>
    <p>Cho nút $Y$ bị mất cân bằng nghiêng trái ($BF = +2$), nút con trái là $X$. Phép xoay phải đưa $X$ lên làm cha $Y$, và chuyển cây con phải của $X$ ($T_2$) sang làm cây con trái của $Y$.</p>

    <h2>5. C++ Educational Implementation</h2>
    <pre><code>int getHeight(TreeNode* n) { return n == nullptr ? 0 : n->height; }
int getBalance(TreeNode* n) { return n == nullptr ? 0 : getHeight(n->pLeft) - getHeight(n->pRight); }

TreeNode* rotateRight(TreeNode* y) {
    TreeNode* x = y->pLeft;
    TreeNode* T2 = x->pRight;
    x->pRight = y;
    y->pLeft = T2;
    y->height = std::max(getHeight(y->pLeft), getHeight(y->pRight)) + 1;
    x->height = std::max(getHeight(x->pLeft), getHeight(x->pRight)) + 1;
    return x;
}</code></pre>

    <h2>6. Complexity Analysis</h2>
    <p>Cây AVL đảm bảo chiều cao $h \le 1.44 \log_2 n$. Do đó các thao tác Tìm kiếm, Chèn, Xóa **luôn luôn đạt $\Theta(\log n)$ trong mọi trường hợp**.</p>

    <h2>7. Dry Run Table (Trace Chèn Khóa gây Mất Cân Bằng)</h2>
    <p>Chèn $30, 20, 10$ vào cây AVL rỗng:</p>
    <table>
        <thead>
            <tr><th>Khóa chèn</th><th>Trạng thái cây trước xoay</th><th>Chỉ số $BF(Root)$</th><th>Xử lý xoay</th><th>Cây sau xoay</th></tr>
        </thead>
        <tbody>
            <tr><td>30, 20</td><td>30 $\rightarrow$ Left: 20</td><td>$BF(30) = +1$</td><td>Cân bằng, không xoay</td><td>30 $\rightarrow$ L:20</td></tr>
            <tr><td>10</td><td>30 $\rightarrow$ L:20 $\rightarrow$ L:10</td><td>$BF(30) = +2, BF(20) = +1$</td><td>Mất cân bằng LL $\rightarrow$ Xoay Phải 30</td><td>Root: 20, Left: 10, Right: 30</td></tr>
        </tbody>
    </table>

    <h2>8. Common Errors & IT003 Exam Style</h2>
    <div class="callout callout-warning">
        <span class="badge badge-exam-style">IT003 EXAM STYLE</span>
        <p><strong>Bẫy Đề Thi:</strong> Nhầm lẫn giữa xoay đơn và xoay kép. Dấu hiệu xoay kép LR: $BF(A) = +2$ nhưng con trái lại có $BF = -1$. Phải xoay trái con trái trước, sau đó mới xoay phải A!</p>
    </div>

    <h2>9. Quick Recall & Exercise Ladder</h2>
    <ul>
        <li><strong>Level 0:</strong> Chiều cao cây con trái là 3, cây con phải là 1. Chỉ số cân bằng $BF$ của gốc là bao nhiêu? Cây có đạt chuẩn AVL không?
            <br><em>Đáp án:</em> $BF = 3 - 1 = +2$. Cây không đạt chuẩn AVL (cần xoay).
        </li>
        <li><strong>Level 1:</strong> Chèn lần lượt các số $1, 2, 3$ vào cây AVL rỗng. Xác định loại xoay.
            <br><em>Gợi ý:</em> Mất cân bằng RR tại nút 1 $\rightarrow$ Xoay Trái nút 1.
        </li>
    </ul>

    <div class="callout">
        <div class="callout-title">📝 Tóm kết Chương 8</div>
        <p>Cây AVL duy trì sự cân bằng nghiêm ngặt nhờ 4 phép xoay chuẩn (LL, RR, LR, RL), đảm bảo thời gian truy xuất lý tưởng $\mathcal{O}(\log n)$.</p>
    </div>
</section>"""
    with open(os.path.join(CHAPTERS_DIR, "08_AVL.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated 08_AVL.html")

def write_ch09():
    html = """<section class="chapter" id="ch09">
    <div class="chapter-header">
        <span class="badge badge-core">PART IX</span>
        <h1>HEAPS VÀ HÀNG ĐỢI ƯU TIÊN (HEAP & PRIORITY QUEUE)</h1>
    </div>

    <h2>1. Intuition (Trực giác & Động lực)</h2>
    <p>Hàng đợi ưu tiên (Priority Queue) là hàng đợi mà phần tử có độ ưu tiên cao nhất luôn được phục vụ trước. Cấu trúc dữ liệu Heap biểu diễn hoàn hảo hàng đợi ưu tiên nhờ khả năng tìm phần tử cực đại/cực tiểu trong $\mathcal{O}(1)$ và cập nhật lại cây trong $\mathcal{O}(\log n)$.</p>

    <h2>2. Formal Model & Invariants</h2>
    <p><strong>Max-Heap</strong> là Cây nhị phân hoàn chỉnh (Complete Binary Tree) thỏa mãn bất biến: Khóa của nút cha luôn $\ge$ khóa của các nút con.</p>

    <h2>3. Visual Diagram (Biểu diễn Heap bằng Mảng)</h2>
    <div class="diagram-container">
        <svg width="550" height="130" viewBox="0 0 550 130" xmlns="http://www.w3.org/2000/svg">
            <rect width="550" height="130" fill="#f8fafc" rx="8"/>
            <g transform="translate(50, 40)">
                <rect x="0" y="0" width="45" height="40" fill="#0f172a" rx="4"/>
                <text x="22" y="25" fill="#ffffff" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">90</text>
                <text x="22" y="55" font-family="Inter" font-size="10" fill="#64748b" text-anchor="middle">0 (Root)</text>
                <rect x="45" y="0" width="45" height="40" fill="#1e40af" rx="4"/>
                <text x="67" y="25" fill="#ffffff" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">75</text>
                <text x="67" y="55" font-family="Inter" font-size="10" fill="#64748b" text-anchor="middle">1 (Left)</text>
                <rect x="90" y="0" width="45" height="40" fill="#1e40af" rx="4"/>
                <text x="112" y="25" fill="#ffffff" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">60</text>
                <text x="112" y="55" font-family="Inter" font-size="10" fill="#64748b" text-anchor="middle">2 (Right)</text>
            </g>
        </svg>
    </div>

    <h2>4. Algorithm & Mechanics (Công thức Chỉ số Mảng)</h2>
    <p><span class="badge badge-uit-convention">IT003 CONVENTION</span>: Với mảng bắt đầu từ index `0`:</p>
    <ul>
        <li>$\text{parent}(i) = \lfloor (i - 1) / 2 \rfloor$</li>
        <li>$\text{left}(i) = 2i + 1$</li>
        <li>$\text{right}(i) = 2i + 2$</li>
    </ul>

    <h2>5. C++ Educational & STL Implementation</h2>
    <pre><code>void heapify(int a[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1, right = 2 * i + 2;
    if (left < n && a[left] > a[largest]) largest = left;
    if (right < n && a[right] > a[largest]) largest = right;
    if (largest != i) {
        std::swap(a[i], a[largest]);
        heapify(a, n, largest);
    }
}

// C++ STL Priority Queue
#include <queue>
void stlPriorityQueue() {
    std::priority_queue<int> maxHeap; // Max Heap mặc định
    maxHeap.push(50); maxHeap.push(80);
    int topVal = maxHeap.top(); // 80
}</code></pre>

    <h2>6. Complexity Analysis</h2>
    <p>Tìm Max: $\Theta(1)$. Chèn / Xóa Max (Heapify): $\Theta(\log n)$. Thuật toán `buildHeap` tạo Heap từ mảng ngẫu nhiên đạt độ phức tạp tuyến tính **$\Theta(n)$**. Heap Sort đạt $\Theta(n \log n)$.</p>

    <h2>7. Dry Run Table (Trace Heapify tại Nút 0)</h2>
    <p>Mảng $A = [10, 50, 40]$, $n=3$, gọi Heapify(A, 3, 0):</p>
    <table>
        <thead>
            <tr><th>Bước</th><th>i</th><th>Largest ban đầu</th><th>Left (a[1]=50)</th><th>Right (a[2]=40)</th><th>Largest sau so sánh</th><th>Hành động</th></tr>
        </thead>
        <tbody>
            <tr><td>1</td><td>0 (val 10)</td><td>0</td><td>50 > 10 $\rightarrow$ largest=1</td><td>40 < 50 $\rightarrow$ largest=1</td><td>1 (val 50)</td><td>Swap(a[0], a[1]) $\rightarrow [50, 10, 40]$</td></tr>
        </tbody>
    </table>

    <h2>8. Common Errors & IT003 Exam Style</h2>
    <div class="callout callout-warning">
        <span class="badge badge-exam-style">IT003 EXAM STYLE</span>
        <p><strong>Bẫy Đề Thi:</strong> Cây nhị phân hoàn chỉnh phải được điền đầy từ trái sang phải ở mức cuối cùng. Đừng nhầm lẫn giữa Max-Heap và Cây BST!</p>
    </div>

    <h2>9. Quick Recall & Exercise Ladder</h2>
    <ul>
        <li><strong>Level 0:</strong> Trong Max-Heap dạng mảng, nút tại vị trí index 3 có nút con trái ở index bao nhiêu?
            <br><em>Đáp án:</em> Index $2(3) + 1 = 7$.
        </li>
        <li><strong>Level 1:</strong> Cho mảng $A = [4, 10, 3, 5, 1]$. Chạy tay `buildHeap` để biến $A$ thành Max-Heap.
            <br><em>Gợi ý:</em> Gọi Heapify từ vị trí $i = \lfloor n/2 \rfloor - 1 = 1 \rightarrow A = [10, 5, 3, 4, 1]$.
        </li>
    </ul>

    <div class="callout">
        <div class="callout-title">📝 Tóm kết Chương 9</div>
        <p>Heap cung cấp cấu trúc ưu tiên hiệu quả nhất với chi phí $\mathcal{O}(\log n)$ cho thao tác cập nhật và $\mathcal{O}(1)$ cho thao tác xem phần tử ưu tiên nhất.</p>
    </div>
</section>"""
    with open(os.path.join(CHAPTERS_DIR, "09_HEAP_PRIORITY_QUEUE.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated 09_HEAP_PRIORITY_QUEUE.html")

def write_ch10():
    html = """<section class="chapter" id="ch10">
    <div class="chapter-header">
        <span class="badge badge-core">PART X</span>
        <h1>CÂY B-TREE (B-TREES - MULTI-WAY SEARCH TREES)</h1>
    </div>

    <h2>1. Intuition (Trực giác & Động lực)</h2>
    <p>Khi dữ liệu quá lớn không thể chứa hết trong RAM mà phải lưu trên đĩa cứng (Hard Drive / SSD), mỗi lần đọc đĩa (Disk I/O) tốn thời gian rất lớn. **B-Tree (Cây tìm kiếm đa đường)** làm giảm chiều cao của cây bằng cách cho phép mỗi nút chứa nhiều khóa và nhiều con, tối ưu hóa tối đa số lần đọc đĩa.</p>

    <h2>2. Formal Model & Rules (Quy tắc B-Tree Bậc $m=5$)</h2>
    <p><span class="badge badge-uit-convention">IT003 CONVENTION</span>: Đề thi IT003 cực kỳ tập trung vào **B-Tree bậc 5 ($m=5$)**:</p>
    <ul>
        <li>Số khóa tối đa trong 1 nút: $m - 1 = 4$ khóa.</li>
        <li>Số con tối đa của 1 nút: $m = 5$ con.</li>
        <li>Số khóa tối thiểu (nút không phải gốc): $\lceil m/2 \rceil - 1 = \lceil 2.5 \rceil - 1 = 2$ khóa.</li>
        <li>Số con tối thiểu (nút không phải gốc): $\lceil m/2 \rceil = 3$ con.</li>
        <li>Tất cả các nút lá đều nằm trên **cùng một mức**.</li>
    </ul>

    <h2>3. Visual Diagram (Sơ đồ Tách Nút B-Tree Bậc 5)</h2>
    <div class="diagram-container">
        <svg width="600" height="140" viewBox="0 0 600 140" xmlns="http://www.w3.org/2000/svg">
            <rect width="600" height="140" fill="#f8fafc" rx="8"/>
            <g transform="translate(30, 40)">
                <!-- Full Node -->
                <rect x="0" y="0" width="180" height="40" fill="#fee2e2" stroke="#b91c1c" stroke-width="2"/>
                <text x="90" y="25" fill="#b91c1c" font-family="Inter" font-size="11" font-weight="bold" text-anchor="middle">[10, 20, 30, 40, 50] (Overflow)</text>
            </g>
            <path d="M 230 60 L 310 60" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>
            <g transform="translate(330, 20)">
                <!-- Promoted Key -->
                <rect x="70" y="0" width="50" height="35" fill="#3b82f6" stroke="#1e40af" stroke-width="2"/>
                <text x="95" y="22" fill="#ffffff" font-family="Inter" font-size="11" font-weight="bold" text-anchor="middle">30 (Root)</text>
                <!-- Left & Right Children -->
                <rect x="0" y="55" width="80" height="35" fill="#dcfce7" stroke="#15803d" stroke-width="2"/>
                <text x="40" y="77" fill="#15803d" font-family="Inter" font-size="11" font-weight="bold" text-anchor="middle">[10, 20]</text>
                <rect x="110" y="55" width="80" height="35" fill="#dcfce7" stroke="#15803d" stroke-width="2"/>
                <text x="150" y="77" fill="#15803d" font-family="Inter" font-size="11" font-weight="bold" text-anchor="middle">[40, 50]</text>
            </g>
        </svg>
    </div>

    <h2>4. Algorithm & Mechanics (Tách Nút Split & Promote)</h2>
    <p>Khi chèn vào nút đã có 4 khóa làm xuất hiện khóa thứ 5 ($[k_1, k_2, k_3, k_4, k_5]$): Khóa trung vị $k_3$ được **đẩy nổi (Promote)** lên nút cha. Nút bị **Tách (Split)** thành 2 nút con chứa $[k_1, k_2]$ và $[k_4, k_5]$.</p>

    <h2>5. C++ Pseudocode Representative Structure</h2>
    <pre><code>const int M = 5; // B-Tree Order 5
struct BTreeNode {
    int keys[M - 1]; // Tối đa 4 khóa
    BTreeNode* child[M]; // Tối đa 5 con
    int numKeys;
    bool isLeaf;
};</code></pre>

    <h2>6. Complexity Analysis</h2>
    <p>Thời gian Tìm kiếm, Chèn, Xóa trên B-Tree luôn đạt **$\Theta(\log_m n)$**, giúp giảm số lần đọc đĩa xuống mức tối thiểu.</p>

    <h2>7. Dry Run Table (Trace Chèn Khóa vào B-Tree bậc 5)</h2>
    <p>Chèn $10, 20, 30, 40, 50$ vào B-Tree bậc 5 rỗng:</p>
    <table>
        <thead>
            <tr><th>Khóa chèn</th><th>Trạng thái Nút lá</th><th>Hiện tượng</th><th>Hành động Tách & Đẩy nổi</th></tr>
        </thead>
        <tbody>
            <tr><td>10, 20, 30, 40</td><td>[10, 20, 30, 40]</td><td>Đủ 4 khóa (Bình thường)</td><td>Chưa tách</td></tr>
            <tr><td>50</td><td>[10, 20, 30, 40, 50]</td><td>Tràn (5 khóa)</td><td>Đẩy nổi 30 lên Root. Tách thành 2 con: [10, 20] và [40, 50]</td></tr>
        </tbody>
    </table>

    <h2>8. Common Errors & IT003 Exam Style</h2>
    <div class="callout callout-warning">
        <span class="badge badge-exam-style">IT003 EXAM STYLE</span>
        <p><strong>Bẫy Đề Thi:</strong> Khi tách nút có 5 khóa trong B-Tree bậc 5, khóa ở giữa (vị trí thứ 3) được đưa lên cha. Đừng nhầm lẫn vị trí khóa được đẩy nổi!</p>
    </div>

    <h2>9. Quick Recall & Exercise Ladder</h2>
    <ul>
        <li><strong>Level 0:</strong> B-Tree bậc 5 chứa tối đa bao nhiêu khóa trong 1 nút? Nút không phải gốc chứa tối thiểu bao nhiêu khóa?
            <br><em>Đáp án:</em> Tối đa $m-1 = 4$ khóa. Tối thiểu $\lceil 5/2 \rceil - 1 = 2$ khóa.
        </li>
        <li><strong>Level 1:</strong> Vẽ B-Tree bậc 5 sau khi chèn các số $5, 15, 25, 35, 45, 55$.
            <br><em>Gợi ý:</em> Sau khi chèn 45, nút tràn $[5, 15, 25, 35, 45] \rightarrow$ Đẩy 25 lên gốc. Sau đó chèn 55 vào nút phải $[35, 45, 55]$.
        </li>
    </ul>

    <div class="callout">
        <div class="callout-title">📝 Tóm kết Chương 10</div>
        <p>B-Tree bậc 5 quy định chặt chẽ số khóa từ 2 đến 4 khóa per node. Quy tắc Split đẩy nổi khóa thứ 3 là tâm điểm các câu hỏi B-Tree trong đề thi IT003.</p>
    </div>
</section>"""
    with open(os.path.join(CHAPTERS_DIR, "10_BTREE.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated 10_BTREE.html")

def write_ch11():
    html = """<section class="chapter" id="ch11">
    <div class="chapter-header">
        <span class="badge badge-core">PART XI</span>
        <h1>BẢNG BĂM (HASH TABLE)</h1>
    </div>

    <h2>1. Intuition (Trực giác & Động lực)</h2>
    <p>Bạn có muốn tìm kiếm dữ liệu trong thời gian tức thì $\mathcal{O}(1)$ không? Bảng băm (Hash Table) biến khóa $k$ thành chỉ số mảng thông qua **Hàm Băm (Hash Function)**, cho phép truy xuất dữ liệu gần như ngay lập tức.</p>

    <h2>2. Formal Model & Collision Resolution</h2>
    <p>Hàm bămModulo: $h(k) = k \bmod M$ ($M$ là kích thước bảng băm). Đụng độ (Collision) xảy ra khi 2 khóa khác nhau có cùng giá trị băm. Các phương pháp giải quyết đụng độ chuẩn IT003:</p>

    <ul>
        <li><strong>Linear Probing (Dò tuyến tính):</strong> $h(k, i) = (h(k) + i) \bmod M$</li>
        <li><strong>Quadratic Probing (Dò bậc hai):</strong> $h(k, i) = (h(k) + i^2) \bmod M$</li>
        <li><strong>Double Hashing (Băm kép):</strong> $h(k, i) = (h_1(k) + i \cdot h_2(k)) \bmod M$ với $h_2(k) = R - (k \bmod R)$</li>
        <li><strong>Separate Chaining:</strong> Lưu mỗi ô bằng một Danh sách liên kết đơn.</li>
    </ul>

    <h2>3. Visual Diagram (Sơ đồ Dò Tuyến Tính Hash Probing)</h2>
    <div class="diagram-container">
        <svg width="550" height="120" viewBox="0 0 550 120" xmlns="http://www.w3.org/2000/svg">
            <rect width="550" height="120" fill="#f8fafc" rx="8"/>
            <g transform="translate(40, 35)">
                <rect x="0" y="0" width="40" height="40" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
                <text x="20" y="25" font-family="Inter" font-size="11" font-weight="bold" text-anchor="middle">10</text>
                <text x="20" y="55" font-family="Inter" font-size="10" fill="#64748b" text-anchor="middle">0</text>
                <rect x="40" y="0" width="40" height="40" fill="#fee2e2" stroke="#b91c1c" stroke-width="2"/>
                <text x="60" y="25" fill="#b91c1c" font-family="Inter" font-size="11" font-weight="bold" text-anchor="middle">21</text>
                <text x="60" y="55" font-family="Inter" font-size="10" fill="#64748b" text-anchor="middle">1 (Collision)</text>
                <rect x="80" y="0" width="40" height="40" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
                <text x="100" y="25" font-family="Inter" font-size="11" font-weight="bold" text-anchor="middle">EMPTY</text>
                <text x="100" y="55" font-family="Inter" font-size="10" fill="#64748b" text-anchor="middle">2</text>
            </g>
        </svg>
    </div>

    <h2>4. Algorithm & Mechanics (Đếm So Sánh $C_{\text{succ}}$ và $C_{\text{unsucc}}$)</h2>
    <p><span class="badge badge-uit-convention">IT003 CONVENTION</span>:</p>
    <ul>
        <li><strong>Tìm kiếm Thành công ($C_{\text{succ}}$):</strong> Trung bình số phép so sánh để tìm thấy các khóa đang có trong bảng.</li>
        <li><strong>Tìm kiếm Thất bại ($C_{\text{unsucc}}$):</strong> Trung bình số phép so sánh từ mỗi ô $i \in [0, M-1]$ cho đến khi **gặp ô trống (`EMPTY`) đầu tiên**. Ô bị xóa (`DELETED`) **không được dừng**!</li>
    </ul>

    <h2>5. C++ Educational & STL Code</h2>
    <pre><code>#include <unordered_map>
#include <iostream>

void stlHashTable() {
    std::unordered_map<std::string, int> hashMap;
    hashMap["UIT"] = 100;
    if (hashMap.find("UIT") != hashMap.end()) {
        std::cout << "Found: " << hashMap["UIT"] << "\n";
    }
}</code></pre>

    <h2>6. Complexity Analysis</h2>
    <p>Trung bình: Tìm kiếm / Chèn / Xóa tốn **$\Theta(1)$ thời gian**. Trường hợp tệ nhất (tất cả các khóa bị đụng độ về 1 ô): $\Theta(n)$.</p>

    <h2>7. Dry Run Table (Trace Dò Tuyến Tính $h(k) = k \bmod 7$)</h2>
    <p>Chèn lần lượt các khóa $14, 21, 7$ vào bảng băm $M=7$ rỗng dùng Linear Probing:</p>
    <table>
        <thead>
            <tr><th>Khóa k</th><th>h(k) = k % 7</th><th>Vị trí ô chèn</th><th>Số lần so sánh (Probes)</th><th>Trạng thái bảng băm [0..6]</th></tr>
        </thead>
        <tbody>
            <tr><td>14</td><td>0</td><td>0 (Trống)</td><td>1</td><td>[14, -, -, -, -, -, -]</td></tr>
            <tr><td>21</td><td>0</td><td>0 (Trùng) $\rightarrow$ ô 1 (Trống)</td><td>2</td><td>[14, 21, -, -, -, -, -]</td></tr>
            <tr><td>7</td><td>0</td><td>0, 1 (Trùng) $\rightarrow$ ô 2 (Trống)</td><td>3</td><td>[14, 21, 7, -, -, -, -]</td></tr>
        </tbody>
    </table>

    <h2>8. Common Errors & IT003 Exam Style</h2>
    <div class="callout callout-warning">
        <span class="badge badge-exam-style">IT003 EXAM STYLE</span>
        <p><strong>Bẫy Đề Thi:</strong> Tính số phép so sánh tìm kiếm thất bại $C_{\text{unsucc}}$. Phải duyệt từ từng ô index $0, 1, \dots, M-1$ đếm số bước tới khi gặp ô trống `EMPTY` đầu tiên, sau đó cộng lại chia cho $M$!</p>
    </div>

    <h2>9. Quick Recall & Exercise Ladder</h2>
    <ul>
        <li><strong>Level 0:</strong> Trong Linear Probing, khi xóa một phần tử, tại sao ta không được gán ô đó thành `EMPTY` mà phải gán thành `DELETED`?
            <br><em>Đáp án:</em> Để không ngắt đoạn chuỗi dò của các phần tử đụng độ được chèn sau đó.
        </li>
        <li><strong>Level 1:</strong> Cho $M=5, h(k) = k \bmod 5$. Chèn $5, 10, 15$ dùng Linear Probing. Tính $C_{\text{succ}}$ trung bình.
            <br><em>Gợi ý:</em> 5 (1 probe ô 0), 10 (2 probes ô 1), 15 (3 probes ô 2). $C_{\text{succ}} = (1+2+3)/3 = 2$ phép so sánh.
        </li>
    </ul>

    <div class="callout">
        <div class="callout-title">📝 Tóm kết Chương 11</div>
        <p>Bảng băm mang lại hiệu năng $\mathcal{O}(1)$ lý tưởng. Hãy chú ý kỹ quy tắc dừng khi tìm kiếm thất bại và công thức đếm probe!</p>
    </div>
</section>"""
    with open(os.path.join(CHAPTERS_DIR, "11_HASH_TABLE.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated 11_HASH_TABLE.html")

def write_ch12():
    html = """<section class="chapter" id="ch12">
    <div class="chapter-header">
        <span class="badge badge-core">PART XII</span>
        <h1>ĐỒ THỊ VÀ BIỂU DIỄN ĐỒ THỊ (GRAPHS & REPRESENTATIONS)</h1>
    </div>

    <h2>1. Intuition (Trực giác & Động lực)</h2>
    <p>Đồ thị (Graph) là mô hình tổng quát nhất biểu diễn các mối quan hệ liên kết: mạng xã hội (user là đỉnh, bạn bè là cạnh), bản đồ giao thông (giao lộ là đỉnh, đường đi là cạnh), hay mạng máy tính.</p>

    <h2>2. Formal Model & Definitions</h2>
    <p>Đồ thị $G = (V, E)$ gồm tập đỉnh $V$ ($|V| = n$) và tập cạnh $E$ ($|E| = m$). Đồ thị có thể là Vô hướng (Undirected) hoặc Có hướng (Directed), Có trọng số (Weighted) hoặc Không trọng số.</p>

    <h2>3. Visual Diagram (Ma trận Kề vs Danh sách Kề)</h2>
    <div class="diagram-container">
        <svg width="550" height="140" viewBox="0 0 550 140" xmlns="http://www.w3.org/2000/svg">
            <rect width="550" height="140" fill="#f8fafc" rx="8"/>
            <g transform="translate(40, 30)">
                <text x="0" y="15" font-family="Inter" font-size="11" font-weight="bold" fill="#0f172a">Ma trận Kề (Matrix):</text>
                <text x="0" y="40" font-family="Fira Code" font-size="10">A[u][v] = 1 nếu có cạnh (u,v)</text>
                <text x="0" y="60" font-family="Inter" font-size="10" fill="#64748b">Bộ nhớ: O(V²)</text>
            </g>
            <g transform="translate(300, 30)">
                <text x="0" y="15" font-family="Inter" font-size="11" font-weight="bold" fill="#0f172a">Danh sách Kề (List):</text>
                <text x="0" y="40" font-family="Fira Code" font-size="10">adj[u] = {v1, v2, ...}</text>
                <text x="0" y="60" font-family="Inter" font-size="10" fill="#64748b">Bộ nhớ: O(V + E)</text>
            </g>
        </svg>
    </div>

    <h2>4. Algorithm & Mechanics (Chuyển đổi Biểu diễn)</h2>
    <p>Chuyển đổi từ Ma trận kề $A[V][V]$ sang Danh sách kề: Duyệt qua từng hàng $i \in [0, V-1]$, nếu $A[i][j] \neq 0$ thì thêm $j$ vào danh sách `adj[i]`.</p>

    <h2>5. C++ Representations Code</h2>
    <pre><code>#include <vector>
#include <iostream>

// Representation via Adjacency List
void buildGraph(int V) {
    std::vector<std::vector<int>> adj(V);
    // Thêm cạnh vô hướng (0, 1)
    adj[0].push_back(1);
    adj[1].push_back(0);
}</code></pre>

    <h2>6. Complexity Analysis Comparison</h2>
    <table>
        <thead>
            <tr><th>Thao tác</th><th>Ma trận Kề (Adjacency Matrix)</th><th>Danh sách Kề (Adjacency List)</th></tr>
        </thead>
        <tbody>
            <tr><td>Bộ nhớ (Space)</td><td>$\Theta(V^2)$</td><td>$\Theta(V + E)$</td></tr>
            <tr><td>Kiểm tra cạnh $(u, v)$</td><td>$\Theta(1)$</td><td>$\mathcal{O}(\text{degree}(u))$</td></tr>
            <tr><td>Tìm tất cả đỉnh kề của $u$</td><td>$\Theta(V)$</td><td>$\Theta(\text{degree}(u))$</td></tr>
        </tbody>
    </table>

    <h2>7. Dry Run Table (Trace Ma trận Kề $\rightarrow$ Danh sách Kề)</h2>
    <p>Cho đồ thị 3 đỉnh {0, 1, 2} có Ma trận kề: row0=[0,1,1], row1=[1,0,0], row2=[1,0,0]:</p>
    <table>
        <thead>
            <tr><th>Đỉnh u</th><th>Các cột v có A[u][v] == 1</th><th>Danh sách kề adj[u]</th></tr>
        </thead>
        <tbody>
            <tr><td>0</td><td>1, 2</td><td>adj[0] = {1, 2}</td></tr>
            <tr><td>1</td><td>0</td><td>adj[1] = {0}</td></tr>
            <tr><td>2</td><td>0</td><td>adj[2] = {0}</td></tr>
        </tbody>
    </table>

    <h2>8. Common Errors & IT003 Exam Style</h2>
    <div class="callout callout-warning">
        <span class="badge badge-exam-style">IT003 EXAM STYLE</span>
        <p><strong>Bẫy Đề Thi:</strong> Phân biệt Đồ thị Có hướng và Vô hướng. Đồ thị Vô hướng có Ma trận kề đối xứng qua đường chéo chính ($A[i][j] = A[j][i]$). Tổng bậc các đỉnh bằng $2E$.</p>
    </div>

    <h2>9. Quick Recall & Exercise Ladder</h2>
    <ul>
        <li><strong>Level 0:</strong> Đồ thị thưa ($E \ll V^2$) nên biểu diễn bằng ma trận kề hay danh sách kề?
            <br><em>Đáp án:</em> Danh sách kề để tiết kiệm bộ nhớ ($\Theta(V+E)$ thay vì $\Theta(V^2)$).
        </li>
        <li><strong>Level 1:</strong> Tính tổng số bậc của tất cả các đỉnh trong đồ thị vô hướng có 5 đỉnh và 7 cạnh.
            <br><em>Gợi ý:</em> Tổng số bậc $= 2E = 2 \times 7 = 14$.
        </li>
    </ul>

    <div class="callout">
        <div class="callout-title">📝 Tóm kết Chương 12</div>
        <p>Hiểu rõ 2 cách biểu diễn Ma trận kề và Danh sách kề là nền tảng bắt buộc để cài đặt các thuật toán BFS, DFS và Dijkstra.</p>
    </div>
</section>"""
    with open(os.path.join(CHAPTERS_DIR, "12_GRAPH.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated 12_GRAPH.html")

def write_ch13():
    html = """<section class="chapter" id="ch13">
    <div class="chapter-header">
        <span class="badge badge-core">PART XIII</span>
        <h1>DUYỆT ĐỒ THỊ (BFS & DFS TRAVERSALS)</h1>
    </div>

    <h2>1. Intuition (Trực giác & Động lực)</h2>
    <p>Duyệt đồ thị là quá trình ghé thăm hệ thống tất cả các đỉnh của đồ thị. **BFS (Chiều rộng)** loang dần theo từng lớp khoảng cách từ đỉnh xuất phát (dùng **Queue**). **DFS (Chiều sâu)** đi sâu nhất có thể theo một nhánh trước khi quay lùi (Backtrack) (dùng **Stack** hoặc Đệ quy).</p>

    <h2>2. Formal Model & Algorithms</h2>
    <ul>
        <li><strong>BFS Algorithm:</strong> Khởi tạo `queue Q`, đánh dấu `visited[start] = true`. Lặp khi Q không rỗng: lấy `u = Q.front()`, thăm `u`, với mỗi `v` kề `u` chưa ghé thăm: đánh dấu `visited[v] = true` và `Q.push(v)`.</li>
        <li><strong>DFS Algorithm:</strong> Đánh dấu `visited[u] = true`. Với mỗi `v` kề `u` chưa ghé thăm: gọi đệ quy `DFS(v)`.</li>
    </ul>

    <h2>3. Visual Diagram (Mô tả Loang BFS vs Đi sâu DFS)</h2>
    <div class="diagram-container">
        <svg width="550" height="130" viewBox="0 0 550 130" xmlns="http://www.w3.org/2000/svg">
            <rect width="550" height="130" fill="#f8fafc" rx="8"/>
            <g transform="translate(60, 30)">
                <rect x="0" y="0" width="180" height="70" fill="#e0f2fe" stroke="#0369a1" stroke-width="2" rx="6"/>
                <text x="90" y="30" font-family="Inter" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">BFS (Chiều Rộng)</text>
                <text x="90" y="50" font-family="Inter" font-size="10" fill="#0369a1" text-anchor="middle">Sử dụng QUEUE (FIFO)</text>
            </g>
            <g transform="translate(310, 30)">
                <rect x="0" y="0" width="180" height="70" fill="#fef3c7" stroke="#b45309" stroke-width="2" rx="6"/>
                <text x="90" y="30" font-family="Inter" font-size="12" font-weight="bold" fill="#b45309" text-anchor="middle">DFS (Chiều Sâu)</text>
                <text x="90" y="50" font-family="Inter" font-size="10" fill="#b45309" text-anchor="middle">Sử dụng STACK (LIFO)</text>
            </g>
        </svg>
    </div>

    <h2>4. C++ Implementation (BFS & DFS)</h2>
    <pre><code>#include <vector>
#include <queue>
#include <iostream>

void BFS(int start, const std::vector<std::vector<int>>& adj, int V) {
    std::vector<bool> visited(V, false);
    std::queue<int> q;
    visited[start] = true; q.push(start);

    while (!q.empty()) {
        int u = q.front(); q.pop();
        std::cout << u << " ";
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
}

void DFSUtil(int u, const std::vector<std::vector<int>>& adj, std::vector<bool>& visited) {
    visited[u] = true;
    std::cout << u << " ";
    for (int v : adj[u]) {
        if (!visited[v]) DFSUtil(v, adj, visited);
    }
}</code></pre>

    <h2>5. Complexity Analysis</h2>
    <p>Cả BFS và DFS biểu diễn bằng Danh sách kề đều đạt độ phức tạp thời gian **$\Theta(V + E)$** và bộ nhớ phụ **$\Theta(V)$** cho mảng `visited` và Queue/Stack.</p>

    <h2>6. Dry Run Table (Trace BFS Từ Đỉnh 0)</h2>
    <p>Đồ thị: adj[0]={1, 2}, adj[1]={0, 3}, adj[2]={0}, adj[3]={1}:</p>
    <table>
        <thead>
            <tr><th>Bước</th><th>Đỉnh u đang xét</th><th>Hành động Hàng đợi Queue</th><th>Thứ tự ghé thăm (Visited)</th></tr>
        </thead>
        <tbody>
            <tr><td>Khởi tạo</td><td>-</td><td>Push(0) $\rightarrow$ Q = [0]</td><td>0</td></tr>
            <tr><td>1</td><td>Pop 0</td><td>Push con kề chưa thăm: Push(1), Push(2) $\rightarrow$ Q = [1, 2]</td><td>0, 1, 2</td></tr>
            <tr><td>2</td><td>Pop 1</td><td>Push con kề chưa thăm: Push(3) $\rightarrow$ Q = [2, 3]</td><td>0, 1, 2, 3</td></tr>
            <tr><td>3</td><td>Pop 2</td><td>Không có con chưa thăm $\rightarrow$ Q = [3]</td><td>0, 1, 2, 3</td></tr>
            <tr><td>4</td><td>Pop 3</td><td>Queue rỗng $\rightarrow$ Kết thúc BFS</td><td><strong>0, 1, 2, 3</strong></td></tr>
        </tbody>
    </table>

    <h2>7. Common Errors & IT003 Exam Style</h2>
    <div class="callout callout-warning">
        <span class="badge badge-exam-style">IT003 EXAM STYLE</span>
        <p><strong>Bẫy Đề Thi:</strong> Trong BFS, phải đánh dấu `visited[v] = true` **ngay khi push `v` vào Queue**, không được chờ tới khi pop `v` ra mới đánh dấu! Đánh dấu trễ sẽ khiến đỉnh `v` bị push lặp lại nhiều lần vào Queue.</p>
    </div>

    <h2>8. Quick Recall & Exercise Ladder</h2>
    <ul>
        <li><strong>Level 0:</strong> Thuật toán nào giúp tìm đường đi ngắn nhất (số cạnh ít nhất) giữa 2 đỉnh trên đồ thị không trọng số?
            <br><em>Đáp án:</em> BFS (Breadth-First Search).
        </li>
        <li><strong>Level 1:</strong> Cho đồ thị có 4 đỉnh 0, 1, 2, 3 với các cạnh (0-1), (0-2), (1-3). Viết thứ tự duyệt DFS từ đỉnh 0 (ưu tiên đỉnh nhỏ hơn).
            <br><em>Gợi ý:</em> 0 $\rightarrow$ 1 $\rightarrow$ 3 $\rightarrow$ 2.
        </li>
    </ul>

    <div class="callout">
        <div class="callout-title">📝 Tóm kết Chương 13</div>
        <p>BFS dùng Queue loang theo tầng, DFS dùng Stack/Đệ quy đi sâu. Nhớ kỹ vị trí đánh dấu `visited` trong BFS để tránh lặp đỉnh!</p>
    </div>
</section>"""
    with open(os.path.join(CHAPTERS_DIR, "13_BFS_DFS.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated 13_BFS_DFS.html")

def write_ch14():
    html = """<section class="chapter" id="ch14">
    <div class="chapter-header">
        <span class="badge badge-core">PART XIV</span>
        <h1>THUẬT TOÁN ĐƯỜNG ĐI NGẮN NHẤT (SHORTEST PATH - DIJKSTRA)</h1>
    </div>

    <h2>1. Intuition (Trực giác & Động lực)</h2>
    <p>Bài toán tìm đường đi ngắn nhất giữa 2 địa điểm trên bản đồ Google Maps là ứng dụng thực tế phổ biến nhất của thuật toán **Dijkstra**. Thuật toán hoạt động theo nguyên lý tham ăn (Greedy): luôn chọn đỉnh có khoảng cách tạm thời nhỏ nhất để cố định (Fix/Finalize) đường đi ngắn nhất tới đỉnh đó.</p>

    <h2>2. Formal Model & Relaxation Principle</h2>
    <p>Điều kiện tiên quyết: Đồ thị có **trọng số không âm ($w(e) \ge 0$)**. Thao tác **Nới cạnh (Relaxation)** giữa cạnh $(u, v)$ có trọng số $w$:</p>
    $$\text{If } d[u] + w < d[v] \Rightarrow d[v] = d[u] + w, \quad p[v] = u$$

    <h2>3. Visual Diagram (Sơ đồ Nới Cạnh Relaxation)</h2>
    <div class="diagram-container">
        <svg width="550" height="120" viewBox="0 0 550 120" xmlns="http://www.w3.org/2000/svg">
            <rect width="550" height="120" fill="#f8fafc" rx="8"/>
            <g transform="translate(80, 40)">
                <circle cx="0" cy="0" r="18" fill="#15803d"/>
                <text x="0" y="5" fill="#ffffff" font-family="Inter" font-size="11" font-weight="bold" text-anchor="middle">u (d[u]=2)</text>
            </g>
            <line x1="105" y1="40" x2="275" y2="40" stroke="#1e40af" stroke-width="3" marker-end="url(#arrow)"/>
            <text x="190" y="30" fill="#1e40af" font-family="Inter" font-size="11" font-weight="bold">w = 3</text>
            <g transform="translate(300, 40)">
                <circle cx="0" cy="0" r="18" fill="#b91c1c"/>
                <text x="0" y="5" fill="#ffffff" font-family="Inter" font-size="11" font-weight="bold" text-anchor="middle">v (d[v]=9)</text>
            </g>
            <text x="350" y="45" font-family="Inter" font-size="11" font-weight="bold" fill="#15803d">Relax: d[v] mới = 2 + 3 = 5!</text>
        </svg>
    </div>

    <h2>4. C++ Implementation (Dijkstra using Priority Queue)</h2>
    <pre><code>#include <vector>
#include <queue>
#include <iostream>

const int INF = 1e9;
using pii = std::pair<int, int>; // (d[u], u)

void dijkstra(int start, const std::vector<std::vector<pii>>& adj, int V) {
    std::vector<int> d(V, INF);
    std::priority_queue<pii, std::vector<pii>, std::greater<pii>> pq;

    d[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [dist, u] = pq.top(); pq.pop();
        if (dist > d[u]) continue;

        for (auto& edge : adj[u]) {
            int v = edge.first, w = edge.second;
            if (d[u] + w < d[v]) {
                d[v] = d[u] + w;
                pq.push({d[v], v});
            }
        }
    }
}</code></pre>

    <h2>5. Complexity Analysis</h2>
    <ul>
        <li>Dijkstra dùng Mảng thông thường: $\Theta(V^2 + E) = \Theta(V^2)$. Thích hợp cho Đồ thị dày ($E \approx V^2$).</li>
        <li>Dijkstra dùng Min-Heap / Priority Queue: **$\Theta((V + E) \log V)$**. Thích hợp cho Đồ thị thưa.</li>
    </ul>

    <h2>6. Dry Run Table (Trace Dijkstra Chuẩn Đề Thi IT003)</h2>
    <p>Tìm đường đi từ A (đỉnh 0) đến các đỉnh 1, 2, 3 với các cạnh (0-1: 4), (0-2: 2), (2-1: 1), (1-3: 5):</p>
    <table>
        <thead>
            <tr><th>Bước</th><th>Đỉnh u chọn cố định</th><th>d[0]</th><th>d[1]</th><th>d[2]</th><th>d[3]</th><th>Hành động Nới Cạnh</th></tr>
        </thead>
        <tbody>
            <tr><td>0</td><td>-</td><td><strong>0</strong></td><td>$\infty$</td><td>$\infty$</td><td>$\infty$</td><td>Khởi tạo d[0]=0</td></tr>
            <tr><td>1</td><td>0 (d[0]=0)</td><td><strong>0</strong></td><td>4 (từ 0)</td><td>2 (từ 0)</td><td>$\infty$</td><td>Nới cạnh (0-1:4), (0-2:2)</td></tr>
            <tr><td>2</td><td>2 (d[2]=2)</td><td><strong>0</strong></td><td><strong>3</strong> (từ 2)</td><td><strong>2</strong></td><td>$\infty$</td><td>Nới cạnh (2-1: 2+1=3 < 4) $\rightarrow$ Cập nhật d[1]=3!</td></tr>
            <tr><td>3</td><td>1 (d[1]=3)</td><td><strong>0</strong></td><td><strong>3</strong></td><td><strong>2</strong></td><td><strong>8</strong> (từ 1)</td><td>Nới cạnh (1-3: 3+5=8) $\rightarrow$ Cập nhật d[3]=8</td></tr>
            <tr><td>4</td><td>3 (d[3]=8)</td><td><strong>0</strong></td><td><strong>3</strong></td><td><strong>2</strong></td><td><strong>8</strong></td><td>Tất cả các đỉnh đã cố định đường đi ngắn nhất!</td></tr>
        </tbody>
    </table>

    <h2>7. Common Errors & IT003 Exam Style</h2>
    <div class="callout callout-warning">
        <span class="badge badge-exam-style">IT003 EXAM STYLE</span>
        <p><strong>Bẫy Đề Thi:</strong> Thuật toán Dijkstra **KHÔNG chạy đúng khi đồ thị có cạnh mang trọng số âm**! Nếu đồ thị có trọng số âm, phải chuyển sang dùng thuật toán Bellman-Ford.</p>
    </div>

    <h2>8. Quick Recall & Exercise Ladder</h2>
    <ul>
        <li><strong>Level 0:</strong> Thuật toán Dijkstra có làm việc được trên đồ thị có chu trình âm không?
            <br><em>Đáp án:</em> Không. Chu trình âm khiến khoảng cách giảm vô tận thành $-\infty$.
        </li>
        <li><strong>Level 1:</strong> Trình bày bảng trace Dijkstra tìm đường đi ngắn nhất từ đỉnh 0 với đồ thị có các trọng số cho trước.
            <br><em>Gợi ý:</em> Lập bảng cột đỉnh, cố định đỉnh có $d[u]$ nhỏ nhất ở mỗi dòng.
        </li>
    </ul>

    <div class="callout">
        <div class="callout-title">📝 Tóm kết Chương 14</div>
        <p>Dijkstra chọn đỉnh tham ăn có $d[u]$ nhỏ nhất để cố định đường đi. Đảm bảo thuộc lòng các bước lập bảng nới cạnh để ghi trọn điểm câu đồ thị cuối kỳ!</p>
    </div>
</section>"""
    with open(os.path.join(CHAPTERS_DIR, "14_SHORTEST_PATH.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated 14_SHORTEST_PATH.html")

def write_ch15():
    html = """<section class="chapter" id="ch15">
    <div class="chapter-header">
        <span class="badge badge-core">PART XV</span>
        <h1>EXAM TOOLKIT & BỘ ĐỀ ÔN THI MẪU CHUẨN IT003</h1>
    </div>

    <h2>1. Quick Recall Cheat Sheet (Tóm Tắt Nhanh Ôn Thi)</h2>
    <div class="callout">
        <div class="callout-title">⚡ Master Summary Cheat Sheet</div>
        <ul>
            <li><strong>Selection & Interchange Sort:</strong> Phép so sánh luôn cố định $C = \frac{n(n-1)}{2}$. Interchange Sort là thuật toán đặc thù UIT.</li>
            <li><strong>Binary Search:</strong> Bắt buộc mảng đã sắp xếp. $\Theta(\log n)$ thời gian.</li>
            <li><strong>BST Deletion (2 con):</strong> Đọc kỹ đề dùng Max-Left hay Min-Right làm phần tử thế mạng.</li>
            <li><strong>AVL Rotation:</strong> $BF = h_{left} - h_{right}$. $+2$ nghiêng trái (LL/LR), $-2$ nghiêng phải (RR/RL).</li>
            <li><strong>B-Tree Bậc 5 ($m=5$):</strong> Max 4 keys, Min 2 keys per node. Tràn 5 keys $\rightarrow$ Tách nút đẩy nổi khóa thứ 3 (trung vị) lên cha.</li>
            <li><strong>Hash Probing Unsuccessful Search:</strong> Phải dò tới khi gặp ô `EMPTY` đầu tiên. Ô `DELETED` không dừng!</li>
            <li><strong>BFS / DFS:</strong> BFS dùng Queue loang theo lớp; DFS dùng Stack/Đệ quy đi sâu.</li>
            <li><strong>Dijkstra:</strong> Chỉ áp dụng cho trọng số không âm ($w \ge 0$). Nới cạnh: `if (d[u] + w < d[v]) d[v] = d[u] + w`.</li>
        </ul>
    </div>

    <h2>2. Integrated Practice Bank (Bộ Đề Thi Mẫu 5 Level)</h2>

    <h3>Bộ Đề Mẫu 1 (Thi Cuối Kỳ IT003 Standard)</h3>
    <p><strong>Câu 1 (2.5 điểm): Sắp Xếp & Đếm Phép Toán</strong></p>
    <p>Cho dãy số $A = [25, 12, 40, 8, 30]$.</p>
    <p>a) Trình bày trạng thái mảng sau từng bước của Interchange Sort. Tính số phép so sánh $C$ và số phép đổi chỗ $M$.</p>
    <p>b) Thực hiện phân hoạch Lomuto đầu tiên cho Quick Sort với Pivot $a[high] = 30$.</p>
    <p><em>Lời giải tóm tắt:</em>
    <br>a) $C = 5(4)/2 = 10$ phép so sánh. Trạng thái sau từng i:
    <br>• $i=0$: Swap(25, 12) $\rightarrow$ Swap(12, 8) $\rightarrow [8, 25, 40, 12, 30]$
    <br>• $i=1$: Swap(25, 12) $\rightarrow [8, 12, 40, 25, 30]$
    <br>• $i=2$: Swap(40, 25) $\rightarrow [8, 12, 25, 40, 30]$
    <br>• $i=3$: Swap(40, 30) $\rightarrow [8, 12, 25, 30, 40]$. Mảng hoàn chỉnh! Total Swaps $M = 5$.
    </p>

    <p><strong>Câu 2 (2.5 điểm): Cây AVL</strong></p>
    <p>Lần lượt chèn các khóa sau vào cây AVL rỗng: $18, 10, 25, 6, 14$. Xác định nút mất cân bằng và vẽ cây AVL sau mỗi lần xoay.</p>
    <p><em>Lời giải tóm tắt:</em>
    <br>• Chèn 18, 10, 25 $\rightarrow$ Cây cân bằng.
    <br>• Chèn 6 $\rightarrow$ Cây cân bằng ($BF(18) = +2$, $BF(10) = +1 \rightarrow$ LL tại 18 $\rightarrow$ Xoay Phải 18 $\rightarrow$ Root 10, Left 6, Right 18 (Right of 18 is 25)).
    <br>• Chèn 14 $\rightarrow$ Cây cân bằng hoàn hảo.
    </p>

    <p><strong>Câu 3 (2.5 điểm): Bảng Băm & B-Tree</strong></p>
    <p>Cho $M=7, h(k) = k \bmod 7$. Chèn các khóa $14, 21, 7, 15$ dùng Linear Probing. Tính $C_{\text{succ}}$ trung bình.</p>
    <p><em>Lời giải tóm tắt:</em>
    <br>• 14 % 7 = 0 $\rightarrow$ Ô 0 (1 probe)
    <br>• 21 % 7 = 0 $\rightarrow$ Ô 1 (2 probes)
    <br>• 7 % 7 = 0 $\rightarrow$ Ô 2 (3 probes)
    <br>• 15 % 7 = 1 $\rightarrow$ Đụng ô 1 $\rightarrow$ Ô 3 (3 probes)
    <br>$\Rightarrow C_{\text{succ}} = \frac{1 + 2 + 3 + 3}{4} = \frac{9}{4} = 2.25$ phép so sánh.
    </p>

    <p><strong>Câu 4 (2.5 điểm): Đồ thị Dijkstra</strong></p>
    <p>Lập bảng trace Dijkstra tìm đường đi ngắn nhất từ đỉnh 0 cho đồ thị 4 đỉnh với ma trận trọng số cho trước.</p>

    <div class="callout callout-warning">
        <div class="callout-title">🎓 Lời Chúc Thi Tốt từ Ban Biên Soạn</div>
        <p>Chúc các bạn sinh viên UIT ôn luyện hiệu quả, tự tin áp dụng tư duy chạy tay và đạt điểm 10 tuyệt đối trong kỳ thi môn IT003!</p>
    </div>
</section>"""
    with open(os.path.join(CHAPTERS_DIR, "15_EXAM_TOOLKIT.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated 15_EXAM_TOOLKIT.html")

def main():
    write_ch07()
    write_ch08()
    write_ch09()
    write_ch10()
    write_ch11()
    write_ch12()
    write_ch13()
    write_ch14()
    write_ch15()

if __name__ == "__main__":
    main()
