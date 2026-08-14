import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

BASE_DIR = r"C:\Users\lyle3\.gemini\antigravity\scratch\IT003_DSA_BOOK"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
os.makedirs(CHAPTERS_DIR, exist_ok=True)

def write_ch05():
    content = """<section class="chapter" id="ch05">
    <div class="chapter-header">
        <span class="badge badge-core">PART V</span>
        <h1>NGĂN XẾP VÀ HÀNG ĐỢI (STACK & QUEUE)</h1>
    </div>

    <h2>1. Stack (Ngăn xếp - LIFO)</h2>
    <p>Stack hoạt động theo nguyên lý <strong>Last In, First Out (LIFO)</strong> — Phần tử nào vào sau cùng sẽ được lấy ra đầu tiên. Các thao tác chính: <code>push</code>, <code>pop</code>, <code>top</code>/<code>peek</code>, <code>isEmpty</code>.</p>

    <h3>C++ Code (Array-based Stack)</h3>
    <pre><code>const int MAX = 1000;
struct Stack {
    int topIndex;
    int a[MAX];

    Stack() { topIndex = -1; }

    bool push(int x) {
        if (topIndex >= (MAX - 1)) return false; // Overflow
        a[++topIndex] = x;
        return true;
    }

    int pop() {
        if (topIndex < 0) return -1; // Underflow
        return a[topIndex--];
    }

    int top() {
        if (topIndex < 0) return -1;
        return a[topIndex];
    }

    bool isEmpty() { return (topIndex < 0); }
};</code></pre>

    <h2>2. Queue (Hàng đợi - FIFO) & Circular Queue</h2>
    <p>Queue hoạt động theo nguyên lý <strong>First In, First Out (FIFO)</strong>. Trong mảng tĩnh thông thường, việc loại bỏ phần tử ở đầu làm cho chỉ số `front` tăng dần, dẫn đến <strong>Hiện tượng Tràn ảo (False Overflow)</strong> khi `rear == MAX - 1` dù mảng còn trống ở đầu.</p>

    <p><span class="badge badge-uit-convention">IT003 CONVENTION</span>: Giải pháp triệt để cho hiện tượng Tràn ảo là <strong>Circular Queue (Hàng đợi vòng)</strong> sử dụng phép toán chia lấy dư (modulo `%`).</p>

    <h3>C++ Circular Queue Code</h3>
    <pre><code>struct CircularQueue {
    int front, rear, count;
    int a[MAX];

    CircularQueue() {
        front = 0;
        rear = -1;
        count = 0;
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
};</code></pre>
</section>
"""
    with open(os.path.join(CHAPTERS_DIR, "05_STACK_QUEUE.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote 05_STACK_QUEUE.html")

def write_ch06():
    content = """<section class="chapter" id="ch06">
    <div class="chapter-header">
        <span class="badge badge-core">PART VI</span>
        <h1>CÂY VÀ CÂY NHỊ PHÂN (TREES & BINARY TREES)</h1>
    </div>

    <h2>1. Định nghĩa & Thuật ngữ (FORMAL MODEL)</h2>
    <ul>
        <li><strong>Root (Gốc)</strong>: Nút duy nhất không có nút cha.</li>
        <li><strong>Leaf (Lá)</strong>: Nút không có con nào (bậc của nút bằng 0).</li>
        <li><strong>Degree (Bậc)</strong>: Số nút con của một nút.</li>
        <li><span class="badge badge-uit-convention">IT003 CONVENTION</span> <strong>Level (Mức)</strong>: Nút gốc Root nằm ở <strong>Level 0</strong> (hoặc Level 1 tùy đề bài chỉ định rõ, mặc định UIT slide tính Root ở Level 0). Height of tree $H = \text{max\_level} + 1$.</li>
    </ul>

    <h2>2. Các Phép Duyệt Cây Nhị Phân (Binary Tree Traversals)</h2>
    <p>Có 6 cách duyệt tổ hợp $(N, L, R)$, trong đó 3 cách duyệt tiền tự, trung tự, hậu tự là quan trọng nhất:</p>

    <ul>
        <li><strong>NLR (Pre-order / Tiền tự)</strong>: Thăm Nút gốc $N \rightarrow$ Duyệt Cây con trái $L \rightarrow$ Duyệt Cây con phải $R$.</li>
        <li><strong>LNR (In-order / Trung tự)</strong>: Duyệt Cây con trái $L \rightarrow$ Thăm Nút gốc $N \rightarrow$ Duyệt Cây con phải $R$. (Cho kết quả tăng dần trên BST!).</li>
        <li><strong>LRN (Post-order / Hậu tự)</strong>: Duyệt Cây con trái $L \rightarrow$ Duyệt Cây con phải $R \rightarrow$ Thăm Nút gốc $N$.</li>
    </ul>

    <h3>C++ Recursive Traversals</h3>
    <pre><code>struct TreeNode {
    int data;
    TreeNode* pLeft;
    TreeNode* pRight;
};

void preOrder(TreeNode* root) {
    if (root != nullptr) {
        cout << root->data << " ";
        preOrder(root->pLeft);
        preOrder(root->pRight);
    }
}

void inOrder(TreeNode* root) {
    if (root != nullptr) {
        inOrder(root->pLeft);
        cout << root->data << " ";
        inOrder(root->pRight);
    }
}

void postOrder(TreeNode* root) {
    if (root != nullptr) {
        postOrder(root->pLeft);
        postOrder(root->pRight);
        cout << root->data << " ";
    }
}</code></pre>
</section>
"""
    with open(os.path.join(CHAPTERS_DIR, "06_TREES_BINARY_TREES.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote 06_TREES_BINARY_TREES.html")

def write_ch07():
    content = """<section class="chapter" id="ch07">
    <div class="chapter-header">
        <span class="badge badge-core">PART VII</span>
        <h1>CÂY NHỊ PHÂN TÌM KIẾM (BINARY SEARCH TREE - BST)</h1>
    </div>

    <h2>1. Tính chất Đặc trưng (INVARIANT)</h2>
    <p>Một Cây nhị phân là <strong>BST</strong> khi và chỉ khi với mọi nút $X$ trên cây:</p>
    <ul>
        <li>Tất cả các nút thuộc cây con trái của $X$ đều có khóa <strong>nhỏ hơn</strong> khóa của $X$.</li>
        <li>Tất cả các nút thuộc cây con phải của $X$ đều có khóa <strong>lớn hơn</strong> khóa của $X$.</li>
    </ul>

    <h2>2. Thao tác Xóa Nút trên BST (Delete Operation)</h2>
    <p>Xóa một nút $X$ khỏi BST được chia thành 3 trường hợp:</p>

    <ol>
        <li><strong>Trường hợp 1: $X$ là nút lá (Leaf)</strong>: Xóa trực tiếp $X$ và gán con trỏ của cha chỉ tới $X$ thành `nullptr`.</li>
        <li><strong>Trường hợp 2: $X$ có đúng 1 con</strong>: Cho con trỏ từ cha của $X$ trỏ trực tiếp tới nút con duy nhất của $X$, sau đó `delete X`.</li>
        <li><strong>Trường hợp 3: $X$ có đủ 2 con</strong>:
            <br><span class="badge badge-uit-convention">IT003 CONVENTION</span>: Tìm phần tử thế mạng $Y$:
            <br>• Option A: <strong>Nút cực phải của cây con trái</strong> (Rightmost of Left Subtree - phần tử lớn nhất bên trái).
            <br>• Option B: <strong>Nút cực trái của cây con phải</strong> (Leftmost of Right Subtree - phần tử nhỏ nhất bên phải).
            <br>Copy dữ liệu từ $Y$ sang $X$, sau đó gọi đệ quy xóa $Y$ (khi này $Y$ chỉ có tối đa 1 con!).
        </li>
    </ol>

    <h3>C++ Implementation for BST Deletion</h3>
    <pre><code>TreeNode* findMin(TreeNode* root) {
    while (root->pLeft != nullptr) root = root->pLeft;
    return root;
}

TreeNode* deleteNode(TreeNode* root, int key) {
    if (root == nullptr) return root;

    if (key < root->data) {
        root->pLeft = deleteNode(root->pLeft, key);
    } else if (key > root->data) {
        root->pRight = deleteNode(root->pRight, key);
    } else {
        // Nút cần xóa tìm thấy tại root
        if (root->pLeft == nullptr) {
            TreeNode* temp = root->pRight;
            delete root;
            return temp;
        } else if (root->pRight == nullptr) {
            TreeNode* temp = root->pLeft;
            delete root;
            return temp;
        }
        // Có 2 con: Dùng Leftmost of Right Subtree (Min Right)
        TreeNode* temp = findMin(root->pRight);
        root->data = temp->data;
        root->pRight = deleteNode(root->pRight, temp->data);
    }
    return root;
}</code></pre>
</section>
"""
    with open(os.path.join(CHAPTERS_DIR, "07_BST.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote 07_BST.html")

def write_ch08():
    content = """<section class="chapter" id="ch08">
    <div class="chapter-header">
        <span class="badge badge-core">PART VIII</span>
        <h1>CÂY CÂN BẰNG AVL (AVL TREES)</h1>
    </div>

    <h2>1. Chỉ số Cân bằng (Balance Factor)</h2>
    <p>Cây AVL là BST tự cân bằng. Chỉ số cân bằng của nút $X$ được tính bằng:</p>

    $$BF(X) = h_{left} - h_{right}$$

    <p>Điều kiện AVL: $BF(X) \in \{-1, 0, +1\}$ với mọi nút $X$. Khi $|BF(X)| \ge 2$, cây bị mất cân bằng tại $X$ và cần thực hiện phép <strong>Xoay (Rotation)</strong> để khôi phục cân bằng.</p>

    <h2>2. Bốn Trường Hợp Xoay Chuẩn (AVL Rotation Cheat Sheet)</h2>

    <div class="callout">
        <div class="callout-title">🔄 Rotation Matrix</div>
        <table>
            <thead>
                <tr>
                    <th>Trường hợp</th>
                    <th>Dấu hiệu $BF(A)$ & $BF(Child)$</th>
                    <th>Phép Xoay Khôi Phục</th>
                    <th>Mô tả Thao tác</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>LL (Left-Left)</strong></td>
                    <td>$BF(A) = +2$, $BF(Left) \ge 0$</td>
                    <td><strong>Xoay Đơn Phải (Rotate Right) tại A</strong></td>
                    <td>Con trái đưa lên làm cha của A, cây con giữa sang trái A.</td>
                </tr>
                <tr>
                    <td><strong>RR (Right-Right)</strong></td>
                    <td>$BF(A) = -2$, $BF(Right) \le 0$</td>
                    <td><strong>Xoay Đơn Trái (Rotate Left) tại A</strong></td>
                    <td>Con phải đưa lên làm cha của A, cây con giữa sang phải A.</td>
                </tr>
                <tr>
                    <td><strong>LR (Left-Right)</strong></td>
                    <td>$BF(A) = +2$, $BF(Left) = -1$</td>
                    <td><strong>Xoay Kép LR</strong> (Rotate Left tại Left Child, rồi Rotate Right tại A)</td>
                    <td>Thực hiện 2 bước xoay để đưa nút cháu lên làm cha.</td>
                </tr>
                <tr>
                    <td><strong>RL (Right-Left)</strong></td>
                    <td>$BF(A) = -2$, $BF(Right) = +1$</td>
                    <td><strong>Xoay Kép RL</strong> (Rotate Right tại Right Child, rồi Rotate Left tại A)</td>
                    <td>Thực hiện 2 bước xoay để đưa nút cháu lên làm cha.</td>
                </tr>
            </tbody>
        </table>
    </div>

    <h3>C++ Rotation Helper Code</h3>
    <pre><code>int getHeight(TreeNode* n) {
    if (n == nullptr) return 0;
    return n->height; // Giả sử struct lưu trường height
}

int getBalance(TreeNode* n) {
    if (n == nullptr) return 0;
    return getHeight(n->pLeft) - getHeight(n->pRight);
}

TreeNode* rotateRight(TreeNode* y) {
    TreeNode* x = y->pLeft;
    TreeNode* T2 = x->pRight;

    x->pRight = y;
    y->pLeft = T2;

    y->height = max(getHeight(y->pLeft), getHeight(y->pRight)) + 1;
    x->height = max(getHeight(x->pLeft), getHeight(x->pRight)) + 1;

    return x; // Root mới
}</code></pre>
</section>
"""
    with open(os.path.join(CHAPTERS_DIR, "08_AVL.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote 08_AVL.html")

def write_ch09():
    content = """<section class="chapter" id="ch09">
    <div class="chapter-header">
        <span class="badge badge-core">PART IX</span>
        <h1>HEAPS VÀ HÀNG ĐỢI ƯU TIÊN (HEAP & PRIORITY QUEUE)</h1>
    </div>

    <h2>1. Max-Heap & Min-Heap Invariants</h2>
    <p><strong>Max-Heap</strong> là một Cây nhị phân hoàn chỉnh (Complete Binary Tree), trong đó khóa của mọi nút cha đều <strong>lớn hơn hoặc bằng</strong> khóa của các nút con của nó. Phần tử cực đại luôn nằm tại Nút gốc (Root index 0).</p>

    <h2>2. Công thức Lưu trữ mảng (Array Representation)</h2>
    <p><span class="badge badge-uit-convention">IT003 CONVENTION</span>: Khi biểu diễn Heap trên mảng bắt đầu từ chỉ số `0` đến `n-1`:</p>
    <ul>
        <li>Nút cha của $i$: $\text{parent}(i) = \lfloor \frac{i-1}{2} \rfloor$.</li>
        <li>Con trái của $i$: $\text{left}(i) = 2i + 1$.</li>
        <li>Con phải của $i$: $\text{right}(i) = 2i + 2$.</li>
    </ul>

    <h3>C++ Heapify Operation</h3>
    <pre><code>void heapify(int a[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && a[left] > a[largest])
        largest = left;
    if (right < n && a[right] > a[largest])
        largest = right;

    if (largest != i) {
        swap(a[i], a[largest]);
        heapify(a, n, largest);
    }
}</code></pre>
</section>
"""
    with open(os.path.join(CHAPTERS_DIR, "09_HEAP_PRIORITY_QUEUE.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote 09_HEAP_PRIORITY_QUEUE.html")

def write_ch10():
    content = """<section class="chapter" id="ch10">
    <div class="chapter-header">
        <span class="badge badge-core">PART X</span>
        <h1>CÂY B-TREE (B-TREES - MULTI-WAY SEARCH TREES)</h1>
    </div>

    <h2>1. Quy tắc Cây B-Tree Bậc $m$ (B-Tree of Order $m$)</h2>
    <p><span class="badge badge-uit-convention">IT003 CONVENTION</span>: Đề thi IT003 cực kỳ tập trung vào <strong>B-Tree bậc 5 ($m=5$)</strong>. Các quy tắc số lượng khóa và con bắt buộc phải ghi nhớ:</p>

    <div class="callout">
        <div class="callout-title">📏 Ràng buộc B-Tree bậc $m = 5$</div>
        <ul>
            <li>Số khóa tối đa trong 1 nút: $m - 1 = 4$ khóa.</li>
            <li>Số con tối đa của 1 nút: $m = 5$ con.</li>
            <li>Số khóa tối thiểu của nút không phải gốc: $\lceil m/2 \rceil - 1 = \lceil 2.5 \rceil - 1 = 2$ khóa.</li>
            <li>Số con tối thiểu của nút không phải gốc: $\lceil m/2 \rceil = 3$ con.</li>
            <li>Nút gốc (Root): Có ít nhất 1 khóa (nếu cây không rỗng) và tối thiểu 2 con.</li>
            <li>Tất cả các nút lá đều nằm trên <strong>cùng một mức (cùng độ sâu)</strong>.</li>
        </ul>
    </div>

    <h2>2. Thao tác Chèn & Tách Nút (Insertion & Splitting Mechanic)</h2>
    <p>Khi chèn một khóa mới vào nút lá đã có sẵn 4 khóa (tổng thành 5 khóa $[k_1, k_2, k_3, k_4, k_5]$):</p>
    <ol>
        <li>Nút bị tràn (Overflow). Khóa trung vị $k_3$ (khóa thứ 3 sau khi sắp xếp) được **đẩy nổi (Promote)** lên nút cha.</li>
        <li>Nút bị **Tách (Split)** thành 2 nút con mới: Nút trái chứa $[k_1, k_2]$, nút phải chứa $[k_4, k_5]$.</li>
        <li>Nếu nút cha tiếp tục bị tràn 5 khóa, quá trình Split & Promote được lan truyền tiếp lên phía gốc (có thể làm tăng chiều cao cây lên 1 mức khi gốc bị split).</li>
    </ol>
</section>
"""
    with open(os.path.join(CHAPTERS_DIR, "10_BTREE.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote 10_BTREE.html")

def write_ch11():
    content = """<section class="chapter" id="ch11">
    <div class="chapter-header">
        <span class="badge badge-core">PART XI</span>
        <h1>BẢNG BĂM (HASH TABLE)</h1>
    </div>

    <h2>1. Hàm Băm & Giải Quyết Đụng Độ (Collision Resolution)</h2>
    <p>Hàm băm thường dùng trong đề thi IT003: $h(k) = k \bmod M$, với $M$ là kích thước bảng băm.</p>

    <h3>Bốn Phương Pháp Giải Quyết Đụng Độ Chuẩn IT003:</h3>
    <ol>
        <li><strong>Dò tuyến tính (Linear Probing)</strong>:
            $$h(k, i) = (h(k) + i) \bmod M, \quad i = 0, 1, 2, \dots$$
        </li>
        <li><strong>Dò bậc hai (Quadratic Probing)</strong>:
            $$h(k, i) = (h(k) + c_1 i + c_2 i^2) \bmod M \quad \text{hoặc} \quad (h(k) + i^2) \bmod M$$
        </li>
        <li><strong>Băm kép (Double Hashing)</strong>:
            $$h(k, i) = (h_1(k) + i \cdot h_2(k)) \bmod M, \quad h_2(k) = R - (k \bmod R)$$
        </li>
        <li><strong>Phần tử kết nối (Separate Chaining)</strong>: Mỗi ô trong bảng băm là một Danh sách liên kết đơn chứa các phần tử đụng độ.</li>
    </ol>

    <h2>2. Tính Số Phép So Sánh Tìm Kiếm (Comparison Count)</h2>
    <div class="callout callout-warning">
        <span class="badge badge-exam-style">IT003 EXAM STYLE</span>
        <p><strong>Bẫy Đề Thi:</strong></p>
        <ul>
            <li><strong>Tìm kiếm Thành công ($C_{\text{succ}}$)</strong>: Tính trung bình số lần so sánh để tìm thấy các khóa $k$ đang có trong bảng.</li>
            <li><strong>Tìm kiếm Thất bại ($C_{\text{unsucc}}$)</strong>: Tính trung bình số lần so sánh bắt đầu từ ô index $i \in [0, M-1]$ duyệt qua các ô đụng độ cho đến khi **gặp ô trống (`EMPTY`) đầu tiên**. Lưu ý: Ô bị xóa (`DELETED`) <strong>KHÔNG được dừng</strong> tìm kiếm thất bại!</li>
        </ul>
    </div>
</section>
"""
    with open(os.path.join(CHAPTERS_DIR, "11_HASH_TABLE.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote 11_HASH_TABLE.html")

def write_ch12():
    content = """<section class="chapter" id="ch12">
    <div class="chapter-header">
        <span class="badge badge-core">PART XII</span>
        <h1>ĐỒ THỊ VÀ BIỂU DIỄN ĐỒ THỊ (GRAPHS & REPRESENTATIONS)</h1>
    </div>

    <h2>1. Định nghĩa & Biểu diễn (Adjacency Matrix vs List)</h2>
    <p>Đồ thị $G = (V, E)$ gồm tập đỉnh $V$ và tập cạnh $E$. Biểu diễn đồ thị có 2 phương pháp chính:</p>

    <ul>
        <li><strong>Ma trận kề (Adjacency Matrix)</strong>: Mảng 2 chiều $A[V][V]$. Tốn $\mathcal{O}(V^2)$ bộ nhớ. Kiểm tra $(u, v) \in E$ tốn $\mathcal{O}(1)$.</li>
        <li><strong>Danh sách kề (Adjacency List)</strong>: Mảng các danh sách liên kết. Tốn $\mathcal{O}(V + E)$ bộ nhớ. Phù hợp cho đồ thị thưa (Sparse Graph).</li>
    </ul>
</section>
"""
    with open(os.path.join(CHAPTERS_DIR, "12_GRAPH.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote 12_GRAPH.html")

def write_ch13():
    content = """<section class="chapter" id="ch13">
    <div class="chapter-header">
        <span class="badge badge-core">PART XIII</span>
        <h1>DUYỆT ĐỒ THỊ (BFS & DFS TRAVERSALS)</h1>
    </div>

    <h2>1. BFS — Duyệt Theo Chiều Rộng (Breadth-First Search)</h2>
    <p>BFS sử dụng cấu trúc dữ liệu <strong>Queue (FIFO)</strong>. Giúp tìm đường đi ngắn nhất trên đồ thị không trọng số.</p>

    <h3>C++ BFS Code</h3>
    <pre><code>void BFS(int startNode, const vector<vector<int>>& adj, int V) {
    vector<bool> visited(V, false);
    queue<int> q;

    visited[startNode] = true;
    q.push(startNode);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        cout << u << " ";

        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
}</code></pre>

    <h2>2. DFS — Duyệt Theo Chiều Sâu (Depth-First Search)</h2>
    <p>DFS sử dụng cấu trúc dữ liệu <strong>Stack (LIFO)</strong> hoặc Đệ quy.</p>

    <h3>C++ DFS Recursive Code</h3>
    <pre><code>void DFSUtil(int u, const vector<vector<int>>& adj, vector<bool>& visited) {
    visited[u] = true;
    cout << u << " ";

    for (int v : adj[u]) {
        if (!visited[v]) {
            DFSUtil(v, adj, visited);
        }
    }
}</code></pre>
</section>
"""
    with open(os.path.join(CHAPTERS_DIR, "13_BFS_DFS.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote 13_BFS_DFS.html")

def write_ch14():
    content = """<section class="chapter" id="ch14">
    <div class="chapter-header">
        <span class="badge badge-core">PART XIV</span>
        <h1>THUẬT TOÁN ĐƯỜNG ĐI NGẮN NHẤT (SHORTEST PATH - DIJKSTRA)</h1>
    </div>

    <h2>1. Thuật toán Dijkstra (Single-Source Shortest Path)</h2>
    <p>Dijkstra tìm đường đi ngắn nhất từ đỉnh nguồn $s$ tới tất cả các đỉnh còn lại trên đồ thị có <strong>trọng số không âm ($w(e) \ge 0$)</strong>.</p>

    <h2>2. Bảng Tracing Chạy Tay Chuẩn Thi IT003</h2>
    <p><span class="badge badge-exam-style">IT003 EXAM STYLE</span>: Trình bày bảng Dijkstra qua từng bước giải phóng đỉnh (Relaxation step):</p>

    <table>
        <thead>
            <tr>
                <th>Bước</th>
                <th>Tập $S$ (Đã chọn)</th>
                <th>$d[A]$</th>
                <th>$d[B]$</th>
                <th>$d[C]$</th>
                <th>$d[D]$</th>
                <th>$d[E]$</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>0</td><td>$\emptyset$</td><td>0 (A)</td><td>$\infty$</td><td>$\infty$</td><td>$\infty$</td><td>$\infty$</td></tr>
            <tr><td>1</td><td>{A}</td><td>0</td><td>4 (A)</td><td>2 (A)</td><td>$\infty$</td><td>$\infty$</td></tr>
            <tr><td>2</td><td>{A, C}</td><td>0</td><td>3 (C)</td><td>2</td><td>7 (C)</td><td>$\infty$</td></tr>
            <tr><td>3</td><td>{A, C, B}</td><td>0</td><td>3</td><td>2</td><td>5 (B)</td><td>6 (B)</td></tr>
        </tbody>
    </table>
</section>
"""
    with open(os.path.join(CHAPTERS_DIR, "14_SHORTEST_PATH.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote 14_SHORTEST_PATH.html")

def write_ch15():
    content = """<section class="chapter" id="ch15">
    <div class="chapter-header">
        <span class="badge badge-core">PART XV</span>
        <h1>EXAM TOOLKIT & BỘ ĐỀ ÔN THI MÔN IT003</h1>
    </div>

    <h2>1. Quick Recall Cheat Sheet</h2>
    <ul>
        <li><strong>Selection Sort</strong>: Phép so sánh luôn $C = n(n-1)/2$. Phép đổi chỗ tối đa $n-1$. Không ổn định.</li>
        <li><strong>Binary Search</strong>: Mảng phải sắp xếp. Độ phức tạp $O(\log n)$.</li>
        <li><strong>BST Deletion 2 children</strong>: Thay bằng Max-Left hoặc Min-Right. Thao tác an toàn pointer.</li>
        <li><strong>AVL Imbalance</strong>: Dấu $BF(A) = +2 \Rightarrow$ LL hoặc LR. Dấu $BF(A) = -2 \Rightarrow$ RR hoặc RL.</li>
        <li><strong>B-Tree bậc 5</strong>: Max 4 keys, Min 2 keys. Split đẩy nổi khóa thứ 3 (trung vị).</li>
        <li><strong>Hash Table Unsuccessful Search</strong>: Dừng lại khi gặp ô `EMPTY` đầu tiên. Ô `DELETED` tiếp tục dò.</li>
    </ul>

    <h2>2. Integrated Exam Practice Bank (Level 0 to Level 5)</h2>
    <div class="callout">
        <div class="callout-title">📝 Bài tập Dạng Thi Mẫu IT003 (Exam Style)</div>
        <p><strong>Câu 1 (2.5 điểm)</strong>: Cho dãy số $A = [25, 12, 40, 8, 30, 15]$. Chạy tay thuật toán Quick Sort với Pivot là phần tử cuối mảng `high`. Trình bày trạng thái mảng sau từng bước phân hoạch.</p>
        <p><strong>Câu 2 (2.5 điểm)</strong>: Lần lượt chèn các khóa sau vào cây AVL rỗng: $18, 10, 25, 6, 14, 20, 28, 12$. Xác định nút mất cân bằng đầu tiên, chỉ rõ loại xoay (LL/RR/LR/RL) và vẽ cây AVL hoàn chỉnh sau mỗi bước xoay.</p>
    </div>
</section>
"""
    with open(os.path.join(CHAPTERS_DIR, "15_EXAM_TOOLKIT.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote 15_EXAM_TOOLKIT.html")

def main():
    write_ch05()
    write_ch06()
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
