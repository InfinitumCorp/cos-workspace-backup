#!/usr/bin/env python3
"""Personal press profile images — B&W portrait + black panel.
No logo watermark, no phone. Poppins. Overwrites:
  press-william-turner-1200x675.jpg
  press-william-turner-1080x1080.jpg
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "william-turner-photo-2026-11.jpg"
FONT_DIR = Path("/usr/share/fonts/truetype/sand-box/google/Poppins")
HAIR_Y_FRAC = 58 / 896  # measured on source


def F(weight: int, size: int) -> ImageFont.FreeTypeFont:
    names = {
        400: "Poppins-Regular.ttf",
        500: "Poppins-Medium.ttf",
        600: "Poppins-SemiBold.ttf",
        700: "Poppins-Bold.ttf",
    }
    return ImageFont.truetype(str(FONT_DIR / names[weight]), size)


def cover_crop(im: Image.Image, tw: int, th: int, focus_x: float, headroom_frac: float):
    sw, sh = im.size
    # Prefer a scale that still covers, but ease off slightly if needed so headroom is real.
    base = max(tw / sw, th / sh)
    sc = base
    for trial in (1.0, 0.98, 0.96, 0.94):
        sc = base * trial
        nw, nh = int(round(sw * sc)), int(round(sh * sc))
        if nw < tw or nh < th:
            continue
        y_hair = HAIR_Y_FRAC * nh
        y0 = int(round(y_hair - headroom_frac * th))
        if y0 >= 0 and y0 + th <= nh:
            break
    else:
        sc = base
        nw, nh = int(round(sw * sc)), int(round(sh * sc))
    r = im.resize((nw, nh), Image.Resampling.LANCZOS)
    x0 = int(round(focus_x * nw - tw / 2))
    x0 = max(0, min(nw - tw, x0))
    y0 = int(round(HAIR_Y_FRAC * nh - headroom_frac * th))
    y0 = max(0, min(nh - th, y0))
    # If still short on width/height after zoom-out, pad with source-edge bg
    crop = r.crop((x0, y0, min(x0 + tw, nw), min(y0 + th, nh)))
    if crop.size != (tw, th):
        canvas = Image.new("RGB", (tw, th), (230, 230, 230))
        canvas.paste(crop, (0, 0))
        return canvas
    return crop


def soft_shadow(h: int, width: int = 32) -> Image.Image:
    strip = Image.new("L", (width, h), 0)
    px = strip.load()
    for x in range(width):
        a = int(160 * (1 - x / (width - 1)) ** 1.7)
        for y in range(h):
            px[x, y] = a
    return strip


def make_landscape(src: Image.Image) -> Image.Image:
    W, H = 1200, 675
    panel_w = 500
    photo_w = W - panel_w
    photo = cover_crop(src, photo_w, H, focus_x=0.50, headroom_frac=0.085)
    im = Image.new("RGB", (W, H), (0, 0, 0))
    im.paste(photo, (0, 0))
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sh = soft_shadow(H, 32)
    band = Image.new("RGBA", (32, H), (0, 0, 0, 255))
    band.putalpha(sh)
    overlay.paste(band, (photo_w - 32, 0), band)
    im = Image.alpha_composite(im.convert("RGBA"), overlay).convert("RGB")
    d = ImageDraw.Draw(im)
    mx = 700 + 40
    brand = "INFINITUM CORPORATION®"
    f_brand = F(600, 17)
    brand_y = 228
    d.text((mx, brand_y), brand, font=f_brand, fill=(255, 255, 255), anchor="ls")
    bw = d.textlength(brand, font=f_brand)
    rule_y = brand_y + 14
    d.line([(mx, rule_y), (mx + bw, rule_y)], fill=(255, 255, 255), width=1)
    name = "William Aaron Turner"
    f_name = F(700, 38)
    while d.textlength(name, font=f_name) > 392 and f_name.size > 30:
        f_name = F(700, f_name.size - 1)
    name_y = 300
    d.text((mx, name_y), name, font=f_name, fill=(255, 255, 255), anchor="ls")
    bbox = d.textbbox((mx, name_y), name, font=f_name, anchor="ls")
    d.text((mx, bbox[3] + 28), "Founder & President", font=F(400, 18), fill=(165, 165, 165), anchor="ls")
    d.text((mx, 612), "PRESS PROFILE · NOVEMBER 2026", font=F(400, 12), fill=(110, 110, 110), anchor="ls")
    return im


def make_square(src: Image.Image) -> Image.Image:
    W = H = 1080
    photo = cover_crop(src, W, 760, focus_x=0.50, headroom_frac=0.075)
    im = Image.new("RGB", (W, H), (0, 0, 0))
    im.paste(photo, (0, 0))
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    grad_start, grad_h = 620, 140
    grad = Image.new("L", (W, grad_h), 0)
    gp = grad.load()
    for y in range(grad_h):
        a = int(255 * (y / (grad_h - 1)) ** 1.2)
        for x in range(W):
            gp[x, y] = a
    band = Image.new("RGBA", (W, grad_h), (0, 0, 0, 255))
    band.putalpha(grad)
    overlay.paste(band, (0, grad_start), band)
    ImageDraw.Draw(overlay).rectangle([0, grad_start + grad_h - 2, W, H], fill=(0, 0, 0, 255))
    im = Image.alpha_composite(im.convert("RGBA"), overlay).convert("RGB")
    d = ImageDraw.Draw(im)
    cx = W // 2
    brand = "INFINITUM CORPORATION®"
    f_brand = F(600, 18)
    brand_y = 790
    d.text((cx, brand_y), brand, font=f_brand, fill=(255, 255, 255), anchor="ms")
    bw = d.textlength(brand, font=f_brand)
    rule_y = brand_y + 14
    d.line([(cx - bw / 2, rule_y), (cx + bw / 2, rule_y)], fill=(255, 255, 255), width=1)
    name = "William Aaron Turner"
    f_name = F(700, 44)
    while d.textlength(name, font=f_name) > W - 160:
        f_name = F(700, f_name.size - 1)
    name_y = 925
    d.text((cx, name_y), name, font=f_name, fill=(255, 255, 255), anchor="ms")
    bbox = d.textbbox((cx, name_y), name, font=f_name, anchor="ms")
    d.text((cx, bbox[3] + 30), "Founder & President", font=F(400, 20), fill=(165, 165, 165), anchor="ms")
    d.text((cx, 1025), "PRESS PROFILE · NOVEMBER 2026", font=F(400, 13), fill=(110, 110, 110), anchor="ms")
    return im


def main():
    src = Image.open(SRC).convert("RGB")
    land = make_landscape(src)
    sq = make_square(src)
    land_path = ROOT / "press-william-turner-1200x675.jpg"
    sq_path = ROOT / "press-william-turner-1080x1080.jpg"
    land.save(land_path, quality=95, optimize=True, subsampling=0)
    sq.save(sq_path, quality=95, optimize=True, subsampling=0)
    print("wrote", land_path, land.size, land_path.stat().st_size)
    print("wrote", sq_path, sq.size, sq_path.stat().st_size)


if __name__ == "__main__":
    main()
