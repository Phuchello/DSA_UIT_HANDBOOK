import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

BASE_DIR = r"C:\Users\lyle3\.gemini\antigravity\scratch\IT003_DSA_BOOK"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")

chapter_files = sorted(os.listdir(CHAPTERS_DIR))

print(f"Found {len(chapter_files)} chapter files in {CHAPTERS_DIR}:")

for fname in chapter_files:
    fpath = os.path.join(CHAPTERS_DIR, fname)
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read().lower()

    missing = []
    if "intuition" not in content and "trực giác" not in content:
        missing.append("Intuition")
    if "formal" not in content and "định nghĩa toán học" not in content and "formal model" not in content and "định nghĩa & thuật ngữ" not in content and "định nghĩa cấu trúc" not in content:
        missing.append("Formal Model")
    if "<svg" not in content and "diagram" not in content:
        missing.append("Visual Diagram (<svg>)")
    if "mechanics" not in content and "thuật toán" not in content and "algorithm" not in content:
        missing.append("Algorithm / Mechanics")
    if "<pre><code>" not in content:
        missing.append("C++ Code")
    if "complexity" not in content and "độ phức tạp" not in content:
        missing.append("Complexity")
    if "dry run" not in content and "chạy tay" not in content and "tracing" not in content:
        missing.append("Dry Run Table")
    if "common" not in content and "sai lầm" not in content and "error" not in content and "bẫy" not in content:
        missing.append("Common Errors")
    if "quick recall" not in content and "tóm tắt nhanh" not in content:
        missing.append("Quick Recall")
    if "exercise" not in content and "bài tập" not in content and "level 0" not in content:
        missing.append("Exercise Ladder")
    if "exam style" not in content and "badge-exam-style" not in content:
        missing.append("IT003 Exam Style")
    if "summary" not in content and "tổng kết" not in content and "lời kết" not in content and "tóm kết" not in content:
        missing.append("Summary")

    print(f"\n📄 {fname} (Length: {len(content)} chars)")
    if missing and fname != "15_EXAM_TOOLKIT.html": # 15 is exam toolkit synthesis
        print(f"   ⚠️ Missing components: {', '.join(missing)}")
    else:
        print("   ✅ All required components present!")
