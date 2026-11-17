"""合併 _series.js ＋ u01.js…u12.js → ../content.js。
用法：python3 build.py"""
from pathlib import Path

here = Path(__file__).resolve().parent
parts = [(here / "_series.js").read_text(encoding="utf-8").rstrip(), "", "window.UNITS = ["]
units = sorted(here.glob("u[0-9][0-9].js"))
for i, f in enumerate(units):
    body = f.read_text(encoding="utf-8").strip().rstrip(";").rstrip(",")
    assert body.startswith("{") and body.endswith("}"), f"{f.name} 必須是單一物件字面值"
    parts.append(f"  // ---------------------------------------------------------- {f.stem.upper()}")
    parts.append(body + ("," if i < len(units) - 1 else ""))
parts.append("];")
(here.parent / "content.js").write_text("\n".join(parts) + "\n", encoding="utf-8")
print(f"content.js ← _series.js + {len(units)} 集：{', '.join(u.stem for u in units)}")
