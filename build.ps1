$chapters = @(
    "00_HOW_TO_MASTER_IT003.html",
    "01_ALGORITHM_ANALYSIS.html",
    "02_SEARCHING.html",
    "03_SORTING.html",
    "04_LINKED_LIST.html",
    "05_STACK_QUEUE.html",
    "06_TREES_BINARY_TREES.html",
    "07_BST.html",
    "08_AVL.html",
    "09_HEAP_PRIORITY_QUEUE.html",
    "10_BTREE.html",
    "11_HASH_TABLE.html",
    "12_GRAPH.html",
    "13_BFS_DFS.html",
    "14_SHORTEST_PATH.html",
    "15_EXAM_TOOLKIT.html"
)

$header = @'
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IT003 DSA UIT — Ultimate Handbook</title>
    <link rel="stylesheet" href="print.css">
    <!-- KaTeX Math Rendering -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
</head>
<body>

<div class="cover-page">
    <div style="text-align: center; padding: 40px 20px;">
        <span class="badge badge-uit-convention" style="font-size: 11pt; padding: 4px 12px;">ĐẠI HỌC QUỐC GIA TP. HỒ CHÍ MINH — TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN</span>
        <h1 style="font-size: 26pt; margin-top: 30px; border-bottom: none; color: #0f172a;">IT003: CẤU TRÚC DỮ LIỆU VÀ GIẢI THUẬT</h1>
        <h2 style="font-size: 18pt; color: #1e40af; border-bottom: none; margin-top: 0;">ULTIMATE HANDBOOK & EXAM REVISION GUIDE</h2>
        <p style="font-size: 11pt; color: #64748b; margin-top: 20px;">Tài liệu Giảng dạy, Cẩm nang Tra cứu & Bộ Đề Thi Mẫu Chuẩn UIT</p>
    </div>
</div>

<div class="toc-container" style="background: #f8fafc; padding: 20px; border-radius: 8px; margin-bottom: 30px; border: 1px solid #cbd5e1;">
    <h2 style="margin-top: 0;">MỤC LỤC TỔNG QUAN (TABLE OF CONTENTS)</h2>
    <ol style="line-height: 1.8;">
        <li><a href="#ch00"><strong>PART 0</strong>: Cách học và Chinh phục môn IT003 (Roadmap & Progression)</a></li>
        <li><a href="#ch01"><strong>PART I</strong>: Phân tích Thuật toán & Độ phức tạp (Big-O, Loop Analysis)</a></li>
        <li><a href="#ch02"><strong>PART II</strong>: Thuật toán Tìm kiếm (Linear & Binary Search)</a></li>
        <li><a href="#ch03"><strong>PART III</strong>: Các Thuật toán Sắp xếp (10 Sorting Algorithms & Complexity Matrix)</a></li>
        <li><a href="#ch04"><strong>PART IV</strong>: Danh sách Liên kết (Singly & Doubly Linked List)</a></li>
        <li><a href="#ch05"><strong>PART V</strong>: Ngăn xếp & Hàng đợi (Stack, Queue & Circular Queue)</a></li>
        <li><a href="#ch06"><strong>PART VI</strong>: Cây & Cây Nhị phân (Trees & Binary Tree Traversals)</a></li>
        <li><a href="#ch07"><strong>PART VII</strong>: Cây Nhị phân Tìm kiếm (BST Search, Insert & Deletion)</a></li>
        <li><a href="#ch08"><strong>PART VIII</strong>: Cây Cân bằng AVL (Balance Factors & 4 Rotations Cheat Sheet)</a></li>
        <li><a href="#ch09"><strong>PART IX</strong>: Heaps & Hàng đợi Ưu tiên (Max/Min Heap & Array Indexing)</a></li>
        <li><a href="#ch10"><strong>PART X</strong>: Cây B-Tree (Order 5 B-Tree Split & Promotion Rules)</a></li>
        <li><a href="#ch11"><strong>PART XI</strong>: Bảng Băm (Hash Table, Probing & Unsuccessful Search Comparisons)</a></li>
        <li><a href="#ch12"><strong>PART XII</strong>: Đồ thị & Biểu diễn (Adjacency Matrix vs Adjacency List)</a></li>
        <li><a href="#ch13"><strong>PART XIII</strong>: Duyệt Đồ thị (BFS with Queue & DFS with Stack/Recursion)</a></li>
        <li><a href="#ch14"><strong>PART XIV</strong>: Đường đi Ngắn nhất (Dijkstra Algorithm & Tracing Table)</a></li>
        <li><a href="#ch15"><strong>PART XV</strong>: Exam Toolkit & Bộ Đề Ôn Thi Mẫu Chuẩn IT003</a></li>
    </ol>
</div>
'@

$footer = @'
<script>
document.addEventListener("DOMContentLoaded", function() {
    if (window.renderMathInElement) {
        renderMathInElement(document.body, {
            delimiters: [
                {left: "$$", right: "$$", display: true},
                {left: "$", right: "$", display: false},
                {left: "\\(", right: "\\)", display: false},
                {left: "\\[", right: "\\]", display: true}
            ],
            throwOnError: false
        });
    }
});
</script>
</body>
</html>
'@

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText("master.html", $header, $utf8NoBom)

foreach ($file in $chapters) {
    $content = Get-Content -Path "chapters\$file" -Raw -Encoding UTF8
    [System.IO.File]::AppendAllText("master.html", "`n" + $content + "`n", $utf8NoBom)
}

[System.IO.File]::AppendAllText("master.html", $footer, $utf8NoBom)
Write-Host "Master HTML assembled successfully"
