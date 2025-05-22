#!/bin/bash

if [ ! -d "venv" ]; then
  python3 -m venv venv
fi
source venv/bin/activate
pip install -q pillow tqdm
python image_compressor.py "$@" 