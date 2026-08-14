# EXAM_DNA.md — IT003 Exam Pattern & Mining Blueprint

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
   - **Hash Table**: Hash function $h(k) = k mod M$, collision resolution via Linear Probing, Double Hashing ($h_2(k) = R - (k mod R)$).
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
  - Comparison count $C = rac{n(n-1)}{2}$ regardless of input array (Unconditional comparison).
  - Swap count $M$: depends on initial order (0 in best case, $3 	imes rac{n(n-1)}{2}$ in worst case if 3 assignments per swap).
- **Bubble Sort**:
  - Stop early if no swap occurred (Adaptive). Best case $C = n-1, M = 0$.
- **Selection Sort**:
  - Always $C = rac{n(n-1)}{2}$. Swaps $M = 3(n-1)$ (at most 1 swap per pass).

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
  - Min keys for non-root node: $\lceil m/2 ceil - 1 = \lceil 2.5 ceil - 1 = 2$. Min children: $\lceil m/2 ceil = 3$.
  - Root: Min 1 key (if not empty), min 2 children.
- **Split Rule**: When inserting into full node (4 keys $ightarrow$ 5 keys $[k_1, k_2, k_3, k_4, k_5]$):
  - Median key $k_3$ (index 3) is **promoted** to parent.
  - Left child gets $[k_1, k_2]$. Right child gets $[k_4, k_5]$.

### Pattern E: Hash Table Search Comparison Count
- Table size $M$.
- **Successful Search**: Average comparisons to find an existing key = $rac{1}{N} \sum_{i=1}^N (	ext{probes to find key } i)$.
- **Unsuccessful Search**: Average comparisons to confirm a key is NOT present = $rac{1}{M} \sum_{i=0}^{M-1} (	ext{probes from index } i 	ext{ until empty slot})$.
- *Exam Trap*: In Linear Probing, unsuccessful search stops at the FIRST EMPTY SLOT (`EMPTY`), but must NOT stop at a deleted slot (`DELETED`).

---

## 3. Recommended Exam Strategy & Time Budget

| Section | Target Time | Key Verification Check |
| :--- | :--- | :--- |
| **Sort Tracing** | 15 mins | Check $C$ formula matches pass count; verify array state at pass 1, 2, 3. |
| **Trees (BST/AVL)** | 20 mins | Re-calculate balance factors after rotation; check BST invariant ($L < N < R$). |
| **B-Tree / Hash** | 20 mins | Check B-Tree key count per node ($2 \le 	ext{keys} \le 4$); trace hash probes step-by-step. |
| **Graph & Dijkstra**| 25 mins | Check queue/stack order; ensure visited array is updated before pushing adjacent vertices. |
