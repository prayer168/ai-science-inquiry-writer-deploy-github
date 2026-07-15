#!/usr/bin/env python3
"""Validate paired plain-text and standalone HTML article outputs."""

from __future__ import annotations

import argparse
import html
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
URL_RE = re.compile(r"https?://\S+")


class ArticleHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.attrs: list[tuple[str, dict[str, str]]] = []
        self.text_parts: list[str] = []
        self.in_style = False
        self.in_script = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        self.attrs.append((tag.lower(), values))
        if tag.lower() == "style":
            self.in_style = True
        if tag.lower() == "script":
            self.in_script = True

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "style":
            self.in_style = False
        if tag.lower() == "script":
            self.in_script = False

    def handle_data(self, data: str) -> None:
        if not self.in_style and not self.in_script:
            self.text_parts.append(data)


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--txt", required=True, type=Path)
    parser.add_argument("--html", required=True, type=Path)
    parser.add_argument("--min-body-chars", type=int, default=2000)
    parser.add_argument("--max-body-chars", type=int, default=3000)
    args = parser.parse_args()

    errors: list[str] = []
    if not args.txt.is_file():
        fail(errors, f"TXT not found: {args.txt}")
    if not args.html.is_file():
        fail(errors, f"HTML not found: {args.html}")
    if errors:
        return report(errors)

    if args.txt.stem != args.html.stem:
        fail(errors, "TXT and HTML must share the same basename")
    if not SLUG_RE.fullmatch(args.txt.stem):
        fail(errors, "Basename must be lowercase ASCII kebab-case")

    try:
        txt = args.txt.read_text(encoding="utf-8")
        html_text = args.html.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(errors, f"UTF-8 decode failed: {exc}")
        return report(errors)

    title = next((line.strip() for line in txt.splitlines() if line.strip()), "")
    if not title:
        fail(errors, "TXT title is missing")

    body = txt.split("資料來源", 1)[0]
    body_chars = len(re.sub(r"\s+", "", body))
    if not args.min_body_chars <= body_chars <= args.max_body_chars:
        fail(errors, f"Body length {body_chars} is outside {args.min_body_chars}-{args.max_body_chars}")

    urls = URL_RE.findall(txt)
    if not 5 <= len(urls) <= 10:
        fail(errors, f"Expected 5-10 source URLs, found {len(urls)}")
    if "查閱日期" not in txt:
        fail(errors, "TXT must include a source access date")
    if re.search(r"^#{1,6}\s", txt, re.MULTILINE) or re.search(r"<[^>]+>", txt):
        fail(errors, "TXT must not contain Markdown headings or HTML tags")

    parsed = ArticleHTMLParser()
    parsed.feed(html_text)
    attrs = parsed.attrs
    html_tags = [values for tag, values in attrs if tag == "html"]
    if not html_tags or html_tags[0].get("lang", "").lower() != "zh-hant":
        fail(errors, 'HTML must use lang="zh-Hant"')
    if not re.search(r'<meta\s+charset=["\']utf-8["\']', html_text, re.IGNORECASE):
        fail(errors, "HTML must declare UTF-8 charset")
    if not re.search(r'<meta\s+name=["\']viewport["\']', html_text, re.IGNORECASE):
        fail(errors, "HTML must include a viewport meta tag")
    if "<style" not in html_text.lower():
        fail(errors, "HTML must include inline CSS")
    if any(tag in {"button", "input"} for tag, _ in attrs):
        fail(errors, "HTML must not contain buttons or inputs")
    for tag, values in attrs:
        if tag == "link" and values.get("href"):
            fail(errors, "HTML must not depend on external link assets")
        if tag == "script" and values.get("src"):
            fail(errors, "HTML must not depend on external scripts")
        if tag == "a" and values.get("href", "").startswith(("http://", "https://")):
            rel_tokens = set(values.get("rel", "").split())
            if values.get("target") != "_blank" or not {"noopener", "noreferrer"}.issubset(rel_tokens):
                fail(errors, f"Unsafe external link attributes: {values.get('href')}")

    if title and f"<title>{title}</title>" not in html_text:
        fail(errors, "HTML <title> must match the TXT title")
    visible = normalize(" ".join(parsed.text_parts))
    body_norm = normalize(body)
    if body_norm not in visible:
        fail(errors, "Visible HTML article body does not match the TXT body")
    if not re.search(r"@media\s*\([^)]*max-width", html_text, re.IGNORECASE):
        fail(errors, "HTML must include a narrow-screen media query")
    if not re.search(r"@media\s+print", html_text, re.IGNORECASE):
        fail(errors, "HTML must include print styles")

    if errors:
        return report(errors)
    print(f"PASS: {args.txt.name} + {args.html.name}")
    print(f"Body characters: {body_chars}; source URLs: {len(urls)}")
    return 0


def report(errors: list[str]) -> int:
    for message in errors:
        print(f"ERROR: {message}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
