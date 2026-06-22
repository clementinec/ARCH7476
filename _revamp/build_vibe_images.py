from pathlib import Path

from PIL import Image, ImageFilter, ImageOps


OUT = Path("assets/generated/vibes-evidence")
SRC = OUT / "source"
SIZE = (1600, 900)

SOURCES = {
    "restaurant-vibe.png": {
        "source": "restaurant-source.jpg",
        "url": "https://platform.eater.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/25869763/BloomsHero1_121___Brett_Wood.jpg?crop=0%2C0%2C100%2C100&quality=90&strip=all&w=2400",
        "crop": (0, 95, 2400, 1445),
    },
    "phone-camera-vibe.png": {
        "source": "phone-camera-source.webp",
        "url": "https://assets.lls.fr/pages/55469386/mat1t8ouvtelephone-2-retoucheok.webp",
        "crop": (0, 500, 2649, 1990),
    },
    "calm-route-vibe.png": {
        "source": "calm-route-source.jpg",
        "url": "https://i0.wp.com/theroadsbeyond.com/wp-content/uploads/2023/03/Avenue-de-Champagne-in-Epernay.jpg?resize=750%2C437&ssl=1",
        "crop": (0, 8, 750, 430),
    },
    "green-facade-vibe.png": {
        "source": "green-facade-source.jpg",
        "url": "https://d36tnp772eyphs.cloudfront.net/blogs/1/2019/04/Giant-green-wall-in-Madrid.jpg",
        "crop": (550, 78, 1280, 489),
    },
}


def export(source, crop, target):
    img = Image.open(source)
    img = ImageOps.exif_transpose(img).convert("RGB")
    img = img.crop(crop)

    # Phone source is portrait; a faint blur layer helps the 16:9 crop feel intentional.
    if target.name == "phone-camera-vibe.png":
        bg = ImageOps.fit(Image.open(source).convert("RGB"), SIZE, method=Image.Resampling.LANCZOS)
        bg = bg.filter(ImageFilter.GaussianBlur(14))
        fg = ImageOps.fit(img, SIZE, method=Image.Resampling.LANCZOS)
        img = Image.blend(bg, fg, 0.88)
    else:
        img = ImageOps.fit(img, SIZE, method=Image.Resampling.LANCZOS)

    img.save(target, optimize=True)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, spec in SOURCES.items():
        source = SRC / spec["source"]
        if not source.exists():
            raise FileNotFoundError(
                f"Missing {source}. Download source from: {spec['url']}"
            )
        target = OUT / name
        export(source, spec["crop"], target)
        print(target)


if __name__ == "__main__":
    main()
