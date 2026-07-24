from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
BASE_IMAGE = ROOT / "i" / "cranbourne.png"
OUTPUT_IMAGE = ROOT / "i" / "bayswater.png"

NAVY = (9, 21, 49)
BLUE = (0, 91, 226)
GREY = (109, 123, 150)
PANEL_TOP = (252, 254, 255)
PANEL_BOTTOM = (247, 250, 255)
LINE = (213, 222, 235)


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(f"C:/Windows/Fonts/{name}", size)


def cover_gradient(image: Image.Image, box: tuple[int, int, int, int]) -> None:
    draw = ImageDraw.Draw(image)
    left, top, right, bottom = box
    height = max(1, bottom - top)
    for y in range(top, bottom):
        ratio = (y - top) / height
        color = tuple(
            round(PANEL_TOP[channel] * (1 - ratio) + PANEL_BOTTOM[channel] * ratio)
            for channel in range(3)
        )
        draw.line((left, y, right, y), fill=color)


def draw_text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, font_name: str, size: int, fill: tuple[int, int, int]) -> None:
    draw.text(xy, text, font=font(font_name, size), fill=fill)


image = Image.open(BASE_IMAGE).convert("RGB")
draw = ImageDraw.Draw(image)

# Clear and redraw only the text areas so the original icons, button, and hero image stay consistent.
cover_gradient(image, (292, 662, 1030, 824))
cover_gradient(image, (292, 856, 1030, 963))
cover_gradient(image, (292, 996, 1030, 1108))

draw.line((142, 828, 988, 828), fill=LINE, width=2)
draw.line((198, 976, 988, 976), fill=LINE, width=2)

draw_text(draw, (304, 678), "BYD Bayswater Service", "arialbd.ttf", 58, NAVY)
draw_text(draw, (306, 748), "BYD Service (Panel and Parts)", "arial.ttf", 38, GREY)
draw_text(draw, (306, 792), "service.bayswater@gloryevgroup-byd.com.au", "arial.ttf", 25, GREY)

draw_text(draw, (306, 871), "ADDRESS", "arialbd.ttf", 27, BLUE)
draw_text(draw, (306, 914), "904 Mountain Hwy, Bayswater VIC 3153", "arial.ttf", 32, NAVY)

draw_text(draw, (306, 1012), "PHONE", "arialbd.ttf", 27, BLUE)
draw_text(draw, (306, 1052), "(03) 8808 1617 / (03) 8808 1618", "arial.ttf", 32, NAVY)

image.save(OUTPUT_IMAGE, "PNG")
print(OUTPUT_IMAGE)
