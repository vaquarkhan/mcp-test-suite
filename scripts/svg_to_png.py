"""Render docs/images/*.svg to PNG via Chromium (Playwright)."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
IMGS = ROOT / "docs" / "images"
HTML_IMGS = ROOT / "html" / "assets" / "images"
TMP = ROOT / "_svg_render"

SVGS = [
    "hero-banner-suite.svg",
    "architecture-suite.svg",
    "multi-language-suite.svg",
    "features-any-language.svg",
    "feature-overview-suite.svg",
    "dogfood-e2e.svg",
]


def viewbox(text: str) -> tuple[int, int]:
    m = re.search(r'viewBox="([^"]+)"', text)
    if not m:
        m = re.search(r"viewBox='([^']+)'", text)
    if m:
        parts = m.group(1).split()
        return int(float(parts[2])), int(float(parts[3]))
    return 1400, 600


def main() -> None:
    TMP.mkdir(exist_ok=True)
    HTML_IMGS.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=2)
        for name in SVGS:
            svg_path = IMGS / name
            raw = svg_path.read_bytes().decode("utf-8", errors="replace")
            w, h = viewbox(raw)
            if re.search(r"<svg[^>]*\swidth=", raw) is None:
                raw = raw.replace("<svg ", f'<svg width="{w}" height="{h}" ', 1)
            doc = (
                "<!DOCTYPE html><html><head><meta charset='utf-8'>"
                "<style>html,body{margin:0;padding:0;background:#0b1220;}svg{display:block;}</style>"
                f"</head><body>{raw}</body></html>"
            )
            html_path = TMP / f"{name}.html"
            html_path.write_text(doc, encoding="utf-8")
            page.set_viewport_size({"width": w, "height": h})
            page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
            page.wait_for_timeout(500)
            png_name = name.replace(".svg", ".png")
            dest = IMGS / png_name
            page.screenshot(path=str(dest), type="png", full_page=True)
            shutil.copyfile(dest, HTML_IMGS / png_name)
            print(f"{png_name}: {dest.stat().st_size} bytes ({w}x{h})")
        browser.close()

    shutil.rmtree(TMP, ignore_errors=True)
    print("done")


if __name__ == "__main__":
    main()
