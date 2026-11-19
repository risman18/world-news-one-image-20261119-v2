#!/usr/bin/env python3
"""Build-time renderer for THE WORLD TODAY — Thu 19 Nov 2026 (v2).

Renders the broadsheet front page to entry.png (1024x1024, <=1 MiB).
Rendering happens HERE at build time; main.py in the repo is a stdlib-only
copier of the pre-rendered entry.png.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

W, H = 1024, 1024
CREAM = (247, 240, 220)
NAVY = (16, 41, 75)
NAVY_LT = (38, 68, 110)
GOLD = (176, 138, 60)
INK = (24, 24, 24)
RULE = (16, 41, 75)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, color=INK):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def fit_panel(path, tw, th):
    """Crop-to-fill an image into tw x th, with a navy border."""
    im = Image.open(path).convert("RGB")
    im = ImageOps.fit(im, (tw, th), Image.LANCZOS)
    return im


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    M = 30  # margin
    R = W - M  # right edge

    # ---- Masthead ----
    f_title = font(SERIF_B, 76)
    d.text((W // 2, 18), "THE WORLD TODAY", font=f_title, fill=NAVY, anchor="ma")
    d.line([(M, 112), (R, 112)], fill=RULE, width=3)
    d.line([(M, 118), (R, 118)], fill=RULE, width=1)
    f_date = font(SANS_B, 22)
    d.text((W // 2, 126), "THURSDAY, 19 NOVEMBER 2026", font=f_date, fill=NAVY, anchor="ma")
    f_tag = font(SANS, 16)
    d.text((W // 2, 154), "ONE IMAGE  ·  THE WHOLE DAY  ·  SHENZHEN — NEW YORK — LONDON",
           font=f_tag, fill=NAVY_LT, anchor="ma")

    # ---- Lead story ----
    y = 186
    f_kick = font(SANS_B, 19)
    d.text((M, y), "THE LEAD  —  SHENZHEN, CHINA", font=f_kick, fill=GOLD)
    y += 26
    f_head = font(SERIF_B, 52)
    d.text((M, y), "THREE AT ONE TABLE", font=f_head, fill=NAVY)
    y += 64
    f_sub = font(SERIF, 24)
    y = para(d, M, y, "Trump, Xi and Putin meet for the first time —",
             f_sub, R - M, 28, color=NAVY_LT)
    y = para(d, M, y, "nuclear arms, Ukraine and Iran on the table.",
             f_sub, R - M, 28, color=NAVY_LT)
    y += 6
    # Lead body: left text column, right summit panel
    body_top = y
    col_w = 430
    f_body = font(SERIF, 20)
    yy = para(d, M, body_top,
              "Xi Jinping hosts Donald Trump and Vladimir Putin at APEC in Shenzhen — the first trilateral meeting of the three leaders.",
              f_body, col_w, 25)
    yy += 6
    yy = para(d, M, yy,
              "Nuclear arms top the agenda: New START, the last US–Russia treaty, lapsed in February. No deal is expected.",
              f_body, col_w, 25)
    # Summit panel, right of body
    px, py = M + col_w + 24, body_top
    pw, ph = R - px, 200
    panel = fit_panel(os.path.join(ASSETS, "media-generation-panel-summit-0-3ddf47c3-9a32-4a4a-9269-56e2c9cd7d10.webp"), pw, ph)
    img.paste(panel, (px, py))
    d.rectangle([px, py, px + pw - 1, py + ph - 1], outline=NAVY, width=3)
    f_cap = font(SANS, 15)
    d.text((px, py + ph + 6), "The three leaders meet on the sidelines of APEC.",
           font=f_cap, fill=NAVY_LT)
    lead_bottom = max(yy, py + ph + 24)

    # ---- Divider ----
    d.line([(M, lead_bottom + 6), (R, lead_bottom + 6)], fill=RULE, width=2)

    # ---- Three supporting stories ----
    top = lead_bottom + 20
    col_w3 = 304
    gap = 16
    stories = [
        ("media-generation-panel-bridge-0-eabb95d7-9b65-4a95-aa77-ad4845584f6b.webp",
         "THE BRIDGE HIT AGAIN",
         "Third strike this week: the rail span is hit overnight; traffic halts."),
        ("media-generation-panel-vicecity-0-1e5097c2-3c01-4e9a-8196-56f9d845b4a8.webp",
         "VICE CITY OPENS",
         "GTA VI launches worldwide after 13 years. 99 on Metacritic; 17.1m copies pre-sold."),
        ("media-generation-panel-vangogh-0-0ba16488-0bf4-4dc2-8b23-d05a471b2ced.webp",
         "A RECORD $190.4M",
         "Van Gogh's Blossoming Chestnut Trees sets an artist record at Sotheby's."),
    ]
    f_h3 = font(SERIF_B, 24)
    f_s3 = font(SERIF, 17)
    mid_bottom = top
    for i, (fname, head, body) in enumerate(stories):
        x = M + i * (col_w3 + gap)
        im3 = fit_panel(os.path.join(ASSETS, fname), col_w3, 110)
        img.paste(im3, (x, top))
        d.rectangle([x, top, x + col_w3 - 1, top + 109], outline=NAVY, width=2)
        hy = top + 120
        for line in wrap(d, head, f_h3, col_w3):
            d.text((x, hy), line, font=f_h3, fill=NAVY)
            hy += 28
        hy = para(d, x, hy + 2, body, f_s3, col_w3, 21)
        mid_bottom = max(mid_bottom, hy)

    # ---- Also today strip ----
    d.line([(M, mid_bottom + 4), (R, mid_bottom + 4)], fill=RULE, width=2)
    ay = mid_bottom + 16
    f_also = font(SANS_B, 20)
    d.text((M, ay), "ALSO TODAY", font=f_also, fill=GOLD)
    ay += 30
    items = [
        ("NVIDIA", "Record $115.8bn revenue; shares fall 2.9% to $150.96."),
        ("VOYAGER 1", "One light-day from Earth — 25.9bn km, a first."),
        ("CYCLONE AKVAN", "Odisha evacuates 46,701; landfall due Friday."),
        ("UKRAINE AID", "EU proposes a €45bn loan for Kyiv."),
        ("THE GULF", "Iran hits US bases in Kuwait and Bahrain."),
        ("WASHINGTON", "Jeffries chosen as Speaker nominee."),
    ]
    f_lab = font(SANS_B, 17)
    f_it = font(SERIF, 17)
    col2_w = (R - M - gap) // 2
    row_h = 46
    for i, (lab, txt) in enumerate(items):
        x = M + (i % 2) * (col2_w + gap)
        yy = ay + (i // 2) * row_h
        d.text((x, yy), lab + "  —  ", font=f_lab, fill=NAVY)
        lw = d.textlength(lab + "  —  ", font=f_lab)
        para(d, x + lw, yy + 1, txt, f_it, col2_w - lw, 21)
    foot_y = ay + 3 * row_h + 2
    d.line([(M, foot_y), (R, foot_y)], fill=RULE, width=1)
    f_foot = font(SANS, 14)
    d.text((W // 2, foot_y + 8), "THE WORLD TODAY  ·  THURSDAY, 19 NOVEMBER 2026  ·  ALL STORIES REPORTED TODAY",
           font=f_foot, fill=NAVY_LT, anchor="ma")

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print("saved", out, img.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
