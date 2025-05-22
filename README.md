# 圖片壓縮工具

這是一個用 Python 撰寫的圖片壓縮小工具，可依指定路徑與正則表達式批次壓縮圖片，壓縮後不失真。

## 需求
- Python 3.7+
- Pillow
- tqdm

## 安裝依賴

建議使用虛擬環境：
```bash
python -m venv venv
source venv/bin/activate  # Windows 請用 venv\Scripts\activate
pip install -r requirements.txt  # 或手動安裝 pillow tqdm
```

## 用法

```bash
python image_compressor.py <資料夾路徑> <正則表達式> [壓縮品質(1-100, 預設85)]
```

### 範例

壓縮所有 png 檔案：
```bash
python image_compressor.py ./images ".*\\.png$" 90
```

壓縮所有 jpg 檔案（品質 80）：
```bash
python image_compressor.py ./photos ".*\\.jpg$" 80
```

## 說明
- 支援 jpg、jpeg、png、bmp、webp
- png 會自動最佳化，jpg/webp 可調整品質（預設85，數字越小壓縮越大但可能失真）
- 會自動遞迴搜尋子資料夾 

## 一鍵啟動腳本

### Linux/macOS (bash)

```bash
bash start.sh <資料夾路徑> <正則表達式> [壓縮品質]
```

範例：
```bash
bash start.sh ./images ".*\\.png$" 90
```

### Windows (bat)

```bat
start.bat <資料夾路徑> <正則表達式> [壓縮品質]
```

範例：
```bat
start.bat .\images ".*\.png$" 90
```

- 路徑可用相對或絕對路徑
- 參數與 python 直接執行相同 