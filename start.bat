@echo off
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate.bat
pip install -q pillow tqdm
python image_compressor.py %* 