import pandas as pd
import read
import re

def read_domains(file):
    df = file
    domains_df = df["url"]
    domains = domains_df.value_counts().nlargest(100)
    no_sub_list = []
    for name, row in domains.items():
        no_sub_domain = re.match(r'(?:\w*://)?(?:.*\.)?([a-zA-Z-1-9]*\.[a-zA-Z]{1,}).*', name)
        no_sub_list.append(no_sub_domain)
        return no_sub_list

read_domains(read.load_data())
