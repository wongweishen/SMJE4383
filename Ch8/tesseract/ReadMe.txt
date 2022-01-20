python3 -m venv venv
. venv/bin/activate
pip install fastapi
pip install uvicorn
pip install opencv-python-headless
pip install opencv-python
pip install pytesseract
pip freeze>requirements.txt
docker build -t python-ocr .
docker run -p 8000:8000 python-ocr
click on link
