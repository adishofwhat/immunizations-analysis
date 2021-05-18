import pandas as pd
import numpy as np

def proportion_of_education():     
    df = pd.read_csv("assets/NISPUF17.csv", index_col = 0)
    mother = df["EDUC1"]
    sm = (sorted(mother))
    total = len(sm)
    one = 0 
    two = 0
    thr = 0
    fou = 0
    for i in sm:
        if i == 1:
            one = one + 1
        elif i == 2:
            two = two + 1
        elif i == 3:
            thr = thr + 1
        elif i == 4:
            fou = fou + 1
    dict = {"less than high school" : one/total,
            "high school" : two/total,
            "more than high school but not college" : thr/total,
            "college" : fou/total}
    return dict
