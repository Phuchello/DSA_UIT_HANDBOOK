# ðŸ¤ HÆ°á»›ng Dáº«n ÄÃ³ng GÃ³p (Contributing Guidelines)

Cáº£m Æ¡n báº¡n Ä‘Ã£ quan tÃ¢m Ä‘áº¿n dá»± Ã¡n **IT003 â€” Cáº¥u trÃºc Dá»¯ liá»‡u vÃ  Giáº£i thuáº­t (UIT DSA Handbook)**! ChÃºng tÃ´i ráº¥t hoan nghÃªnh má»i Ä‘Ã³ng gÃ³p tá»« cá»™ng Ä‘á»“ng sinh viÃªn vÃ  giáº£ng viÃªn Ä‘á»ƒ cáº©m nang ngÃ y cÃ ng chÃ­nh xÃ¡c, hoÃ n thiá»‡n vÃ  há»¯u Ã­ch hÆ¡n.

---

## ðŸŽ¯ CÃ¡c hÃ¬nh thá»©c Ä‘Ã³ng gÃ³p Ä‘Æ°á»£c Æ°u tiÃªn

1. **BÃ¡o lá»—i há»c thuáº­t (Academic / Factual Corrections):**
   - Sai lá»‡ch cÃ´ng thá»©c toÃ¡n, Ä‘á»‹nh lÃ½ hoáº·c Ä‘á»™ phá»©c táº¡p thuáº­t toÃ¡n.
   - Nháº§m láº«n vá» tÃ­nh cháº¥t thuáº­t toÃ¡n (vÃ­ dá»¥: tÃ­nh á»•n Ä‘á»‹nh Stable / Unstable, in-place).
   - Lá»—i logic trong báº£ng cháº¡y tay (dry-run trace) hoáº·c lá»i giáº£i bÃ i táº­p.
2. **Cáº£i tiáº¿n mÃ£ nguá»“n & vÃ­ dá»¥ (Code & Examples):**
   - PhÃ¡t hiá»‡n lá»—i tiá»m áº©n trong code C++ (null pointer, trÃ n sá»‘, rÃ² rá»‰ bá»™ nhá»›).
   - Bá»• sung giáº£i thÃ­ch trá»±c quan ngáº¯n gá»n cho cÃ¡c Ä‘oáº¡n mÃ£ phá»©c táº¡p.
3. **Sá»­a lá»—i chÃ­nh táº£ & Ä‘á»‹nh dáº¡ng (Formatting & Typos):**
   - Lá»—i gÃµ tiáº¿ng Viá»‡t, lá»—i ngáº¯t dÃ²ng hoáº·c hiá»ƒn thá»‹ KaTeX / SVG.
   - Cáº£i thiá»‡n tÃ­nh tiáº¿p cáº­n (accessibility) trÃªn cÃ¡c thiáº¿t bá»‹ di Ä‘á»™ng.

---

## ðŸ“ Quy trÃ¬nh gá»­i Ä‘Ã³ng gÃ³p

### BÃ¡o lá»—i qua Issue
- Sá»­ dá»¥ng cÃ¡c máº«u cÃ³ sáºµn trong má»¥c **Issues**:
  - **[BÃ¡o lá»—i ná»™i dung há»c thuáº­t]** náº¿u phÃ¡t hiá»‡n sai sÃ³t kiáº¿n thá»©c/thuáº­t toÃ¡n.
  - **[BÃ¡o lá»—i hiá»ƒn thá»‹ / ká»¹ thuáº­t]** náº¿u gáº·p sá»± cá»‘ giao diá»‡n hoáº·c render trang.
- Vui lÃ²ng trÃ­ch dáº«n rÃµ vá»‹ trÃ­ (TÃªn chÆ°Æ¡ng, má»¥c sá»‘ máº¥y) vÃ  cung cáº¥p tÃ i liá»‡u/nguá»“n tham chiáº¿u Ä‘á»‘i chiáº¿u náº¿u cÃ³.

### Gá»­i Pull Request (PR)
1. Fork repository vá» tÃ i khoáº£n GitHub cÃ¡ nhÃ¢n cá»§a báº¡n.
2. Táº¡o branch má»›i vá»›i tÃªn gá»£i má»Ÿ: `fix/ch08-avl-rotation-note` hoáº·c `typo/ch03-sorting-table`.
3. Chá»‰ chá»‰nh sá»­a cÃ¡c file mÃ£ nguá»“n liÃªn quan trong thÆ° má»¥c `chapters/` hoáº·c tÃ i liá»‡u Markdown.
4. Cháº¡y script `build.ps1` Ä‘á»ƒ kiá»ƒm tra báº£n xuáº¥t báº£n `master.html` váº«n biÃªn dá»‹ch bÃ¬nh thÆ°á»ng.
5. Táº¡o Pull Request mÃ´ táº£ rÃµ nguyÃªn nhÃ¢n vÃ  ná»™i dung thay Ä‘á»•i.

---

## âš–ï¸ Quy chuáº©n ná»™i dung

- **TÃ´n trá»ng tÃ i liá»‡u gá»‘c:** Æ¯u tiÃªn bÃ¡m sÃ¡t chÆ°Æ¡ng trÃ¬nh giáº£ng dáº¡y vÃ  chuáº©n thi cá»§a TrÆ°á»ng ÄH CÃ´ng nghá»‡ ThÃ´ng tin (ÄHQG-HCM).
- **Giá»¯ phong cÃ¡ch sÆ° pháº¡m:** Ngáº¯n gá»n, trá»±c quan, giáº£i thÃ­ch rÃµ trá»±c giÃ¡c trÆ°á»›c khi Ä‘Æ°a ra mÃ£ nguá»“n.
- **KhÃ´ng thay Ä‘á»•i pháº¡m vi lá»›n vÃ´ cÄƒn cá»©:** TrÃ¡nh viáº¿t láº¡i toÃ n bá»™ má»™t chÆ°Æ¡ng náº¿u khÃ´ng cÃ³ lá»—i há»c thuáº­t nghiÃªm trá»ng Ä‘Ã£ Ä‘Æ°á»£c tháº£o luáº­n tá»« trÆ°á»›c.