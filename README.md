# ðŸ“˜ IT003 â€” Cáº¥u trÃºc Dá»¯ liá»‡u vÃ  Giáº£i thuáº­t
### UIT DSA Handbook

> Cáº©m nang há»c táº­p, tra cá»©u vÃ  Ã´n thi mÃ´n **Cáº¥u trÃºc Dá»¯ liá»‡u vÃ  Giáº£i thuáº­t (IT003)** táº¡i **TrÆ°á»ng Äáº¡i há»c CÃ´ng nghá»‡ ThÃ´ng tin (ÄHQG-HCM)**. TÃ i liá»‡u Ä‘Æ°á»£c thiáº¿t káº¿ theo tiáº¿n trÃ¬nh sÆ° pháº¡m: tá»« trá»±c giÃ¡c thá»±c táº¿, phÃ¢n tÃ­ch Ä‘á»™ phá»©c táº¡p, mÃ£ nguá»“n C++, báº£ng cháº¡y tay tá»«ng bÆ°á»›c (dry-run) Ä‘áº¿n ngÃ¢n hÃ ng bÃ i táº­p vÃ  Ä‘á» thi máº«u.

**BiÃªn soáº¡n:** [VÃµ Trá»ng PhÃºc](https://github.com/Phuchello)

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Book-blue?style=flat&logo=github)](https://phuchello.github.io/DSA_UIT_HANDBOOK/)
[![PDF](https://img.shields.io/badge/PDF-Download%20(1.4MB)-red?style=flat&logo=adobe-acrobat-reader)](IT003_DSA_UIT_CamNang_FINAL.pdf)
[![Course](https://img.shields.io/badge/Course-IT003%20UIT-1e40af?style=flat)](https://www.uit.edu.vn)
[![Code](https://img.shields.io/badge/Code-C%2B%2B17-00599C?style=flat&logo=c%2B%2B)](chapters/)

---

## ðŸš€ Truy cáº­p & Táº£i vá» nhanh

| PhiÃªn báº£n | Äá»‹nh dáº¡ng | MÃ´ táº£ |
| :--- | :--- | :--- |
| ðŸŒ **[Äá»c trá»±c tuyáº¿n trÃªn Web](https://phuchello.github.io/DSA_UIT_HANDBOOK/)** | Web View (Pages) | Giao diá»‡n tá»‘i Æ°u Ä‘á»c trÃªn mÃ¡y tÃ­nh, tablet vÃ  Ä‘iá»‡n thoáº¡i |
| ðŸ“„ **[Táº£i báº£n PDF hoÃ n chá»‰nh (1.4 MB)](IT003_DSA_UIT_CamNang_FINAL.pdf)** | PDF A4 | SÃ¡ch in chuáº©n A4, KaTeX vector sáº¯c nÃ©t, layout hoÃ n thiá»‡n |
| ðŸ’» **[File HTML Ä‘á»™c láº­p (Offline)](IT003_DSA_UIT_CamNang_FINAL.html)** | Standalone HTML | TÃ­ch há»£p sáºµn KaTeX & CSS offline, má»Ÿ khÃ´ng cáº§n Internet |
| ðŸ“Š **[Ma tráº­n Äá» thi & Báº«y thÆ°á»ng gáº·p](EXAM_DNA.md)** | Markdown | PhÃ¢n tÃ­ch cáº¥u trÃºc Ä‘á» thi IT003, cÃ¡ch cháº¥m Ä‘iá»ƒm vÃ  cÃ¡c báº«y kinh Ä‘iá»ƒn |
| ðŸ—ºï¸ **[Báº£n Ä‘á»“ Kiáº¿n thá»©c & CÃ¢y phá»¥ thuá»™c](IT003_SYLLABUS_MAP.md)** | Markdown | Lá»™ trÃ¬nh 7 táº§ng kiáº¿n thá»©c vÃ  biá»ƒu Ä‘á»“ Mermaid quan há»‡ chá»§ Ä‘á» |
| ðŸ” **[BÃ¡o cÃ¡o Tháº©m Ä‘á»‹nh Há»c thuáº­t (QA)](QA_REPORT_FINAL.md)** | Markdown | Nháº­t kÃ½ kiá»ƒm thá»­ thuáº­t toÃ¡n, fact-check vÃ  thang Ä‘iá»ƒm cháº¥t lÆ°á»£ng |

---

## ðŸ’¡ Äiá»ƒm ná»•i báº­t cá»§a Handbook

* **Trá»±c giÃ¡c trÆ°á»›c cÃ i Ä‘áº·t (Intuition-First):** Má»i cáº¥u trÃºc dá»¯ liá»‡u vÃ  giáº£i thuáº­t Ä‘á»u báº¯t Ä‘áº§u báº±ng cÃ¢u há»i trá»±c quan *"VÃ¬ sao cáº§n cáº¥u trÃºc nÃ y?"* vÃ  sÆ¡ Ä‘á»“ minh há»a trÆ°á»›c khi Ä‘i vÃ o mÃ£ nguá»“n.
* **Báº£ng cháº¡y tay tá»«ng bÆ°á»›c (Dry-run Tables):** HÆ°á»›ng dáº«n chi tiáº¿t cÃ¡ch láº­p báº£ng theo dÃµi tráº¡ng thÃ¡i biáº¿n, con trá» vÃ  máº£ng qua tá»«ng vÃ²ng láº·p â€” ká»¹ nÄƒng trá»ng tÃ¢m cá»§a cÃ¡c cÃ¢u há»i tá»± luáº­n trong Ä‘á» thi IT003.
* **Chuáº©n C++ giÃ¡o khoa & STL song hÃ nh:** TrÃ¬nh bÃ y song song mÃ£ nguá»“n C++ thuáº§n con trá» (phá»¥c vá»¥ thi cá»­, hiá»ƒu sÃ¢u báº£n cháº¥t cáº¥p phÃ¡t Ä‘á»™ng) vÃ  thÆ° viá»‡n chuáº©n `std::` (phá»¥c vá»¥ á»©ng dá»¥ng thá»±c táº¿).
* **Cáº£nh bÃ¡o báº«y há»c thuáº­t (Pitfalls & Traps):** LÃ m rÃµ cÃ¡c lá»—i dá»… máº¥t Ä‘iá»ƒm nhÆ° tÃ­nh cháº¥t *Not Stable* cá»§a Interchange Sort, Ä‘iá»u kiá»‡n dá»«ng cá»§a tÃ¬m kiáº¿m tháº¥t báº¡i trÃªn Báº£ng bÄƒm, vÃ  quy táº¯c tÃ¡ch/gá»™p nÃºt B-Tree báº­c 5.

---

## ðŸ“š Pháº¡m vi ná»™i dung (Course Coverage)

Handbook bao quÃ¡t toÃ n diá»‡n chÆ°Æ¡ng trÃ¬nh mÃ´n há»c IT003 táº¡i UIT, Ä‘Æ°á»£c chia thÃ nh 5 nhÃ³m kiáº¿n thá»©c trá»ng tÃ¢m:

### 1. Ná»n táº£ng & TÃ¬m kiáº¿m (Foundations & Searching)
* **PhÃ¢n tÃ­ch thuáº­t toÃ¡n:** KÃ½ phÃ¡p tiá»‡m cáº­n Big-O, Big-Omega, Big-Theta, quy táº¯c cá»™ng/nhÃ¢n, Ä‘áº¿m sá»‘ phÃ©p toÃ¡n vÃ²ng láº·p, phÃ¢n tÃ­ch Ä‘á»™ sÃ¢u cÃ¢y Ä‘á»‡ quy vÃ  bá»™ nhá»› Call Stack.
* **Thuáº­t toÃ¡n tÃ¬m kiáº¿m:** Linear Search (TÃ¬m kiáº¿m tuyáº¿n tÃ­nh) vÃ  Binary Search (TÃ¬m kiáº¿m nhá»‹ phÃ¢n, Ä‘iá»u kiá»‡n máº£ng cÃ³ thá»© tá»±, phÃ²ng trÃ¡nh trÃ n sá»‘ khi tÃ­nh `mid`).

### 2. 10 Thuáº­t toÃ¡n Sáº¯p xáº¿p (Sorting Algorithms)
* **NhÃ³m cÆ¡ báº£n O(nÂ²):** Selection Sort, Interchange Sort (Ä‘áº·c thÃ¹ UIT, *Not Stable*), Bubble Sort (báº£n thÆ°á»ng vs báº£n tá»‘i Æ°u cá» hiá»‡u), Insertion Sort, Binary Insertion Sort (giáº£m phÃ©p so sÃ¡nh nhÆ°ng tá»•ng thá»i gian váº«n O(nÂ²)).
* **NhÃ³m nÃ¢ng cao O(n log n):** Shell Sort (phá»¥ thuá»™c Gap sequence), Heap Sort (vá»›i `buildHeap` cháº¡y trong Theta(n)), Quick Sort (phÃ¢n hoáº¡ch Lomuto chuáº©n), Merge Sort (chia Ä‘á»ƒ trá»‹, bá»™ nhá»› phá»¥ O(n)).
* **NhÃ³m phi so sÃ¡nh:** Radix Sort (sáº¯p xáº¿p theo tá»«ng chá»¯ sá»‘ vá»›i cÆ¡ sá»‘ k).

### 3. Cáº¥u trÃºc Tuyáº¿n tÃ­nh (Linear Data Structures)
* **Danh sÃ¡ch liÃªn káº¿t (Linked List):** DSLK Ä‘Æ¡n (Singly Linked List) vÃ  DSLK Ä‘Ã´i (Doubly Linked List), ká»¹ thuáº­t quáº£n lÃ½ con trá» `pHead`, `pTail`, thao tÃ¡c thÃªm/xÃ³a Ä‘áº§u/cuá»‘i/giá»¯a vÃ  giáº£i phÃ³ng bá»™ nhá»› an toÃ n.
* **NgÄƒn xáº¿p & HÃ ng Ä‘á»£i (Stack & Queue):** CÆ¡ cháº¿ LIFO/FIFO, cÃ i Ä‘áº·t báº±ng máº£ng vÃ  danh sÃ¡ch liÃªn káº¿t, HÃ ng Ä‘á»£i vÃ²ng (Circular Queue vá»›i phÃ©p toÃ¡n Modulo giáº£i quyáº¿t trÃ n giáº£), á»©ng dá»¥ng kiá»ƒm tra ngoáº·c há»£p lá»‡ vÃ  chuyá»ƒn Ä‘á»•i biá»ƒu thá»©c Infix sang Postfix.

### 4. Cáº¥u trÃºc CÃ¢y (Tree Structures)
* **CÃ¢y nhá»‹ phÃ¢n (Binary Trees):** Äá»‹nh nghÄ©a nÃºt gá»‘c, nÃºt lÃ¡, chiá»u cao, má»©c (Level 0), cÃ¡c thá»© tá»± duyá»‡t Pre-order (NLR), In-order (LNR), Post-order (LRN).
* **CÃ¢y nhá»‹ phÃ¢n tÃ¬m kiáº¿m (BST):** Báº¥t biáº¿n cÃ¢y tÃ¬m kiáº¿m, tÃ¬m kiáº¿m, chÃ¨n, thao tÃ¡c xÃ³a nÃºt 2 con dÃ¹ng pháº§n tá»­ tháº¿ máº¡ng cá»±c trÃ¡i cÃ¢y con pháº£i (Min-Right) hoáº·c cá»±c pháº£i cÃ¢y con trÃ¡i (Max-Left).
* **CÃ¢y cÃ¢n báº±ng AVL (AVL Trees):** Há»‡ sá»‘ cÃ¢n báº±ng `BF = h(left) - h(right)`, 4 phÃ©p xoay chuáº©n (Xoay Ä‘Æ¡n LL, RR vÃ  Xoay kÃ©p LR, RL) khÃ´i phá»¥c Ä‘á»™ phá»©c táº¡p O(log n).
* **Heap & HÃ ng Ä‘á»£i Æ°u tiÃªn (Priority Queue):** Cáº¥u trÃºc Max-Heap, cÃ´ng thá»©c Ã¡nh xáº¡ chá»‰ sá»‘ máº£ng 0-indexed (`2i+1`, `2i+2`, `floor((i-1)/2)`), thuáº­t toÃ¡n `buildHeap` Theta(n) vÃ  Heap Sort.
* **CÃ¢y B-Tree:** Cáº¥u trÃºc B-Tree báº­c 5 (m = 5, tá»‘i Ä‘a 4 khÃ³a, tá»‘i thiá»ƒu 2 khÃ³a), quy táº¯c trÃ n khÃ³a tÃ¡ch nÃºt Ä‘áº©y ná»•i trung vá»‹ thá»© 3, vÃ  quy táº¯c xÃ³a nÃºt (mÆ°á»£n anh em hoáº·c gá»™p nÃºt).

### 5. Báº£ng bÄƒm, Äá»“ thá»‹ & Luyá»‡n thi (Hashing, Graphs & Exam Prep)
* **Báº£ng bÄƒm (Hash Table):** HÃ m bÄƒm Modulo, cÃ¡c phÆ°Æ¡ng phÃ¡p giáº£i quyáº¿t Ä‘á»¥ng Ä‘á»™: Linear Probing, Quadratic Probing, Double Hashing (vá»›i hÃ m h2 do Ä‘á» bÃ i quy Ä‘á»‹nh), Separate Chaining; cÃ´ng thá»©c Ä‘áº¿m sá»‘ phÃ©p so sÃ¡nh trung bÃ¬nh tÃ¬m kiáº¿m thÃ nh cÃ´ng (C_succ) vÃ  tháº¥t báº¡i (C_unsucc).
* **Äá»“ thá»‹ (Graphs):** Biá»ƒu diá»…n báº±ng Ma tráº­n ká» vs Danh sÃ¡ch ká», duyá»‡t Ä‘á»“ thá»‹ theo chiá»u rá»™ng BFS (Queue) vÃ  chiá»u sÃ¢u DFS (Stack/Äá»‡ quy), xá»­ lÃ½ Ä‘á»“ thá»‹ khÃ´ng liÃªn thÃ´ng.
* **ÄÆ°á»ng Ä‘i ngáº¯n nháº¥t (Shortest Path):** Thuáº­t toÃ¡n Dijkstra (trá»ng sá»‘ khÃ´ng Ã¢m, nguyÃªn lÃ½ ná»›i cáº¡nh Relaxation), so sÃ¡nh vá»›i Bellman-Ford (há»— trá»£ cáº¡nh Ã¢m, phÃ¡t hiá»‡n chu trÃ¬nh Ã¢m) vÃ  Floyd-Warshall (má»i cáº·p Ä‘á»‰nh).
* **Exam Toolkit:** NgÃ¢n hÃ ng bÃ i táº­p 5 cáº¥p Ä‘á»™ (Level 0 Concept -> Level 5 Challenge) vÃ  bá»™ Ä‘á» thi thá»­ hoÃ n chá»‰nh kÃ¨m lá»i giáº£i chi tiáº¿t tá»«ng bÆ°á»›c.

---

## ðŸ“‘ Danh má»¥c 16 Pháº§n (Table of Contents)

| Pháº§n | TÃªn ChÆ°Æ¡ng | Ná»™i dung trá»ng tÃ¢m |
| :--- | :--- | :--- |
| **Part 0** | Roadmap & Progression | PhÆ°Æ¡ng phÃ¡p há»c táº­p, lá»™ trÃ¬nh 4 bÆ°á»›c vÃ  chiáº¿n lÆ°á»£c lÃ m bÃ i thi |
| **Part I** | PhÃ¢n tÃ­ch Thuáº­t toÃ¡n | Äá»‹nh nghÄ©a Big-O, Omega, Theta, quy táº¯c cá»™ng/nhÃ¢n, phÃ¢n tÃ­ch Ä‘á»‡ quy |
| **Part II** | Thuáº­t toÃ¡n TÃ¬m kiáº¿m | Linear Search, Binary Search, invariants vÃ  ká»¹ thuáº­t trÃ¡nh trÃ n sá»‘ |
| **Part III** | 10 Thuáº­t toÃ¡n Sáº¯p xáº¿p | Ma tráº­n so sÃ¡nh 10 thuáº­t toÃ¡n, Ä‘á»™ phá»©c táº¡p, tÃ­nh á»•n Ä‘á»‹nh (Stable) vÃ  in-place |
| **Part IV** | Danh sÃ¡ch LiÃªn káº¿t | Singly/Doubly Linked List, thao tÃ¡c con trá» vÃ  trÃ¡nh rÃ² rá»‰ bá»™ nhá»› |
| **Part V** | NgÄƒn xáº¿p & HÃ ng Ä‘á»£i | Stack, Queue, Circular Queue (Modulo), chuyá»ƒn Ä‘á»•i Infix sang Postfix |
| **Part VI** | CÃ¢y & CÃ¢y Nhá»‹ phÃ¢n | KhÃ¡i niá»‡m cÃ¢y, quy Æ°á»›c má»©c/chiá»u cao, 3 thá»© tá»± duyá»‡t NLR, LNR, LRN |
| **Part VII** | CÃ¢y BST | CÃ¢y nhá»‹ phÃ¢n tÃ¬m kiáº¿m, tÃ¬m kiáº¿m, chÃ¨n, xÃ³a nÃºt 2 con (Min-Right / Max-Left) |
| **Part VIII** | CÃ¢y CÃ¢n báº±ng AVL | Há»‡ sá»‘ BF, báº£ng tra 4 phÃ©p xoay LL, RR, LR, RL vÃ  mÃ£ nguá»“n C++ |
| **Part IX** | Heap & HÃ ng Ä‘á»£i Æ¯u tiÃªn | Max-Heap, cÃ´ng thá»©c chá»‰ sá»‘ máº£ng 0-indexed, BuildHeap Theta(n), HeapSort |
| **Part X** | CÃ¢y B-Tree | B-Tree báº­c 5 (m = 5), cÆ¡ cháº¿ trÃ n khÃ³a tÃ¡ch nÃºt vÃ  mÆ°á»£n/gá»™p khi xÃ³a |
| **Part XI** | Báº£ng BÄƒm (Hash Table) | Linear/Quadratic/Double Hashing, Ä‘áº¿m sá»‘ phÃ©p so sÃ¡nh C_succ vÃ  C_unsucc |
| **Part XII** | Biá»ƒu diá»…n Äá»“ thá»‹ | Ma tráº­n ká» vs Danh sÃ¡ch ká», so sÃ¡nh bá»™ nhá»› vÃ  thá»i gian truy xuáº¥t |
| **Part XIII** | Duyá»‡t Äá»“ thá»‹ | BFS (Queue, loang lá»›p), DFS (Stack/Äá»‡ quy, Ä‘i sÃ¢u), báº«y thá»© tá»± Ä‘á»‰nh ká» |
| **Part XIV** | ÄÆ°á»ng Ä‘i Ngáº¯n nháº¥t | Thuáº­t toÃ¡n Dijkstra, báº£ng trace ná»›i cáº¡nh, so sÃ¡nh Bellman-Ford & Floyd |
| **Part XV** | Exam Toolkit | NgÃ¢n hÃ ng bÃ i táº­p 5 cáº¥p Ä‘á»™ + Äá» thi máº«u cuá»‘i ká»³ kÃ¨m Ä‘Ã¡p Ã¡n chi tiáº¿t |

---

## ðŸ“‚ Cáº¥u trÃºc Repository

```text
DSA_UIT_HANDBOOK/
â”œâ”€â”€ index.html                           # File phá»¥c vá»¥ GitHub Pages (báº£n xuáº¥t báº£n chÃ­nh thá»©c)
â”œâ”€â”€ IT003_DSA_UIT_CamNang_FINAL.html      # Báº£n HTML Ä‘á»™c láº­p (Offline Standalone)
â”œâ”€â”€ IT003_DSA_UIT_CamNang_FINAL.pdf       # Báº£n PDF hoÃ n chá»‰nh chuáº©n in áº¥n A4 (~1.4 MB)
â”œâ”€â”€ print.css                            # CSS Ä‘á»‹nh kiá»ƒu giao diá»‡n web & tá»‘i Æ°u in áº¥n PDF
â”œâ”€â”€ build.ps1                            # Script PowerShell tá»± Ä‘á»™ng biÃªn dá»‹ch cÃ¡c chapter
â”œâ”€â”€ chapters/                            # ThÆ° má»¥c chá»©a 16 file nguá»“n HTML tá»«ng chÆ°Æ¡ng
â”‚   â”œâ”€â”€ 00_HOW_TO_MASTER_IT003.html
â”‚   â”œâ”€â”€ 01_ALGORITHM_ANALYSIS.html
â”‚   â”œâ”€â”€ ...
â”‚   â””â”€â”€ 15_EXAM_TOOLKIT.html
â”œâ”€â”€ assets/                              # TÃ i nguyÃªn phá»¥ trá»£ (font KaTeX offline, icons)
â”œâ”€â”€ EXAM_DNA.md                          # PhÃ¢n tÃ­ch cáº¥u trÃºc Ä‘á» thi IT003 & báº«y kinh Ä‘iá»ƒn
â”œâ”€â”€ IT003_SYLLABUS_MAP.md                # Báº£n Ä‘á»“ phÃ¢n táº§ng 7 cáº¥p Ä‘á»™ kiáº¿n thá»©c & sÆ¡ Ä‘á»“ quan há»‡
â”œâ”€â”€ SOURCE_AUDIT.md                      # Báº£ng Ä‘á»‘i chiáº¿u nguá»“n tÆ° liá»‡u & tÃ i liá»‡u tham kháº£o
â”œâ”€â”€ QA_REPORT_FINAL.md                   # BÃ¡o cÃ¡o tháº©m Ä‘á»‹nh há»c thuáº­t vÃ  kiá»ƒm thá»­ giáº£i thuáº­t
â””â”€â”€ CONTRIBUTING.md                      # HÆ°á»›ng dáº«n Ä‘Ã³ng gÃ³p & bÃ¡o lá»—i há»c thuáº­t
```

---

## ðŸ› ï¸ HÆ°á»›ng dáº«n biÃªn dá»‹ch táº¡i mÃ¡y cá»¥c bá»™ (Build Locally)

Náº¿u báº¡n muá»‘n chá»‰nh sá»­a cÃ¡c chÆ°Æ¡ng riÃªng láº» trong thÆ° má»¥c `chapters/` vÃ  biÃªn dá»‹ch láº¡i thÃ nh file HTML tá»•ng há»£p:

1. **YÃªu cáº§u mÃ´i trÆ°á»ng:** Windows PowerShell 5.1 hoáº·c PowerShell Core 7+.
2. **Cháº¡y lá»‡nh biÃªn dá»‹ch:**
   ```powershell
   powershell -ExecutionPolicy Bypass -File .\build.ps1
   ```
3. Script sáº½ Ä‘á»c tuáº§n tá»± 16 chÆ°Æ¡ng nguá»“n vÃ  táº¡o ra file `master.html` hoÃ n chá»‰nh vá»›i Ä‘áº§y Ä‘á»§ má»¥c lá»¥c, trang bÃ¬a vÃ  cáº¥u hÃ¬nh KaTeX.

---

## ðŸ”Ž Nguá»“n tÆ° liá»‡u & Quy trÃ¬nh Kiá»ƒm Ä‘á»‹nh (QA)

* **Nguá»“n tham chiáº¿u trá»ng tÃ¢m:** BÃ i giáº£ng chÃ­nh thá»©c, tÃ i liá»‡u thá»±c hÃ nh vÃ  cÃ¡c bá»™ Ä‘á» thi mÃ´n IT003 táº¡i TrÆ°á»ng Äáº¡i há»c CÃ´ng nghá»‡ ThÃ´ng tin (ÄHQG-HCM).
* **Kiá»ƒm chá»©ng há»c thuáº­t:** Äá»‘i chiáº¿u cÃ¡c Ä‘á»‹nh lÃ½, cÃ´ng thá»©c tÃ­nh toÃ¡n vÃ  tÃ­nh cháº¥t thuáº­t toÃ¡n vá»›i giÃ¡o trÃ¬nh chuáº©n quá»‘c táº¿ (*Introduction to Algorithms - CLRS*).
* **Quy trÃ¬nh QA:** ToÃ n bá»™ cÃ´ng thá»©c toÃ¡n LaTeX, mÃ£ nguá»“n C++, báº£ng cháº¡y tay vÃ  tÃ­nh cháº¥t thuáº­t toÃ¡n (tÃ­nh á»•n Ä‘á»‹nh, Ä‘á»™ phá»©c táº¡p) Ä‘Ã£ vÆ°á»£t qua quy trÃ¬nh kiá»ƒm thá»­ tá»± Ä‘á»™ng vÃ  tháº©m Ä‘á»‹nh há»c thuáº­t nghiÃªm ngáº·t (Ä‘áº¡t Ä‘iá»ƒm Ä‘Ã¡nh giÃ¡ **100/100** trong [QA_REPORT_FINAL.md](QA_REPORT_FINAL.md)).

---

## ðŸ‘¤ NgÆ°á»i biÃªn soáº¡n

**VÃµ Trá»ng PhÃºc**  
* GitHub: [@Phuchello](https://github.com/Phuchello)  
* Dá»± Ã¡n: [DSA_UIT_HANDBOOK](https://github.com/Phuchello/DSA_UIT_HANDBOOK)

---

## âš ï¸ LÆ°u Ã½ & Miá»…n trá»« trÃ¡ch nhiá»‡m (Disclaimer)

> ÄÃ¢y lÃ  tÃ i liá»‡u há»c táº­p Ä‘á»™c láº­p do cÃ¡ nhÃ¢n biÃªn soáº¡n nháº±m má»¥c Ä‘Ã­ch há»— trá»£ sinh viÃªn há»c táº­p, tra cá»©u vÃ  Ã´n thi mÃ´n IT003 Cáº¥u trÃºc Dá»¯ liá»‡u vÃ  Giáº£i thuáº­t. TÃ i liá»‡u **khÃ´ng pháº£i áº¥n pháº©m chÃ­nh thá»©c** cá»§a TrÆ°á»ng Äáº¡i há»c CÃ´ng nghá»‡ ThÃ´ng tin (ÄHQG-HCM) vÃ  khÃ´ng thay tháº¿ cho slide bÃ i giáº£ng, giÃ¡o trÃ¬nh chÃ­nh khÃ³a hay cÃ¡c hÆ°á»›ng dáº«n trá»±c tiáº¿p tá»« giáº£ng viÃªn bá»™ mÃ´n.

---

## ðŸ¤ ÄÃ³ng gÃ³p (Contributing)

Má»i Ã½ kiáº¿n Ä‘Ã³ng gÃ³p, phÃ¡t hiá»‡n lá»—i sai há»c thuáº­t hoáº·c Ä‘á» xuáº¥t cáº£i tiáº¿n ná»™i dung Ä‘á»u Ä‘Æ°á»£c hoan nghÃªnh. Vui lÃ²ng Ä‘á»c ká»¹ [CONTRIBUTING.md](CONTRIBUTING.md) trÆ°á»›c khi táº¡o Issue hoáº·c gá»­i Pull Request.