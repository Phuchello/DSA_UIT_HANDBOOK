# STYLE_GUIDE.md — IT003 DSA Ultimate Handbook Style & Design System

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
