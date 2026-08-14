import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

BASE_DIR = r"C:\Users\lyle3\.gemini\antigravity\scratch\IT003_DSA_BOOK"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
os.makedirs(CHAPTERS_DIR, exist_ok=True)

def write_ch04():
    html = """<section class="chapter" id="ch04">
    <div class="chapter-header">
        <span class="badge badge-core">PART IV</span>
        <h1>DANH SÁCH LIÊN KẾT (LINKED LIST)</h1>
    </div>

    <h2>1. Intuition (Trực giác & Động lực)</h2>
    <p>Mảng tĩnh có kích thước cố định và thao tác chèn/xóa ở giữa tốn $\mathcal{O}(n)$ do phải dời hàng loạt phần tử. Danh sách liên kết (Linked List) giải quyết triệt để vấn đề này bằng cách cấp phát động từng nút (Node) nằm rải rác trên bộ nhớ Heap và liên kết chúng bằng các con trỏ (Pointer).</p>

    <h2>2. Formal Model (Định nghĩa Cấu trúc)</h2>
    <p>Một **Singly Linked List** gồm tập hợp các nút `Node`, trong đó mỗi nút chứa 2 thành phần: `data` (giá trị lưu trữ) và `pNext` (con trỏ chỉ tới nút kế tiếp). Danh sách được quản lý bởi con trỏ `pHead` (chỉ nút đầu) và `pTail` (chỉ nút cuối).</p>

    <h2>3. Visual Diagram (Sơ đồ Bộ nhớ Danh sách Liên kết)</h2>
    <div class="diagram-container">
        <svg width="620" height="120" viewBox="0 0 620 120" xmlns="http://www.w3.org/2000/svg">
            <rect width="620" height="120" fill="#f8fafc" rx="8"/>
            <g transform="translate(30, 35)">
                <rect x="0" y="0" width="60" height="40" fill="#0f172a" rx="4"/>
                <text x="30" y="25" fill="#ffffff" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">10</text>
                <rect x="60" y="0" width="30" height="40" fill="#1e40af" rx="4"/>
                <circle cx="75" cy="20" r="4" fill="#ffffff"/>
                <line x1="75" y1="20" x2="135" y2="20" stroke="#1e40af" stroke-width="2" marker-end="url(#arrow)"/>
            </g>
            <g transform="translate(170, 35)">
                <rect x="0" y="0" width="60" height="40" fill="#0f172a" rx="4"/>
                <text x="30" y="25" fill="#ffffff" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">25</text>
                <rect x="60" y="0" width="30" height="40" fill="#1e40af" rx="4"/>
                <circle cx="75" cy="20" r="4" fill="#ffffff"/>
                <line x1="75" y1="20" x2="135" y2="20" stroke="#1e40af" stroke-width="2" marker-end="url(#arrow)"/>
            </g>
            <g transform="translate(310, 35)">
                <rect x="0" y="0" width="60" height="40" fill="#0f172a" rx="4"/>
                <text x="30" y="25" fill="#ffffff" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">40</text>
                <rect x="60" y="0" width="30" height="40" fill="#64748b" rx="4"/>
                <text x="75" y="24" fill="#ffffff" font-family="Inter" font-size="10" font-weight="bold" text-anchor="middle">NULL</text>
            </g>
            <defs>
                <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 0 L 10 5 L 0 10 z" fill="#1e40af"/>
                </marker>
            </defs>
        </svg>
    </div>

    <h2>4. Algorithm & Mechanics (Các Thao tác Con trỏ)</h2>
    <ul>
        <li><strong>Add Head:</strong> Tạo `pNew`. Cho `pNew->pNext = pHead`. Cập nhật `pHead = pNew`.</li>
        <li><strong>Add Tail:</strong> Tạo `pNew`. Cho `pTail->pNext = pNew`. Cập nhật `pTail = pNew`.</li>
        <li><strong>Delete Head:</strong> Lưu `temp = pHead`. Cho `pHead = pHead->pNext`. Giải phóng `delete temp`.</li>
    </ul>

    <h2>5. C++ Educational & STL Code</h2>
    <pre><code>struct Node {
    int data;
    Node* pNext;
};

struct LinkedList {
    Node* pHead;
    Node* pTail;
};

void initList(LinkedList& list) {
    list.pHead = list.pTail = nullptr;
}

Node* createNode(int val) {
    Node* p = new Node;
    if (p == nullptr) return nullptr;
    p->data = val;
    p->pNext = nullptr;
    return p;
}

void addHead(LinkedList& list, int val) {
    Node* p = createNode(val);
    if (list.pHead == nullptr) {
        list.pHead = list.pTail = p;
    } else {
        p->pNext = list.pHead;
        list.pHead = p;
    }
}

// STL Usage Example
#include <list>
void stlExample() {
    std::list<int> myList;
    myList.push_front(10);
    myList.push_back(20);
}</code></pre>

    <h2>6. Complexity Analysis & Edge Cases</h2>
    <ul>
        <li><strong>Chèn/Xóa ở Đầu:</strong> $\Theta(1)$ thời gian, $\mathcal{O}(1)$ bộ nhớ.</li>
        <li><strong>Truy xuất theo chỉ số / Tìm kiếm:</strong> $\Theta(n)$ thời gian.</li>
        <li><strong>Edge Cases bắt buộc kiểm tra:</strong> Danh sách rỗng (`pHead == nullptr`), Danh sách chỉ có 1 nút (`pHead == pTail`).</li>
    </ul>

    <h2>7. Dry Run Table (Chạy tay Thao tác Add Head & Delete Head)</h2>
    <table>
        <thead>
            <tr><th>Thao tác</th><th>Trạng thái pHead trước</th><th>Trạng thái pTail trước</th><th>Biến đổi con trỏ</th><th>Trạng thái pHead sau</th></tr>
        </thead>
        <tbody>
            <tr><td>Add Head(10) vào List rỗng</td><td>nullptr</td><td>nullptr</td><td>`pHead = pTail = pNew`</td><td>Node(10)</td></tr>
            <tr><td>Add Head(5) vào List(10)</td><td>Node(10)</td><td>Node(10)</td><td>`pNew->pNext = pHead; pHead = pNew`</td><td>Node(5) $\rightarrow$ Node(10)</td></tr>
            <tr><td>Delete Head trên List(5, 10)</td><td>Node(5)</td><td>Node(10)</td><td>`temp=pHead; pHead=pHead->pNext; delete temp`</td><td>Node(10)</td></tr>
        </tbody>
    </table>

    <h2>8. Common Errors & IT003 Exam Style</h2>
    <div class="callout callout-warning">
        <span class="badge badge-exam-style">IT003 EXAM STYLE</span>
        <p><strong>Bẫy Đề Thi:</strong> Khi xóa nút duy nhất trong danh sách, nếu chỉ cập nhật `pHead = nullptr` mà không cập nhật `pTail = nullptr`, con trỏ `pTail` sẽ trở thành **Con trỏ rác (Dangling Pointer)** dẫn đến sập chương trình ở các thao tác sau!</p>
    </div>

    <h2>9. Quick Recall & Exercise Ladder</h2>
    <ul>
        <li><strong>Level 0:</strong> Tại sao chèn vào cuối DSLK đơn có con trỏ `pTail` tốn $\mathcal{O}(1)$ nhưng xóa phần tử cuối vẫn tốn $\Theta(n)$?
            <br><em>Đáp án:</em> Vì để cập nhật `pTail` mới, ta phải duyệt từ `pHead` đến nút áp cuối (nút trước `pTail`), tốn $\Theta(n)$.
        </li>
        <li><strong>Level 1:</strong> Viết hàm đếm số phần tử trong DSLK đơn.
            <br><em>Gợi ý:</em> Dùng con trỏ chạy `Node* p = list.pHead`, vừa duyệt vừa tăng biến đếm `count++` cho đến khi `p == nullptr`.
        </li>
    </ul>

    <div class="callout">
        <div class="callout-title">📝 Tóm kết Chương 4</div>
        <p>DSLK cho phép chèn/xóa ở đầu trong $\mathcal{O}(1)$ mà không cần dời bộ nhớ. Luôn chú ý quản lý cả `pHead` và `pTail` cùng các trường hợp rỗng/1 nút!</p>
    </div>
</section>"""
    with open(os.path.join(CHAPTERS_DIR, "04_LINKED_LIST.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated 04_LINKED_LIST.html")

def write_ch05():
    html = """<section class="chapter" id="ch05">
    <div class="chapter-header">
        <span class="badge badge-core">PART V</span>
        <h1>NGĂN XẾP VÀ HÀNG ĐỢI (STACK & QUEUE)</h1>
    </div>

    <h2>1. Intuition (Trực giác & Động lực)</h2>
    <p><strong>Stack (Ngăn xếp)</strong> giống như một chồng dĩa: dĩa nào đặt vào sau cùng sẽ được lấy ra đầu tiên (<strong>LIFO — Last In, First Out</strong>). <strong>Queue (Hàng đợi)</strong> giống như hàng người xếp hàng mua vé: ai đến trước sẽ được phục vụ trước (<strong>FIFO — First In, First Out</strong>).</p>

    <h2>2. Formal Model (Định nghĩa Cấu trúc)</h2>
    <ul>
        <li><strong>Stack ADT:</strong> Các thao tác chính gồm <code>push(x)</code> (thêm vào đỉnh), <code>pop()</code> (lấy khỏi đỉnh), <code>top()</code> (xem đỉnh), <code>isEmpty()</code>.</li>
        <li><strong>Queue ADT:</strong> Các thao tác chính gồm <code>enqueue(x)</code> (thêm vào đuôi), <code>dequeue()</code> (lấy khỏi đầu), <code>front()</code> (xem đầu), <code>isEmpty()</code>.</li>
    </ul>

    <h2>3. Visual Diagram (Sơ đồ Tràn Ảo & Hàng Đợi Vòng)</h2>
    <div class="diagram-container">
        <svg width="600" height="150" viewBox="0 0 600 150" xmlns="http://www.w3.org/2000/svg">
            <rect width="600" height="150" fill="#f8fafc" rx="8"/>
            <g transform="translate(50, 40)">
                <!-- Circular Queue Representation -->
                <circle cx="100" cy="35" r="45" fill="none" stroke="#3b82f6" stroke-width="4"/>
                <text x="100" y="30" font-family="Inter" font-size="11" font-weight="bold" text-anchor="middle">CIRCULAR</text>
                <text x="100" y="45" font-family="Inter" font-size="11" font-weight="bold" text-anchor="middle">QUEUE</text>
                <path d="M 145 35 A 45 45 0 0 1 100 80" fill="none" stroke="#1e40af" stroke-width="4" marker-end="url(#arrow)"/>
            </g>
            <g transform="translate(280, 30)">
                <text x="0" y="20" font-family="Inter" font-size="11" font-weight="bold" fill="#0f172a">Công thức Hàng Đợi Vòng (Modulo):</text>
                <text x="0" y="45" font-family="Fira Code" font-size="11" fill="#1e40af">rear = (rear + 1) % MAX;</text>
                <text x="0" y="70" font-family="Fira Code" font-size="11" fill="#1e40af">front = (front + 1) % MAX;</text>
            </g>
        </svg>
    </div>

    <h2>4. Algorithm & Mechanics (Hiện tượng Tràn Ảo - False Overflow)</h2>
    <p>Khi dùng mảng tĩnh cho Queue, sau một số thao tác enqueue và dequeue, chỉ số `rear` tiến tới `MAX - 1`. Khi này mảng báo đầy (`rear == MAX - 1`) dù các ô đầu mảng đã bị bỏ trống. Giải pháp là dùng **Circular Queue** với phép toán chia lấy dư `% MAX`.</p>

    <h2>5. C++ Educational & STL Code</h2>
    <pre><code>// Circular Queue Implementation
const int MAX = 100;
struct CircularQueue {
    int front, rear, count;
    int a[MAX];

    CircularQueue() {
        front = 0; rear = -1; count = 0;
    }

    bool enqueue(int x) {
        if (count == MAX) return false; // Full
        rear = (rear + 1) % MAX;
        a[rear] = x;
        count++;
        return true;
    }

    int dequeue() {
        if (count == 0) return -1; // Empty
        int val = a[front];
        front = (front + 1) % MAX;
        count--;
        return val;
    }
};

// C++ STL Standard Stack & Queue
#include <stack>
#include <queue>

void stlStackQueue() {
    std::stack<int> s;
    s.push(10); s.pop();

    std::queue<int> q;
    q.push(20); q.pop();
}</code></pre>

    <h2>6. Complexity Analysis & Invariants</h2>
    <p>Tất cả các thao tác `push`, `pop`, `top`, `enqueue`, `dequeue`, `front` trên Stack và Queue chuẩn đều đạt độ phức tạp **$\Theta(1)$ thời gian và $\mathcal{O}(1)$ bộ nhớ phụ**.</p>

    <h2>7. Dry Run Table (Trace Chuỗi Thao Tác Circular Queue)</h2>
    <p>Thực hiện lần lượt: Enqueue(5), Enqueue(8), Dequeue(), Enqueue(12) trên Queue $MAX=3$:</p>
    <table>
        <thead>
            <tr><th>Thao tác</th><th>front</th><th>rear</th><th>count</th><th>Mảng a[0..2]</th><th>Kết quả trả về</th></tr>
        </thead>
        <tbody>
            <tr><td>Ban đầu</td><td>0</td><td>-1</td><td>0</td><td>[-, -, -]</td><td>-</td></tr>
            <tr><td>Enqueue(5)</td><td>0</td><td>0</td><td>1</td><td>[5, -, -]</td><td>True</td></tr>
            <tr><td>Enqueue(8)</td><td>0</td><td>1</td><td>2</td><td>[5, 8, -]</td><td>True</td></tr>
            <tr><td>Dequeue()</td><td>1</td><td>1</td><td>1</td><td>[-, 8, -]</td><td>5</td></tr>
            <tr><td>Enqueue(12)</td><td>1</td><td>2</td><td>2</td><td>[-, 8, 12]</td><td>True</td></tr>
        </tbody>
    </table>

    <h2>8. Common Errors & IT003 Exam Style</h2>
    <div class="callout callout-warning">
        <span class="badge badge-exam-style">IT003 EXAM STYLE</span>
        <p><strong>Bẫy Đề Thi:</strong> Ứng dụng kiểm tra biểu thức ngoặc hợp lệ (Parentheses Matching) hoặc chuyển đổi Hậu tố (Postfix). Luôn nhớ: DFS dùng **Stack**, BFS dùng **Queue**!</p>
    </div>

    <h2>9. Quick Recall & Exercise Ladder</h2>
    <ul>
        <li><strong>Level 0:</strong> Phân biệt nguyên lý hoạt động của Stack và Queue.
            <br><em>Đáp án:</em> Stack là LIFO (Vào sau Ra trước), Queue là FIFO (Vào trước Ra trước).
        </li>
        <li><strong>Level 1:</strong> Cho chuỗi thao tác Stack: `Push(3), Push(7), Pop(), Push(5), Pop()`. Giá trị còn lại trong Stack là gì?
            <br><em>Gợi ý:</em> Push 3 $\rightarrow$ Push 7 $\rightarrow$ Pop 7 $\rightarrow$ Push 5 $\rightarrow$ Pop 5 $\Rightarrow$ Còn lại giá trị 3.
        </li>
    </ul>

    <div class="callout">
        <div class="callout-title">📝 Tóm kết Chương 5</div>
        <p>Stack và Queue là 2 cấu trúc dữ liệu tuyến tính quan trọng nhất làm tiền đề cho các thuật toán duyệt cây, duyệt đồ thị BFS/DFS.</p>
    </div>
</section>"""
    with open(os.path.join(CHAPTERS_DIR, "05_STACK_QUEUE.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated 05_STACK_QUEUE.html")

def write_ch06():
    html = """<section class="chapter" id="ch06">
    <div class="chapter-header">
        <span class="badge badge-core">PART VI</span>
        <h1>CÂY VÀ CÂY NHỊ PHÂN (TREES & BINARY TREES)</h1>
    </div>

    <h2>1. Intuition (Trực giác & Động lực)</h2>
    <p>Khác với mảng hay danh sách liên kết là cấu trúc dữ liệu tuyến tính (Linear), Cây (Tree) là cấu trúc dữ liệu phi tuyến (Non-linear) phân cấp. Cây mô phỏng hoàn hảo các hệ thống phân cấp thực tế như cây thư mục máy tính, sơ đồ tổ chức công ty hay cây quyết định.</p>

    <h2>2. Formal Model & Terminology (Định nghĩa & Thuật ngữ)</h2>
    <ul>
        <li><strong>Root (Gốc):</strong> Nút duy nhất không có nút cha.</li>
        <li><strong>Leaf (Nút lá):</strong> Nút không có con nào (bậc của nút bằng 0).</li>
        <li><strong>Degree (Bậc):</strong> Số nút con của một nút.</li>
        <li><span class="badge badge-uit-convention">IT003 CONVENTION</span> <strong>Level (Mức):</strong> Nút gốc Root nằm ở <strong>Level 0</strong>. Nút con của Root nằm ở Level 1. Chiều cao của cây $H = \text{max\_level} + 1$.</li>
    </ul>

    <h2>3. Visual Diagram (Sơ đồ Duyệt Cây Nhị Phân)</h2>
    <div class="diagram-container">
        <svg width="500" height="180" viewBox="0 0 500 180" xmlns="http://www.w3.org/2000/svg">
            <rect width="500" height="180" fill="#f8fafc" rx="8"/>
            <!-- Tree Nodes -->
            <g transform="translate(250, 30)">
                <circle cx="0" cy="0" r="18" fill="#0f172a"/>
                <text x="0" y="5" fill="#ffffff" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">A</text>
            </g>
            <g transform="translate(160, 90)">
                <circle cx="0" cy="0" r="18" fill="#1e40af"/>
                <text x="0" y="5" fill="#ffffff" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">B</text>
            </g>
            <g transform="translate(340, 90)">
                <circle cx="0" cy="0" r="18" fill="#1e40af"/>
                <text x="0" y="5" fill="#ffffff" font-family="Inter" font-size="12" font-weight="bold" text-anchor="middle">C</text>
            </g>
            <!-- Edges -->
            <line x1="237" y1="43" x2="173" y2="77" stroke="#0f172a" stroke-width="2"/>
            <line x1="263" y1="43" x2="327" y2="77" stroke="#0f172a" stroke-width="2"/>
        </svg>
    </div>

    <h2>4. Algorithm & Mechanics (3 Phép Duyệt Cây)</h2>
    <ul>
        <li><strong>NLR (Pre-order / Tiền tự):</strong> Thăm Nút gốc $N \rightarrow$ Duyệt Cây con trái $L \rightarrow$ Duyệt Cây con phải $R$.</li>
        <li><strong>LNR (In-order / Trung tự):</strong> Duyệt Cây con trái $L \rightarrow$ Thăm Nút gốc $N \rightarrow$ Duyệt Cây con phải $R$.</li>
        <li><strong>LRN (Post-order / Hậu tự):</strong> Duyệt Cây con trái $L \rightarrow$ Duyệt Cây con phải $R \rightarrow$ Thăm Nút gốc $N$.</li>
    </ul>

    <h2>5. C++ Educational & Traversals Code</h2>
    <pre><code>struct TreeNode {
    int data;
    TreeNode* pLeft;
    TreeNode* pRight;
};

void preOrder(TreeNode* root) {
    if (root != nullptr) {
        std::cout << root->data << " ";
        preOrder(root->pLeft);
        preOrder(root->pRight);
    }
}

void inOrder(TreeNode* root) {
    if (root != nullptr) {
        inOrder(root->pLeft);
        std::cout << root->data << " ";
        inOrder(root->pRight);
    }
}

void postOrder(TreeNode* root) {
    if (root != nullptr) {
        postOrder(root->pLeft);
        postOrder(root->pRight);
        std::cout << root->data << " ";
    }
}</code></pre>

    <h2>6. Complexity Analysis & Invariants</h2>
    <p>Tất cả các phép duyệt cây nhị phân đều ghé thăm mỗi nút đúng 1 lần, độ phức tạp là **$\Theta(n)$ thời gian và $\mathcal{O}(h)$ bộ nhớ phụ** (với $h$ là chiều cao cây do gọi đệ quy trên Call Stack).</p>

    <h2>7. Dry Run Table (Trace Phép Duyệt NLR, LNR, LRN)</h2>
    <p>Cho cây nhị phân: Gốc A, con trái B, con phải C. B có con trái D:</p>
    <table>
        <thead>
            <tr><th>Phép duyệt</th><th>Thứ tự nút được ghé thăm</th></tr>
        </thead>
        <tbody>
            <tr><td><strong>NLR (Tiền tự)</strong></td><td>A $\rightarrow$ B $\rightarrow$ D $\rightarrow$ C</td></tr>
            <tr><td><strong>LNR (Trung tự)</strong></td><td>D $\rightarrow$ B $\rightarrow$ A $\rightarrow$ C</td></tr>
            <tr><td><strong>LRN (Hậu tự)</strong></td><td>D $\rightarrow$ B $\rightarrow$ C $\rightarrow$ A</td></tr>
        </tbody>
    </table>

    <h2>8. Common Errors & IT003 Exam Style</h2>
    <div class="callout callout-warning">
        <span class="badge badge-exam-style">IT003 EXAM STYLE</span>
        <p><strong>Bẫy Đề Thi:</strong> Xác định chiều cao của cây $H$. Đọc kỹ quy ước trong đề thi! Nếu đề thi tính Root ở Level 0 thì $H = \text{max\_level} + 1$. Nếu tính Root ở Level 1 thì $H = \text{max\_level}$.</p>
    </div>

    <h2>9. Quick Recall & Exercise Ladder</h2>
    <ul>
        <li><strong>Level 0:</strong> Phép duyệt nào trên Cây Nhị Phân Tìm Kiếm (BST) sẽ xuất ra các giá trị khóa theo thứ tự tăng dần?
            <br><em>Đáp án:</em> Phép duyệt Trung tự **LNR (In-order)**.
        </li>
        <li><strong>Level 1:</strong> Tính số nút tối đa của một Cây nhị phân có chiều cao $h$ (Root ở Level 0, height $h = \text{max\_level} + 1$).
            <br><em>Gợi ý:</em> Số nút tối đa là $2^h - 1$.
        </li>
    </ul>

    <div class="callout">
        <div class="callout-title">📝 Tóm kết Chương 6</div>
        <p>Nắm vững khái niệm mức (Level), chiều cao và 3 phép duyệt NLR, LNR, LRN là chìa khóa để xử lý toàn bộ các câu hỏi về Cây trong đề thi IT003.</p>
    </div>
</section>"""
    with open(os.path.join(CHAPTERS_DIR, "06_TREES_BINARY_TREES.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated 06_TREES_BINARY_TREES.html")

def main():
    write_ch04()
    write_ch05()
    write_ch06()

if __name__ == "__main__":
    main()
