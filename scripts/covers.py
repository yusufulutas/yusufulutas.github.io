"""Resize cover images to 920px wide WebP into assets/img/games.

    pip install pillow
    python scripts/covers.py ~/Downloads/grounded.jpg ~/Downloads/v-rising.png
"""

import sys
from pathlib import Path

from PIL import Image

WIDTH = 920
OUT = Path(__file__).resolve().parent.parent / "assets" / "img" / "games"


def convert(src):
    src = Path(src)
    dst = OUT / (src.stem.lower().replace(" ", "-") + ".webp")
    with Image.open(src) as im:
        im = im.convert("RGB")
        if im.width > WIDTH:
            im = im.resize((WIDTH, round(im.height * WIDTH / im.width)), Image.LANCZOS)
        im.save(dst, "WEBP", quality=80, method=6)
    print(f"{dst.name}  {dst.stat().st_size // 1024} KB")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    OUT.mkdir(parents=True, exist_ok=True)
    for path in sys.argv[1:]:
        convert(path)
