import json
import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "조항데이터.json"


def main():
    if len(sys.argv) < 2:
        print("사용법: python solution.py <키워드>")
        sys.exit(1)
    keyword = sys.argv[1]

    articles = json.loads(DATA.read_text(encoding="utf-8"))

    filtered = [a for a in articles if keyword in a["본문"]]

    out = HERE / f"결과_{keyword}.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["조", "제목", "본문"])
        for a in filtered:
            w.writerow([a["조"], a["제목"], a["본문"]])
    print(f"[OK] {len(filtered)}건 저장 → {out.name}")


if __name__ == "__main__":
    main()