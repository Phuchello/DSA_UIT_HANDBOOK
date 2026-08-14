import os
import sys
import io
import json
import glob
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

RESEARCH_DIR = r"C:\Users\lyle3\.gemini\antigravity\scratch\IT003_DSA_BOOK\research"
EXTRACTED_DIR = os.path.join(RESEARCH_DIR, "extracted")

TOPICS = [
    "Complexity & Analysis",
    "Searching Algorithms",
    "Sorting Algorithms",
    "Linked Lists",
    "Stack & Queue",
    "Trees & Binary Trees",
    "Binary Search Trees (BST)",
    "AVL Trees",
    "Heaps & Priority Queues",
    "B-Trees",
    "Hash Tables",
    "Graphs & Representations",
    "Graph Traversal (BFS/DFS)",
    "Shortest Path (Dijkstra/Bellman/Floyd)"
]

def analyze_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    char_len = len(text)
    lower_text = text.lower()

    # Classification
    source_type = "Secondary UIT"
    reliability = "High"
    it003_relevance = "High"
    exam_relevance = "Medium"

    if any(k in lower_text for k in ["đề thi", "đáp án", "giữa kỳ", "cuối kỳ", "ck", "gk", "đề-1"]):
        source_type = "Exam"
        exam_relevance = "CRITICAL"
        reliability = "Official Exam"
    elif "vothuongphuc" in lower_text or "vo_trong_phuc" in lower_text or "votrongphuc" in lower_text:
        source_type = "Primary UIT (Võ Trọng Phúc High-Score)"
        reliability = "High (Top Student / Verified Refit)"
        exam_relevance = "High"
    elif "ctdl_" in lower_text or "slide" in lower_text or "chương" in lower_text:
        source_type = "Primary UIT (Official Lecture Slides)"
        reliability = "Official Curriculum"
        exam_relevance = "High"
    elif "bht cnpm" in lower_text or "emily" in lower_text or "btvn" in lower_text:
        source_type = "Student notes / Practice"
        reliability = "Medium (Student Reference)"
        exam_relevance = "Medium"

    # Identify topics
    detected_topics = []
    if any(k in lower_text for k in ["big-o", "độ phức tạp", "o(n", "o(1", "thời gian thực thi"]):
        detected_topics.append("Complexity & Analysis")
    if any(k in lower_text for k in ["tìm kiếm", "binary search", "linear search", "nhi phan"]):
        detected_topics.append("Searching Algorithms")
    if any(k in lower_text for k in ["sắp xếp", "selection", "quick sort", "merge sort", "heap sort", "interchange", "bubble", "insertion", "radix"]):
        detected_topics.append("Sorting Algorithms")
    if any(k in lower_text for k in ["danh sách liên kết", "linked list", "phead", "ptail", "node"]):
        detected_topics.append("Linked Lists")
    if any(k in lower_text for k in ["stack", "queue", "ngăn xếp", "hàng đợi", "lifo", "fifo", "circular"]):
        detected_topics.append("Stack & Queue")
    if any(k in lower_text for k in ["cây", "tree", "binary tree", "gốc", "mức", "mức 0", "mức 1"]):
        detected_topics.append("Trees & Binary Trees")
    if any(k in lower_text for k in ["bst", "tìm kiếm nhị phân", "nhi phan tim kiem"]):
        detected_topics.append("Binary Search Trees (BST)")
    if any(k in lower_text for k in ["avl", "xoay", "balance factor", "cân bằng"]):
        detected_topics.append("AVL Trees")
    if any(k in lower_text for k in ["heap", "vun đống", "priority queue"]):
        detected_topics.append("Heaps & Priority Queues")
    if any(k in lower_text for k in ["b-tree", "btree", "bậc", "order"]):
        detected_topics.append("B-Trees")
    if any(k in lower_text for k in ["bảng băm", "hash", "probing", "băm", "đụng độ", "collision"]):
        detected_topics.append("Hash Tables")
    if any(k in lower_text for k in ["đồ thị", "graph", "đỉnh", "cạnh", "ma trận kề", "danh sách kề"]):
        detected_topics.append("Graphs & Representations")
    if any(k in lower_text for k in ["bfs", "dfs", "duyệt theo chiều rộng", "duyệt theo chiều sâu"]):
        detected_topics.append("Graph Traversal (BFS/DFS)")
    if any(k in lower_text for k in ["dijkstra", "bellman", "floyd", "đường đi ngắn nhất", "shortest path"]):
        detected_topics.append("Shortest Path (Dijkstra/Bellman/Floyd)")

    return {
        "filename": filename,
        "char_len": char_len,
        "type": source_type,
        "reliability": reliability,
        "it003_relevance": it003_relevance,
        "exam_relevance": exam_relevance,
        "topics": detected_topics,
        "snippet": text[:300].replace("\n", " ")
    }

def main():
    files = glob.glob(os.path.join(EXTRACTED_DIR, "*.txt"))
    results = [analyze_file(f) for f in files]
    
    analysis_file = os.path.join(RESEARCH_DIR, "detailed_source_analysis.json")
    with open(analysis_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"Analyzed {len(results)} extracted source files.")

if __name__ == "__main__":
    main()
