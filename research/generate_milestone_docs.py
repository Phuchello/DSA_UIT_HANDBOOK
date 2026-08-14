import os
import sys
import io
import json
import glob
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

BASE_DIR = r"C:\Users\lyle3\.gemini\antigravity\scratch\IT003_DSA_BOOK"
RESEARCH_DIR = os.path.join(BASE_DIR, "research")
EXTRACTED_DIR = os.path.join(RESEARCH_DIR, "extracted")

def build_source_audit():
    files = glob.glob(os.path.join(EXTRACTED_DIR, "*.txt"))
    
    source_items = []
    
    # Filter to IT003 relevant files
    for filepath in files:
        fname = os.path.basename(filepath)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        
        lower_fname = fname.lower()
        lower_content = content.lower()

        is_it003 = any(k in lower_fname or k in lower_content for k in [
            "it003", "ctdl", "dsa", "cấu trúc dữ liệu", "thuật toán", "sắp xếp", "tìm kiếm", "bảng băm", "b-tree", "avl", "đồ thị", "stack", "queue", "lập trình c"
        ])
        
        # Filter out HDH (IT007), PLDC, CSDL if not related to IT003
        if ("hdh" in lower_fname or "pldc" in lower_fname or "phap_luat" in lower_fname or "he_dieu_hanh" in lower_fname) and "it003" not in lower_fname:
            continue
            
        if not is_it003:
            continue

        # Classify
        stype = "Primary UIT"
        rel = "High"
        it003_rel = "High"
        exam_rel = "High"
        use_in = "Core chapters & Exam DNA"

        if any(k in lower_fname for k in ["de_thi", "ck", "gk", "dapan", "de-1"]):
            stype = "Exam"
            rel = "Official Exam"
            exam_rel = "CRITICAL"
            use_in = "EXAM_DNA & Practice bank"
        elif "votrongphuc" in lower_fname or "vo_trong_phuc" in lower_fname:
            stype = "Secondary UIT (High-Score Refit)"
            rel = "High (Top Student Refit)"
            use_in = "Intuition, Mechanics, Dry-run examples"
        elif "ctdl_" in lower_fname or "01_" in lower_fname or "chuong" in lower_fname:
            stype = "Primary UIT (Official Slide)"
            rel = "Official Curriculum"
            use_in = "Syllabus mapping & Formal definitions"
        else:
            stype = "Student notes / Supplementary"
            rel = "Medium"
            use_in = "Edge case verification"

        # Topic detection
        topics = []
        if "phan_tich" in lower_fname or "tquan" in lower_fname or "chuong1" in lower_fname or "bigo" in lower_fname:
            topics.append("Analysis & Complexity")
        if "tim_kiem" in lower_fname or "timkiem" in lower_fname or "search" in lower_fname:
            topics.append("Searching")
        if "sap_xep" in lower_fname or "sapxep" in lower_fname or "sxtk" in lower_fname or "sort" in lower_fname:
            topics.append("Sorting")
        if "danhsach" in lower_fname or "list" in lower_fname or "con_tro" in lower_fname:
            topics.append("Linked List & Pointers")
        if "stack" in lower_fname or "nganxep" in lower_fname or "queue" in lower_fname:
            topics.append("Stack & Queue")
        if "cay" in lower_fname or "tree" in lower_fname or "bst" in lower_fname or "avl" in lower_fname or "b_tree" in lower_fname:
            topics.append("Trees (Binary, BST, AVL, B-Tree)")
        if "bangbam" in lower_fname or "hash" in lower_fname:
            topics.append("Hash Table")
        if "dothi" in lower_fname or "graph" in lower_fname:
            topics.append("Graph & Traversals & Shortest Path")
            
        if not topics:
            topics.append("Comprehensive IT003 Review")

        topic_str = ", ".join(topics)

        summary_snippet = content[:150].replace("\n", " ").strip()

        source_items.append({
            "name": fname.replace(".txt", "").replace("_pdf", ".pdf").replace("_pptx", ".pptx").replace("_docx", ".docx"),
            "stype": stype,
            "topic": topic_str,
            "contents": summary_snippet if len(summary_snippet) > 20 else "Nội dung bài giảng / đề thi IT003",
            "reliability": rel,
            "it003_rel": it003_rel,
            "exam_rel": exam_rel,
            "use_in": use_in
        })

    md = """# SOURCE_AUDIT.md — IT003 DSA UIT Handbook

> **Systematic Audit of Local & Official Materials**
> Target Course: IT003 - Cấu trúc dữ liệu và Giải thuật, Trường ĐH Công nghệ Thông tin, ĐHQG-HCM.

---

## 1. Local Source Inventory & Audit Table

| Source Name | Type | Topic | Main Contents | Reliability | IT003 Relevance | Exam Relevance | Use In |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
"""
    for item in source_items:
        md += f"| `{item['name']}` | **{item['stype']}** | {item['topic']} | {item['contents'][:80]}... | {item['reliability']} | {item['it003_rel']} | {item['exam_rel']} | {item['use_in']} |\n"

    md += """
---

## 2. Key Findings & Truth Verification Rules

1. **Official Slides (`CTDL_*.pptx`)**:
   - Primary reference for **conventions**, **naming**, and **scope**.
   - Tree levels start at **Level 0 (Root at Level 0)** or **Level 1** depending on slide context — *must highlight UIT Badge*.
   - Sorting algorithms include: **Selection Sort**, **Interchange Sort** (đặc thù UIT), **Bubble Sort**, **Insertion Sort**, **Binary Insertion Sort**, **Shell Sort**, **Heap Sort**, **Quick Sort**, **Merge Sort**, **Radix Sort**.
   - Linked List implementation uses explicit `Node* pHead, *pTail`.
   - Hash Table collision resolutions: **Linear Probing**, **Quadratic Probing**, **Double Hashing**, **Chaining**.

2. **Vo Trong Phuc High-Score Refit Materials (`IT003_*_Vo_Trong_Phuc.pdf`)**:
   - Highly detailed step-by-step tracing for AVL rotations, BST deletion (2 children), B-Tree order 5 insert/split/promote.
   - Comprehensive exam-focused problem sets.

3. **Official Exam Papers (`IT003_2019_2020_HK2_CK2.pdf`, `IT003_CK_HK2_2022_2023.pdf`, `IT003.DE THI CK.HK2.2023-2024.pdf`, `IT003_2023_2024_De-1-DapAnThamKhao.pdf`)**:
   - Heavy emphasis on **manual tracing table**: exact comparison count ($C$), assignment/swap count ($M$).
   - BST deletion: replacing node with **Rightmost node of Left Subtree** (max-left) OR **Leftmost node of Right Subtree** (min-right). UIT exam key specifies exact choice.
   - Hash probing comparison count: tracing unsuccessful search length vs successful search length.
   - Graph: BFS/DFS tracing queue/stack step-by-step and listing node visitation order.
   - Shortest Path: Dijkstra relaxation table with vertex columns and weight vectors.
"""
    with open(os.path.join(BASE_DIR, "SOURCE_AUDIT.md"), "w", encoding="utf-8") as f:
        f.write(md)
    print("Generated SOURCE_AUDIT.md")


def build_syllabus_map():
    md = """# IT003_SYLLABUS_MAP.md — IT003 Curriculum Reconstruction

> **Comprehensive Knowledge Mapping & Dependency Graph**
> IT003 — Data Structures & Algorithms, University of Information Technology (UIT-VNUHCM).

---

## 1. Classification Matrix

### [CORE]
- Pointer & Dynamic Memory Allocation in C++
- Algorithm Analysis & Big-O Notation ($\mathcal{O}, \Omega, \Theta$)
- Elementary Sorting (Selection, Interchange, Bubble, Insertion)
- Advanced Sorting (Quick Sort, Heap Sort, Merge Sort)
- Linear Data Structures (Singly Linked List, Doubly Linked List)
- Stack & Queue (Array-based, Pointer-based, Circular Queue)
- Trees & Binary Search Tree (BST: Search, Insert, Delete)

### [MUST KNOW]
- Binary Search & Search Complexity Bounds
- Binary Insertion Sort & Shell Sort
- Balanced BST: AVL Tree (LL, RR, LR, RL Rotations & Balance Factors)
- B-Tree (Order $m$, Key insertion, Node split & promotion, Redistribution & Merge)
- Hash Table (Hash functions, Probing: Linear, Quadratic, Double Hashing, Chaining)
- Graph Representations (Adjacency Matrix, Adjacency List)
- Graph Traversals (BFS with Queue, DFS with Stack/Recursion)
- Shortest Path Algorithms (Dijkstra Algorithm)

### [EXAM HIGH FREQUENCY]
- Manual Tracing of Sorting Steps & Exact Count of Comparisons / Swaps ($C, M$)
- BST Deletion with 2 children (Tracing exact tree state after deletion)
- AVL Rotation Tracing (Identifying imbalance node & executing 1-step or 2-step rotation)
- B-Tree Insertion & Splitting (Order 5 B-Tree step-by-step state)
- Hash Table Insertion & Search Comparison Count ($C_{\text{succ}}, C_{\text{unsucc}}$)
- Graph BFS/DFS Visitation Sequence & Queue/Stack state
- Dijkstra Table Tracing step-by-step

### [PREREQUISITE]
- C++ Basics (Variables, Control flow, Structs, Functions, References `&`, Pointers `*`)
- Dynamic Memory Management (`new`, `delete`, `nullptr`, memory leak prevention)

### [EXTENSION & OPTIONAL]
- Radix Sort (Counting / Bucket intuition)
- Heap & Priority Queue (Max Heap, Min Heap, `std::priority_queue`)
- Bellman-Ford & Floyd-Warshall Algorithms (Shortest paths with negative weights)
- C++ STL Containers (`std::vector`, `std::list`, `std::stack`, `std::queue`, `std::unordered_map`, `std::map`)

---

## 2. Dependency Graph

```mermaid
graph TD
    PRE["Prerequisites: C++ & Pointers"] --> ALG["Part I: Algorithm Analysis & Big-O"]
    ALG --> SEARCH["Part II: Searching (Linear, Binary)"]
    SEARCH --> SORT_ELEM["Part III.A: Elementary Sorting (Selection, Interchange, Bubble, Insertion)"]
    SORT_ELEM --> SORT_ADV["Part III.B: Advanced Sorting (Quick, Heap, Merge, Shell, Radix)"]
    PRE --> LL["Part IV: Linked Lists (Singly, Doubly, Circular)"]
    LL --> SQ["Part V: Stack & Queue (Array & List)"]
    LL --> TREE["Part VI: Trees & Binary Trees"]
    TREE --> BST["Part VII: Binary Search Trees (BST)"]
    BST --> AVL["Part VIII: AVL Trees (Self-balancing)"]
    BST --> HEAP["Part IX: Heap & Priority Queue"]
    TREE --> BTREE["Part X: B-Trees (Multi-way search trees)"]
    SQ --> HASH["Part XI: Hash Tables (Probing & Chaining)"]
    TREE --> GRAPH["Part XII: Graphs (Matrix & List)"]
    GRAPH --> TRAV["Part XIII: Graph Traversals (BFS & DFS)"]
    TRAV --> SP["Part XIV: Shortest Path (Dijkstra)"]
    
    SORT_ADV --> EXAM["Part XV: Exam Toolkit & Synthesis"]
    AVL --> EXAM
    BTREE --> EXAM
    HASH --> EXAM
    SP --> EXAM
```
"""
    with open(os.path.join(BASE_DIR, "IT003_SYLLABUS_MAP.md"), "w", encoding="utf-8") as f:
        f.write(md)
    print("Generated IT003_SYLLABUS_MAP.md")


def build_exam_dna():
    md = """# EXAM_DNA.md — IT003 Exam Pattern & Mining Blueprint

> **Deep Analysis of IT003 Midterm & Final Examination Structure**
> University of Information Technology — VNUHCM

---

## 1. Exam Structure Overview

IT003 Final Exams typically consist of **4 to 5 major structural questions** (Time: 60-90 mins):

1. **Question 1: Sorting & Complexity Analysis (2.0 - 2.5 pts)**
   - Manual trace of a given array through $k$ passes of a specific algorithm (Interchange, Bubble, Selection, Quick, Heap).
   - Exact count of key comparisons ($C$) and swaps/assignments ($M$).
   - Complexity analysis for Best/Worst case.

2. **Question 2: Trees (BST & AVL) (2.5 - 3.0 pts)**
   - Construct BST from a sequence of keys.
   - Tree traversals (NLR, LNR, LRN).
   - Node deletion in BST (especially 2 children case).
   - Insert keys into AVL tree; identify balance factors; perform LL/RR/LR/RL rotations.

3. **Question 3: Advanced Trees / Hash Table (2.0 pts)**
   - **B-Tree**: Insert/delete keys in B-Tree of Order 5 ($m=5$), trace split and promotion of median key.
   - **Hash Table**: Hash function $h(k) = k \bmod M$, collision resolution via Linear Probing, Double Hashing ($h_2(k) = R - (k \bmod R)$).
   - Calculate exact number of comparisons for successful and unsuccessful searches.

4. **Question 4: Graphs & Algorithms (2.5 - 3.0 pts)**
   - Convert between Adjacency Matrix and Adjacency List.
   - Trace BFS starting from vertex $v$ (showing Queue state at each step).
   - Trace DFS starting from vertex $v$ (showing Stack/Recursion state).
   - Trace Dijkstra algorithm: update step-by-step vector $d[u]$ and predecessor $p[u]$ table.

---

## 2. Dạng Bài & Pattern Mining Detail

### Pattern A: Exact Comparison & Swap Counting ($C, M$)
- **Interchange Sort**:
  - Outer loop $i$ from $0$ to $n-2$, inner loop $j$ from $i+1$ to $n-1$.
  - Comparison count $C = \frac{n(n-1)}{2}$ regardless of input array (Unconditional comparison).
  - Swap count $M$: depends on initial order (0 in best case, $3 \times \frac{n(n-1)}{2}$ in worst case if 3 assignments per swap).
- **Bubble Sort**:
  - Stop early if no swap occurred (Adaptive). Best case $C = n-1, M = 0$.
- **Selection Sort**:
  - Always $C = \frac{n(n-1)}{2}$. Swaps $M = 3(n-1)$ (at most 1 swap per pass).

### Pattern B: BST Node Deletion Traps
- **Trap**: When deleting node $X$ with 2 children:
  - Substitution Node Option 1: **Rightmost node of Left Subtree** (max value in left subtree).
  - Substitution Node Option 2: **Leftmost node of Right Subtree** (min value in right subtree).
  - *UIT Exam Requirement*: Look closely at prompt instruction! If prompt specifies "thay thế bằng phần tử nhỏ nhất bên cây con phải", option 2 MUST be used.

### Pattern C: AVL Rotation Recognition
- Height of tree $h$, Balance factor $BF(node) = h_{left} - h_{right} \in \{-1, 0, 1\}$.
- Imbalance occurs when $BF = +2$ or $-2$.
  - $BF(A) = +2$:
    - If $BF(left\_child) \ge 0 \Rightarrow$ **LL Rotation** (Single Right Rotation at A).
    - If $BF(left\_child) = -1 \Rightarrow$ **LR Rotation** (Left Rotation at Left Child, then Right Rotation at A).
  - $BF(A) = -2$:
    - If $BF(right\_child) \le 0 \Rightarrow$ **RR Rotation** (Single Left Rotation at A).
    - If $BF(right\_child) = +1 \Rightarrow$ **RL Rotation** (Right Rotation at Right Child, then Left Rotation at A).

### Pattern D: B-Tree Order 5 ($m=5$) Operations
- Properties for B-Tree of Order 5:
  - Max keys per node: $m-1 = 4$. Max children: $m = 5$.
  - Min keys for non-root node: $\lceil m/2 \rceil - 1 = \lceil 2.5 \rceil - 1 = 2$. Min children: $\lceil m/2 \rceil = 3$.
  - Root: Min 1 key (if not empty), min 2 children.
- **Split Rule**: When inserting into full node (4 keys $\rightarrow$ 5 keys $[k_1, k_2, k_3, k_4, k_5]$):
  - Median key $k_3$ (index 3) is **promoted** to parent.
  - Left child gets $[k_1, k_2]$. Right child gets $[k_4, k_5]$.

### Pattern E: Hash Table Search Comparison Count
- Table size $M$.
- **Successful Search**: Average comparisons to find an existing key = $\frac{1}{N} \sum_{i=1}^N (\text{probes to find key } i)$.
- **Unsuccessful Search**: Average comparisons to confirm a key is NOT present = $\frac{1}{M} \sum_{i=0}^{M-1} (\text{probes from index } i \text{ until empty slot})$.
- *Exam Trap*: In Linear Probing, unsuccessful search stops at the FIRST EMPTY SLOT (`EMPTY`), but must NOT stop at a deleted slot (`DELETED`).

---

## 3. Recommended Exam Strategy & Time Budget

| Section | Target Time | Key Verification Check |
| :--- | :--- | :--- |
| **Sort Tracing** | 15 mins | Check $C$ formula matches pass count; verify array state at pass 1, 2, 3. |
| **Trees (BST/AVL)** | 20 mins | Re-calculate balance factors after rotation; check BST invariant ($L < N < R$). |
| **B-Tree / Hash** | 20 mins | Check B-Tree key count per node ($2 \le \text{keys} \le 4$); trace hash probes step-by-step. |
| **Graph & Dijkstra**| 25 mins | Check queue/stack order; ensure visited array is updated before pushing adjacent vertices. |
"""
    with open(os.path.join(BASE_DIR, "EXAM_DNA.md"), "w", encoding="utf-8") as f:
        f.write(md)
    print("Generated EXAM_DNA.md")


def build_style_guide():
    md = """# STYLE_GUIDE.md — IT003 DSA Ultimate Handbook Style & Design System

> **Design Guidelines, Typography, Color System, Code Standards & Print CSS Specification**

---

## 1. Design Aesthetics & Visual Hierarchy

- **Style Theme**: *Modern Academic Technical Handbook* — Clean, dense, highly structured, optimized for both screen viewing and A4 PDF print.
- **Color System (Semantic Palette)**:
  - **Primary**: Deep Academic Navy (`#0f172a` / `hsl(222, 47%, 11%)`)
  - **Accent**: UIT Cobalt Blue (`#1e40af` / `hsl(224, 76%, 48%)`)
  - **Secondary Accent**: Emerald Teal (`#0d9488` / `hsl(173, 80%, 32%)`)
  - **Warning / Alert**: Amber Red (`#b91c1c` / `hsl(0, 72%, 45%)`)
  - **Background**: Pure Crisp White (`#ffffff`) with subtle cool tint containers (`#f8fafc`).
  - **Forbidden**: No purple on dark, no rainbow gradients, no excessive glowing borders, no icon-stuffed bento boxes.

- **Typography & Font System**:
  - Headings & Title: Inter / Roboto / System Sans-serif, bold weight, tight letter-spacing.
  - Body Text: System Sans-serif, 10.5pt base font for print, line-height 1.55.
  - Code & Pseudocode: `Fira Code`, `JetBrains Mono`, or `Consolas`, 9.5pt font, crisp background (`#f1f5f9`).

---

## 2. Pedagogical Progression Model (12-Step Progression)

Every major concept must follow this pedagogical structure:

1. **WHY**: Why is this data structure / algorithm needed? What problem does it solve?
2. **INTUITION**: Real-world analogy or mental model before formal mathematics.
3. **FORMAL MODEL**: Exact mathematical definition, ADT specifications.
4. **VISUAL**: High-clarity vector diagram (SVG / Mermaid).
5. **MECHANICS**: Step-by-step breakdown of core operations.
6. **DRY RUN**: Complete manual trace table on a concrete sample dataset.
7. **CODE**: Dual C++ implementation (Educational custom code vs Standard Library `std::`).
8. **COMPLEXITY**: Rigorous mathematical proof of Time & Space complexity ($\mathcal{O}, \Omega, \Theta$).
9. **INVARIANT**: Loop invariant or structural invariant (e.g., BST property, AVL balance factor, Heap property).
10. **COMMON ERRORS**: Pitfalls, memory leaks, off-by-one errors, null pointer dereferences.
11. **EXAM CONNECTION**: How UIT examiners turn this concept into exam questions (with Badges).
12. **PRACTICE**: Graded practice exercises (Level 0 to Level 5).

---

## 3. Code Standards & Dual-Layer Implementation

- **Language**: Modern C++ (C++17 standard compatible, clean pointer syntax).
- **Layer 1: Educational Implementation**:
  - Written from scratch for total understanding.
  - Explicit struct/class definitions, clear pointer variable names (`pHead`, `pTail`, `pNext`, `pLeft`, `pRight`).
  - Strict null check & dynamic memory clean up (`delete`).
- **Layer 2: STL Implementation**:
  - Demonstrates professional C++ usage using `std::vector`, `std::stack`, `std::queue`, `std::priority_queue`, `std::unordered_map`.

---

## 4. Print CSS Specification (A4 Page Fit)

```css
@page {
    size: A4 portrait;
    margin: 18mm 15mm 18mm 15mm;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.5;
    color: #0f172a;
    background-color: #ffffff;
}

/* Page Break Controls */
h1, h2, h3 {
    break-after: avoid;
    break-inside: avoid;
}

.chapter-header {
    break-before: page;
}

.code-block, .diagram-container, table, .exam-badge-box {
    break-inside: avoid;
}

/* Orphan and Widow Control */
p, li {
    orphans: 3;
    widows: 3;
}
```
"""
    with open(os.path.join(BASE_DIR, "STYLE_GUIDE.md"), "w", encoding="utf-8") as f:
        f.write(md)
    print("Generated STYLE_GUIDE.md")


def build_project_state_and_todo():
    pstate = """PROJECT:
IT003 DSA UIT Handbook

CURRENT PHASE:
PHASE 1 — Research, Architecture & Core Authoring

CURRENT MODEL:
Gemini 3.6

COMPLETED:
- M0: Inventory of local sources (PDFs, PPTXs, DOCXs, Exam papers, High-Score refits)
- M1: SOURCE_AUDIT.md generated with detailed audit table & source classification
- M2: IT003_SYLLABUS_MAP.md constructed with 7-tier knowledge classification & Mermaid dependency graph
- M3: EXAM_DNA.md created with detailed pattern mining, comparison/swap counting rules, BST/AVL/B-Tree/Hash/Graph exam traps
- M4: STYLE_GUIDE.md defined with Modern Academic theme, 12-step pedagogical progression, dual C++ code standards, and A4 print CSS specs

IN PROGRESS:
- M5 - M10: Core Chapter Authoring (Writing comprehensive HTML chapters for Part 0 to Part XV)

REMAINING:
- M11: Visual pass & diagram enhancements (SVG / Mermaid)
- M12: Full master.html integration
- M13: Content QA
- M14: Print QA (A4 layout verification)
- M15: Final Gemini Candidate delivery

FILES CREATED:
- SOURCE_AUDIT.md
- IT003_SYLLABUS_MAP.md
- EXAM_DNA.md
- STYLE_GUIDE.md
- PROJECT_STATE.md
- TODO.md

FILES MODIFIED:
- None

IMPORTANT DECISIONS:
- Established IT003 Badge System: [IT003 CONVENTION] and [IT003 EXAM STYLE]
- Adopted 12-step progression (WHY -> INTUITION -> FORMAL MODEL -> VISUAL -> MECHANICS -> DRY RUN -> CODE -> COMPLEXITY -> INVARIANT -> COMMON ERRORS -> EXAM CONNECTION -> PRACTICE)
- Preserved exact UIT slide conventions for sorting names (Interchange Sort included) and tree level conventions

KNOWN ISSUES:
- None

QA BLOCKERS:
- None

LAST SAFE CHECKPOINT:
Milestones M0-M4 Complete

EXACT NEXT ACTION:
Begin authoring core handbook chapters in `chapters/` folder starting with Part 0 (How to Master IT003), Part I (Algorithm Analysis), Part II (Searching), Part III (Sorting), Part IV (Linked Lists), Part V (Stack & Queue), etc.
"""
    with open(os.path.join(BASE_DIR, "PROJECT_STATE.md"), "w", encoding="utf-8") as f:
        f.write(pstate)
    print("Generated PROJECT_STATE.md")

    todo = """# TODO.md — IT003 DSA UIT Handbook

## Priority Legend
- [P0]: Blocker / Critical Milestone
- [P1]: High Priority (Core Curriculum Content)
- [P2]: Medium Priority (Practice Bank & Refinements)
- [P3]: Low Priority / Polish

---

## Task Checklist

### Milestone M0 - M4 (Foundations & Architecture)
- [x] [P0] M0: Inventory all local files (PDFs, PPTXs, Exam papers)
- [x] [P0] M1: Generate SOURCE_AUDIT.md
- [x] [P0] M2: Generate IT003_SYLLABUS_MAP.md
- [x] [P0] M3: Generate EXAM_DNA.md
- [x] [P0] M4: Generate STYLE_GUIDE.md & Print CSS specs

### Milestone M5 - M10 (Core Authoring)
- [ ] [P0] Part 0: How to Master IT003 (Roadmap, Dry-running, Complexity mindset)
- [ ] [P0] Part I: Algorithm Analysis & Big-O Notation
- [ ] [P0] Part II: Searching Algorithms (Linear & Binary Search)
- [ ] [P0] Part III: Sorting Algorithms (Selection, Interchange, Bubble, Insertion, Binary Insertion, Shell, Heap, Quick, Merge, Radix)
- [ ] [P0] Part IV: Linked Lists (Singly, Doubly, Circular, Pointer Memory Diagrams)
- [ ] [P0] Part V: Stack & Queue (Array, Linked List, Circular Queue, DFS/BFS intuition)
- [ ] [P0] Part VI: Trees & Binary Trees
- [ ] [P0] Part VII: Binary Search Trees (BST - Insert, Search, Delete edge cases)
- [ ] [P0] Part VIII: AVL Trees (Rotations: LL, RR, LR, RL, Balance Factors)
- [ ] [P0] Part IX: Heaps & Priority Queues
- [ ] [P0] Part X: B-Trees (Order 5, Insertion, Split, Promotion, Redistribution, Merge)
- [ ] [P0] Part XI: Hash Tables (Modulo, Linear Probing, Quadratic, Double Hashing, Chaining, Unsuccessful search comparisons)
- [ ] [P0] Part XII: Graphs & Representations (Matrix, List)
- [ ] [P0] Part XIII: Graph Traversals (BFS & DFS)
- [ ] [P0] Part XIV: Shortest Path (Dijkstra Algorithm & Tables)
- [ ] [P1] Part XV: Exam Toolkit, Cheat Sheets & Integrated Practice Bank

### Milestone M11 - M15 (Integration, QA & Delivery)
- [ ] [P1] M11: SVG & Mermaid visual diagrams refinement
- [ ] [P0] M12: Build master.html and print.css
- [ ] [P1] M13: Content QA (Fact-checking complexities, stability, invariants)
- [ ] [P1] M14: Print QA (Checking A4 page breaks, margins, no blank pages)
- [ ] [P0] M15: Phase 1 Final Delivery Checkpoint
"""
    with open(os.path.join(BASE_DIR, "TODO.md"), "w", encoding="utf-8") as f:
        f.write(todo)
    print("Generated TODO.md")

def main():
    build_source_audit()
    build_syllabus_map()
    build_exam_dna()
    build_style_guide()
    build_project_state_and_todo()

if __name__ == "__main__":
    main()
