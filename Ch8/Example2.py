#https://gutenberg.org/cache/epub/1513/pg1513.txt
from pathlib import Path
from textblob import TextBlob
blob = TextBlob (Path('RomeoandJuliet.txt').read_text())
items = blob.word_counts.items()

