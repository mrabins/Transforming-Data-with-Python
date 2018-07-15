import read
from collections import Counter

def read_files(file):
    df = file
    combined_headlines = df["headline"].str.cat(sep=" ").lower()
    counter = Counter(combined_headlines.split())
    print(counter.most_common(100))

read_files(read.load_data())
