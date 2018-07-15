import pandas as pd

if __name__ == "__main__":
    print("Welcome to a Python script")

def load_data():
    df = pd.read_csv("hn_stories.csv", sep=",", names=["submission_time", "upvotes", "url", "headline" ])
    return df

load_data()
