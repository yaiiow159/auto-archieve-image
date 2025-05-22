import os
import re
import sys
from PIL import Image
from tqdm import tqdm

IMAGE_EXTS = [".jpg", ".jpeg", ".png", ".bmp", ".webp"]

def find_images(root, pattern):
    matched = []
    regex = re.compile(pattern, re.IGNORECASE)
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if any(fname.lower().endswith(ext) for ext in IMAGE_EXTS):
                if regex.fullmatch(fname) or regex.match(fname):
                    matched.append(os.path.join(dirpath, fname))
    return matched

def compress_image(path, quality=85):
    try:
        img = Image.open(path)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        ext = os.path.splitext(path)[1].lower()
        if ext in [".jpg", ".jpeg"]:
            img.save(path, "JPEG", quality=quality, optimize=True)
        elif ext == ".webp":
            img.save(path, "WEBP", quality=quality, optimize=True)
        elif ext == ".png":
            try:
                img_quant = img.quantize(method=Image.MEDIANCUT)
                img_quant.save(path, "PNG", optimize=True)
            except Exception:
                img.save(path, "PNG", optimize=True)
        else:
            img.save(path)
        return True
    except Exception as e:
        print(f"壓縮失敗: {path}，錯誤: {e}")
        return False

def main():
    if len(sys.argv) < 3:
        print('用法: python image_compressor.py <資料夾路徑> <正則表達式> [壓縮品質(1-100, 預設85)]')
        print('範例: python image_compressor.py ./images ".*\\.png$" 90')
        sys.exit(1)
    root = sys.argv[1]
    pattern = sys.argv[2]
    quality = int(sys.argv[3]) if len(sys.argv) > 3 else 85
    images = find_images(root, pattern)
    if not images:
        print("找不到符合條件的圖片")
        return
    print(f"共找到 {len(images)} 張圖片，開始壓縮...")
    for img_path in tqdm(images):
        compress_image(img_path, quality)
    print("壓縮完成！")

if __name__ == "__main__":
    main() 