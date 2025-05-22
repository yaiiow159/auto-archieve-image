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

## 啟動腳本流程

### PowerShell 執行
```powershell
.\venv\Scripts\Activate
pip install -r requirements.txt

python image_compressor.py "<資料夾路徑>" "<正則表達式>" [壓縮比]

./start.bat "<資料夾路徑>" ".*\.(jpg^|jpeg^|png^|bmp^|webp)$" [壓縮比]

cmd /c start.bat "<資料夾路徑>" ".*\.(jpg|jpeg|png|bmp|webp)$" [壓縮比]
```

### CMD 執行
```cmd
# 直接執行 bat 腳本
start.bat "<資料夾路徑>" ".*\.(jpg|jpeg|png|bmp|webp)$" [壓縮比]
```

---

## 正則表達式範例
- `.*\.png$`：所有 png
- `.*\.(jpg|jpeg)$`：所有 jpg、jpeg
- `.*\.(jpg|jpeg|png|bmp|webp)$`：所有支援格式
- `^IMG_.*\.jpg$`：檔名開頭為 IMG_ 的 jpg
- `Snipaste_2025-05-19_13-21-31.png$`：指定單一檔案

---

## 壓縮比設置
- 第三個參數為壓縮比（品質），數字 1~100，數字越小壓縮越大（失真風險高），越大畫質越好（檔案較大）
- 建議 80~90 之間
- PNG 會自動最佳化與減色，壓縮比參數不影響 PNG

### 範例
壓縮所有 jpg，品質 80：
```powershell
python image_compressor.py "C:\Users\yaiio\OneDrive\文件" ".*\.jpg$" 80
```
壓縮所有格式，品質 90：
```powershell
python image_compressor.py "C:\Users\yaiio\OneDrive\文件" ".*\.(jpg|jpeg|png|bmp|webp)$" 90
```
壓縮單一 png（PNG 只會自動最佳化與減色）：
```powershell
python image_compressor.py "C:\Users\yaiio\OneDrive\文件" "Snipaste_2025-05-19_13-21-31.png"
``` 