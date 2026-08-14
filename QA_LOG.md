# QA_LOG.md — IT003 Precision Fix Log

> **Systematic Record of Precision Fixes & Verification**

---

## Precision Audit Resolution Table

| ID | Status | Files Changed | Verification Details | Result |
| :--- | :---: | :--- | :--- | :--- |
| **PREC-001** | **RESOLVED** | `chapters/15_EXAM_TOOLKIT.html`, `master.html` | Replaced invalid AVL sequence `18, 10, 25, 6, 14` with `30, 20, 40, 10, 5`. Recalculated balance factors ($BF(20)=+2, BF(10)=+1 \Rightarrow$ LL rotation at 20). | **PASS** |
| **PREC-002** | **RESOLVED** | `chapters/01_ALGORITHM_ANALYSIS.html`, `master.html` | Rewrote Big-O, Big-Omega, Big-Theta definitions as mathematical asymptotic function bounds. Added IT003 Precision Note distinguishing bounds from input cases. | **PASS** |
| **PREC-003** | **RESOLVED** | `chapters/03_SORTING.html`, `master.html` | Added footnote explaining Binary Insertion Sort comparisons ($\Theta(n \log n)$) vs data movements ($0$) in Best Case. | **PASS** |
| **PREC-004** | **RESOLVED** | `chapters/03_SORTING.html`, `master.html` | Added footnote specifying Shell Sort complexity dependence on gap sequence (Shell original $\Theta(n^2)$ vs Sedgewick $\mathcal{O}(n^{4/3})$). | **PASS** |
| **PREC-005** | **RESOLVED** | `chapters/03_SORTING.html`, `master.html` | Updated Interchange Sort stability to "Yes" under strict `a[i] > a[j]` condition. | **PASS** |
| **PREC-006** | **RESOLVED** | `chapters/09_HEAP_PRIORITY_QUEUE.html`, `master.html` | Fixed KaTeX floor syntax `\lfloor (i-1)/2 \rfloor` across heap formulas and exercise hints. | **PASS** |
| **PREC-007** | **RESOLVED** | `chapters/03_SORTING.html`, `master.html` | Defined $k$ in Radix Sort space complexity $\Theta(n + k)$ as number system radix/base. | **PASS** |
| **SVG-001** | **RESOLVED** | `chapters/04_LINKED_LIST.html`, `07_BST.html`, `08_AVL.html`, `10_BTREE.html`, `14_SHORTEST_PATH.html`, `master.html` | Replaced duplicate `<marker id="arrow">` tags with unique IDs (`arrow-ll`, `arrow-bst`, `arrow-avl`, `arrow-btree`, `arrow-dijkstra`). | **PASS** |
| **KATEX-001** | **RESOLVED** | `build.ps1`, `master.html` | Removed malformed CSS `<script>` tag and unified KaTeX auto-render configuration with `throwOnError: false`. | **PASS** |

---

## Checkpoint Status Criteria

- **Encoding Corruption**: 0
- **Broken Math Expressions**: 0
- **Unresolved CRITICAL Issues**: 0
- **Unresolved MAJOR Issues**: 0
- **Answer-key Correctness Checked**: YES

**CURRENT PHASE**: `CONTENT_LOCKED_READY_FOR_CODEX`
