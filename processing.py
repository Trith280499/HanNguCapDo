import os

import json
import jieba
from collections import Counter

# ===== LOAD FILE COMPLETE =====
# with open("complete.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "complete.json")

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# ===== BUILD DICTIONARY =====
HSK_DICT = {}

def map_level(level_list):
    if not level_list:
        return "NA"

    lvl = level_list[0]
    if lvl.startswith("new-"):
        num = lvl.replace("new-", "")
        if num.isdigit():
            return int(num)
        else:
            return "ADVANCED"
    return "NA"

for item in data:
    word = item.get("simplified")
    level = map_level(item.get("level", []))
    if word:
        HSK_DICT[word] = level

# ===== ANALYZE FUNCTION =====
def analyze(text: str):
    char_count = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')

    words = [w for w in jieba.lcut(text) if w.strip()]
    word_count = len(words)

    levels = [HSK_DICT.get(w, "NA") for w in words]
    stats = Counter(levels)

    basic_levels = [l for l in levels if isinstance(l, int)]
    advanced_count = levels.count("ADVANCED")

    estimated = "Unknown"

    if basic_levels:
        most_common_level, count = Counter(basic_levels).most_common(1)[0]
        ratio = count / len(words)
        estimated = f"HSK{most_common_level}"

        if most_common_level == 1 and word_count >= 4:
            estimated = "HSK2"

    warning = None
    if advanced_count > 0:
        warning = "Contains advanced words (HSK7+)"

    return {
        "characters": char_count,
        "words": word_count,
        "level_distribution": dict(stats),
        "estimated_level": estimated,
        "warning": warning
    }
