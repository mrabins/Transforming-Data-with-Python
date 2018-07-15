import pandas as pd
import read

def read_domains(file):
    df = file
    domains_df = df["url"]
    domains = domains_df.value_counts()
    for name, row in domains.items():
        print("{0}: {1}".format(name, row))

read_domains(read.load_data())
